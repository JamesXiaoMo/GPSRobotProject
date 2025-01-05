from PySide6.QtWidgets import QDialog

from windows.BLEUI import Ui_BLE


class BLE(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BLE()
        self.ui.setupUi(self)

    def ShowBLE(self):
        self.exec()