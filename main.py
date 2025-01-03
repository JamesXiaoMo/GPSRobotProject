import datetime
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import pygame

import requests.exceptions
from PySide6.QtCore import QUrl, QTimer, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QHeaderView, QTableWidgetItem

from MainWindowsUI import Ui_MainWindow
from lib import GetIPLocationInfo, GenerateGIS
from windows.AboutSoftwareUI import Ui_AboutSoftware
from windows.AutoScanUI import Ui_AutoScan
from windows.ConnectErrorUI import Ui_ConnectError
from windows.ControllerSettingsUI import Ui_ControllerSettings
from windows.BLEUI import Ui_BLE


class AboutSoftware(QDialog):
    """
    “关于软件”弹窗类
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutSoftware()
        self.ui.setupUi(self)


def ShowAboutSoftwareDialog():
    """
    显示“关于软件”窗口的槽
    :return:
    """
    dialog = AboutSoftware()
    dialog.exec()


def scan_ip(target_ip, port=7769, timeout=2):
    """
    扫描单个 IP 的指定端口是否开放
    :param target_ip: 目标 IP 地址
    :param port: 目标端口号
    :param timeout: 超时时间
    :return: (IP, 是否成功)
    """
    try:
        with socket.create_connection((target_ip, port), timeout=timeout):
            return target_ip  # 返回成功的 IP 地址
    except (socket.timeout, socket.error):
        return None  # 返回 None 表示失败


class AutoScan(QDialog):
    """
    ”自动扫描“弹窗类
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_AutoScan()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0, 240)
        self.ui.tableWidget.setColumnWidth(1, 100)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.pushButton.clicked.connect(self.ScanDevices)
        self.ui.tableWidget.itemSelectionChanged.connect(self.SelectIP)
        self.ui.pushButton_2.clicked.connect(self.accept)
        self.selectedIP = None

    def ScanDevices(self):
        """
        多线程优化的设备扫描方法
        """
        self.ui.tableWidget.setRowCount(0)
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            ip_parts = local_ip.split('.')
            network = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}."
            devices = []

            with ThreadPoolExecutor(max_workers=50) as executor:
                futures = {executor.submit(scan_ip, f"{network}{i}"): i for i in range(1, 255)}
                for future in futures:
                    ip_index = futures[future]
                    try:
                        result = future.result()
                        if result:
                            devices.append(result)

                            current_row = self.ui.tableWidget.rowCount()
                            self.ui.tableWidget.insertRow(current_row)
                            self.ui.tableWidget.setItem(current_row, 0, QTableWidgetItem(result))
                            self.ui.tableWidget.setItem(current_row, 1, QTableWidgetItem(str(7769)))

                        progress = int((ip_index / 254) * 100)
                        self.ui.progressBar.setValue(progress)

                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)

    def SelectIP(self):
        selected_items = self.ui.tableWidget.selectedItems()
        if selected_items:
            item = selected_items[0]
            row = item.row()
            self.ui.pushButton_2.setEnabled(True)  # 启用按钮
            ip_item = self.ui.tableWidget.item(row, 0)
            self.selectedIP = ip_item.text()
        else:
            self.ui.pushButton_2.setEnabled(False)  # 禁用按钮

    def GetIP(self):
        return self.selectedIP


