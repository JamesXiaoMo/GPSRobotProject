from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from concurrent.futures import ThreadPoolExecutor
from windows.AutoScanUI import Ui_AutoScan
import socket


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

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
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

    def ShowAutoScan(self):
        """
        ”自动扫描“弹窗的槽
        :return:
        """
        # dialog = AutoScan()
        if self.exec() == QDialog.Accepted:
            ip = self.GetIP()
            self.mainWindow.ui.lineEdit.setText(ip)
            self.mainWindow.ui.lineEdit_2.setText("7769")
            self.mainWindow.ui.pushButton_4.click()