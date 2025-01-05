from PySide6.QtWidgets import QDialog
from windows.AboutSoftwareUI import Ui_AboutSoftware


class AboutSoftware(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutSoftware()
        self.ui.setupUi(self)

    def ShowAboutSoftwareDialog(self):
        """
        显示“关于软件”窗口的槽
        :return:
        """
        self.exec()