class ConnectError(QDialog):
    """
        ”连接错误“弹窗类
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_ConnectError()
        self.ui.setupUi(self)


class ControllerSettings(QDialog):
    """
        ”手柄设置“弹窗类
    """

    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_ControllerSettings()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)

    def update(self):
        if self.main_window.isControllerConnected:
            self.ui.label_2.setText(self.main_window.ControllerName)
            self.ui.label_2.setStyleSheet("color: rgb(255, 255, 255);")

            self.ui.label_4.setText(f'{self.main_window.FrontBackAxis}%')
            self.ui.label_6.setText(f'{self.main_window.LeftRightAxis}%')
        else:
            self.ui.label_2.setText("未接続")
            self.ui.label_2.setStyleSheet("color: red")
            self.ui.label_4.setText('0%')
            self.ui.label_6.setText('0%')


class BLEDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BLE()
        self.ui.setupUi(self)


def ShowBLE():
    dialog = BLEDialog()
    dialog.exec()


class MainWindow(QMainWindow):
    Update_Connect_Status = Signal(bool)
    Update_RSSI = Signal(str)
    Update_Interval = Signal(int)
    Update_Command_Line = Signal(str)
    Send_Command = Signal()

    def __init__(self):
        super().__init__()
        self.ManualControl = False  # 是否启用手动控制
        self.isESPConnected = False  # ESP是否连接

        self.isControllerConnected = False
        self.ControllerName = None
        self.controllers = []
        self.FrontBackAxis = 0
        self.LeftRightAxis = 0

        self.isGetPong = False  # 是否接收到Pong
        self.PongTime = None  # 接收到Pong的时间戳
        self.TCP_SOCKET = None  # Socket对象
        self.t1 = None  # t1线程用于TCP收信
        self.t2 = None  # t2线程用于Ping-Pong
        self.t3 = threading.Thread(target=self.ControllerOperation)
        self.t3.daemon = True
        self.t3.start()
        self.pause = None  # t1和t2共享Event用于计算网络延迟时间
        self.ui = Ui_MainWindow()  # 创建界面实例
        self.ui.setupUi(self)  # 初始化界面
        self.ui.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)  #
        # 允许访问本地文件
        self.ui.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)  #
        # 允许访问本地文件
        self.MapUpdate(0)  # 初始化地图
        # 自动更新地图功能
        self.auto_map_update = QTimer(self)
        self.auto_map_update.setInterval(10000)
        self.auto_map_update.timeout.connect(self.AutoMapUpdate)
        self.auto_map_update.start()
        # 信号/槽
        self.ui.horizontalSlider.valueChanged.connect(lambda: self.SliderDataUpdate(0))
        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.SliderDataUpdate(1))
        self.ui.horizontalSlider_4.valueChanged.connect(lambda: self.SliderDataUpdate(2))
        self.ui.horizontalSlider_3.valueChanged.connect(lambda: self.SliderDataUpdate(3))
        self.ui.radioButton.clicked.connect(self.ManualControlUpdate)
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.MapUpdate(self.ui.comboBox.currentIndex()))
        self.ui.pushButton_3.clicked.connect(self.MapUpdate)
        self.ui.pushButton_4.clicked.connect(self.ESPConnect)
        self.ui.action.triggered.connect(self.SwitchFullScreen)
        self.ui.action_4.triggered.connect(ShowAboutSoftwareDialog)
        self.ui.action_2.triggered.connect(self.close)
        self.ui.pushButton_5.clicked.connect(self.ShowAutoScan)
        self.ui.action_3.triggered.connect(self.ShowControllerSettings)
        self.Update_Connect_Status.connect(self.UpdateConnectStatus)
        self.Update_RSSI.connect(self.UpdateRSSI)
        self.Update_Interval.connect(self.UpdateInterval)
        self.Update_Command_Line.connect(self.UpdateCommandLine)
        self.Send_Command.connect(self.SendCommand)
        self.ui.pushButton_7.clicked.connect(self.Send_Command)
        self.ui.pushButton_6.clicked.connect(ShowBLE)

    def SliderDataUpdate(self, no):
        """
        根据进度条更新对应的标签信息
        :param no: 进度条序号
        :return:
        """
        if no == 0:
            self.ui.label_7.setText(str(self.ui.horizontalSlider.value()))
        elif no == 1:
            self.ui.label_8.setText(str(self.ui.horizontalSlider_2.value()))
        elif no == 2:
            self.ui.label_15.setText(f'{str(self.ui.horizontalSlider_4.value())}%')
        elif no == 3:
            self.ui.label_16.setText(f'{str(self.ui.horizontalSlider_3.value())}%')

    def ManualControlUpdate(self):
        """
        启动/关闭对电机的手动控制
        :return:
        """
        self.ManualControl = not self.ManualControl
        self.ui.horizontalSlider_3.setEnabled(self.ManualControl)
        self.ui.horizontalSlider_4.setEnabled(self.ManualControl)
        if not self.ManualControl:
            self.ui.horizontalSlider_4.setValue(0)
            self.ui.horizontalSlider_3.setValue(0)

    def MapUpdate(self, map_center: int = False):
        """
        更新地图
        :param map_center: 地图中心参数
        :return:
        """
        IP_GIS = None
        if not map_center:
            map_center = self.ui.comboBox.currentIndex()
        try:
            IP_GIS = GetIPLocationInfo.get_ip_location_info()
        except requests.exceptions.ConnectionError as e:
            print("1" + str(e))
        Map_Path = GenerateGIS.create_map(map_center, IP_GIS)
        self.ui.webEngineView.setUrl(QUrl.fromLocalFile(Map_Path))
        self.ui.label_12.setText(f'{str(IP_GIS[0])},{str(IP_GIS[1])}')

    def AutoMapUpdate(self):
        """
        自动更新地图
        :return:
        """
        if self.ui.checkBox.isChecked():
            self.MapUpdate()

    def SwitchFullScreen(self):
        """
        切换全屏和窗口显示
        :return:
        """
        if not self.isFullScreen():
            self.showFullScreen()
            self.ui.action.setText("通常表示")
        else:
            self.showNormal()
            self.ui.action.setText("全画面表示")

    def ESPConnect(self):
        """
        连接ESP芯片
        :return:
        """
        if not self.isESPConnected:
            try:
                self.TCP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP连接对象
                self.TCP_SOCKET.settimeout(10)
                self.TCP_SOCKET.connect((str(self.ui.lineEdit.text()), int(self.ui.lineEdit_2.text())))
            except WindowsError as e:
                print("2" + str(e))
                self.ShowConnectError()
            except socket.error as e:
                print("a" + e)
                self.ShowConnectError()
            else:
                self.ui.lineEdit.setEnabled(False)
                self.ui.lineEdit_2.setEnabled(False)
                self.ui.pushButton_4.setText("切断する")
                self.isESPConnected = True
                self.t1 = threading.Thread(target=self.ESPListen)  # 监听线程初始化
                self.t1.daemon = True  # 监听线程修改成守护线程
                self.t1.start()
                self.ESPSend(data="Connect")
        else:
            self.TCP_SOCKET.close()
            self.Update_Connect_Status.emit(False)

    def ESPSend(self, data: str):
        """
        向ESP芯片发送数据
        :param data: 数据
        :return:
        """
        if self.isESPConnected and self.TCP_SOCKET:
            try:
                self.TCP_SOCKET.sendall((data + '\n').encode('utf-8'))
            except OSError as e:
                print("3" + str(e))
            print(f'>>> {data}')
            self.Update_Command_Line.emit(f'>>> {data}')

    def ESPListen(self):
        """
        监听ESP芯片的数据
        :return:
        """
        while self.isESPConnected:
            try:
                data = self.TCP_SOCKET.recv(1024).decode('utf-8').strip('\n').strip('\r')
                if data:
                    print(f'<<< {data}')
                    self.Update_Command_Line.emit(f'<<< {data}')
                    if data == "ConnectOK":
                        print("Connect successfully")
                        self.Update_Command_Line.emit("### EPS connect successfully!!")
                        self.Update_Connect_Status.emit(True)
                        self.t2 = threading.Thread(target=self.ESPPingPong)  # Ping-Pong线程初始化
                        self.t2.daemon = True  # Ping-Pong线程修改成守护线程
                        self.t2.start()
                    elif data.startswith("+"):
                        RSSI = data[1:]
                        self.isGetPong = True
                        self.PongTime = datetime.datetime.now()
                        self.pause.set()
                        self.Update_RSSI.emit(RSSI)
            except OSError as e:
                print("4" + str(e))
                self.Update_Connect_Status.emit(False)
            except socket.error as e:
                print(f"Socket error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def ESPPingPong(self):
        """
        Ping-Pong
        :return:
        """
        while self.isESPConnected:
            self.ESPSend(data="RSSI")
            start_time = datetime.datetime.now()
            self.pause = threading.Event()
            self.pause.wait()
            Interval = int((self.PongTime - start_time).total_seconds() * 1000)
            if self.isGetPong:
                self.Update_Interval.emit(Interval)
            else:
                self.Update_Connect_Status.emit(False)
            self.isGetPong = False
            time.sleep(5)

    def ShowAutoScan(self):
        """
        ”自动扫描“弹窗的槽
        :return:
        """
        dialog = AutoScan()
        if dialog.exec() == QDialog.Accepted:
            ip = dialog.GetIP()
            self.ui.lineEdit.setText(ip)
            self.ui.lineEdit_2.setText("7769")
            self.ui.pushButton_4.click()

    def ShowConnectError(self):
        """
        ”连接失败“弹窗的槽
        :return:
        """
        dialog = ConnectError()
        dialog.exec()
        self.ui.lineEdit.setText("")
        self.ui.lineEdit_2.setText("")

    def ShowControllerSettings(self):
        """
            显示“手柄控制”窗口的槽
            :return:
        """
        dialog = ControllerSettings(main_window=self)
        dialog.exec()

    def UpdateConnectStatus(self, isConnected: bool):
        if isConnected:
            self.ui.label_21.setText("接続済み")
            self.ui.label_21.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.ui.lineEdit.setEnabled(True)
            self.ui.lineEdit_2.setEnabled(True)
            self.ui.pushButton_4.setText("接続する")
            self.isESPConnected = False
            self.Update_Command_Line.emit("### ESP disconnected!!")
            self.ui.label_21.setText("未接続")
            self.ui.label_21.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_22.setText('9999ms')
            self.ui.label_22.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_23.setPixmap(QPixmap(u":/images/assets/images/wifi_0.png"))
            self.ui.label_24.setText("-99dBm")
            self.ui.label_24.setStyleSheet("color: rgb(255, 0, 0);")

    def UpdateRSSI(self, RSSI: str):
        self.ui.label_24.setText(f'{RSSI}dBm')
        if -51 <= int(RSSI) <= 0:
            self.ui.label_24.setStyleSheet("color: rgb(0, 255, 0);")
            self.ui.label_23.setPixmap(QPixmap(u":/images/assets/images/wifi_2.png"))
        elif -70 <= int(RSSI) < -51:
            self.ui.label_24.setStyleSheet("color: rgb(255, 255, 0);")
            self.ui.label_23.setPixmap(QPixmap(u":/images/assets/images/wifi_1.png"))
        else:
            self.ui.label_24.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_23.setPixmap(QPixmap(u":/images/assets/images/wifi_0.png"))

    def UpdateInterval(self, Interval: int):
        self.ui.label_22.setText(f'{Interval} ms')
        if 0 <= Interval <= 1000:
            self.ui.label_22.setStyleSheet("color: rgb(0, 255, 0);")
        elif 1000 < Interval <= 2000:
            self.ui.label_22.setStyleSheet("color: rgb(255, 255, 0);")
        else:
            self.ui.label_22.setStyleSheet("color: rgb(255, 0, 0);")

    def ControllerOperation(self):
        pygame.init()
        pygame.joystick.init()

        while True:
            if pygame.joystick.get_count() != 0:
                for i in range(pygame.joystick.get_count()):
                    joystick = pygame.joystick.Joystick(i)
                    joystick.init()
                    print(f"Joystick {i}: {joystick.get_name()} initialized")
                    self.Update_Command_Line.emit(f"### Joystick {i}: {joystick.get_name()} initialized")
                    self.ControllerName = joystick.get_name()
                self.isControllerConnected = True
            else:
                self.isControllerConnected = False
                self.ControllerName = None
                for event in pygame.event.get():
                    if event.type == pygame.JOYDEVICEADDED:
                        joystick = pygame.joystick.Joystick(event.device_index)
                        joystick.init()
                        self.ControllerName = joystick.get_name()
                        self.isControllerConnected = True
                        print(f"New joystick connected: {self.ControllerName}")
                        self.Update_Command_Line.emit(f"New joystick connected: {self.ControllerName}")
            while pygame.joystick.get_count() != 0:
                for event in pygame.event.get():
                    if event.type == pygame.JOYBUTTONDOWN:
                        print(f"Button {event.button} pressed on joystick {event.joy}")
                    elif event.type == pygame.JOYAXISMOTION:
                        if event.axis == 1:
                            axis_data = int(event.value * -100)
                            if -10 < axis_data < 10:
                                axis_data = 0
                            self.FrontBackAxis = axis_data
                        if event.axis == 2:
                            axis_data = int(event.value * -100)
                            if -10 < axis_data < 10:
                                axis_data = 0
                            self.LeftRightAxis = axis_data
                pygame.time.wait(10)
            time.sleep(1)

    def UpdateCommandLine(self, cmd: str):
        self.ui.plainTextEdit.appendPlainText(f'{datetime.datetime.now().strftime("%H:%M:%S")}   {cmd}')

    def SendCommand(self):
        if self.ui.lineEdit_3.text() != "":
            if self.isESPConnected:
                self.ESPSend(data=self.ui.lineEdit_3.text())
            self.ui.lineEdit_3.clear()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
