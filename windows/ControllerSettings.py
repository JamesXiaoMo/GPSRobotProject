from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QDialog

from windows.ControllerSettingsUI import Ui_ControllerSettings


class ControllerSettings(QDialog):
    """
        手柄设置弹窗类
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

    def ShowControllerSettings(self):
        """
            显示“手柄控制”窗口的槽
            :return:
        """
        self.exec()