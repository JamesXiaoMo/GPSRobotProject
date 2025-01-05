from PySide6.QtWidgets import QDialog

from windows.ConnectErrorUI import Ui_ConnectError


class ConnectError(QDialog):
    """
        ”连接错误“弹窗类
    """

    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.ui = Ui_ConnectError()
        self.ui.setupUi(self)

    def ShowConnectError(self):
        """
        ”连接失败“弹窗的槽
        :return:
        """
        self.exec()
        self.mainWindow.ui.lineEdit.setText("")
        self.mainWindow.ui.lineEdit_2.setText("")