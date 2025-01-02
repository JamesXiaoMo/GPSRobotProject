# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BLE.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_BLE(object):
    def setupUi(self, BLE):
        if not BLE.objectName():
            BLE.setObjectName(u"BLE")
        BLE.resize(400, 200)
        icon = QIcon()
        icon.addFile(u":/images/assets/images/bluetooth.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        BLE.setWindowIcon(icon)
        self.label = QLabel(BLE)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 130, 54, 16))
        self.label_2 = QLabel(BLE)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 160, 71, 16))
        self.lineEdit = QLineEdit(BLE)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 130, 141, 20))
        self.lineEdit_2 = QLineEdit(BLE)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 160, 141, 20))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton = QPushButton(BLE)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(285, 157, 90, 24))
        self.pushButton_2 = QPushButton(BLE)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(285, 127, 90, 24))
        self.listWidget = QListWidget(BLE)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(25, 10, 350, 100))

        self.retranslateUi(BLE)

        QMetaObject.connectSlotsByName(BLE)
    # setupUi

    def retranslateUi(self, BLE):
        BLE.setWindowTitle(QCoreApplication.translate("BLE", u"BLE\u914d\u7db2", None))
        self.label.setText(QCoreApplication.translate("BLE", u"Wi-Fi\u540d:", None))
        self.label_2.setText(QCoreApplication.translate("BLE", u"\u30d1\u30b9\u30ef\u30fc\u30c9:", None))
        self.pushButton.setText(QCoreApplication.translate("BLE", u"\u9001\u4fe1", None))
        self.pushButton_2.setText(QCoreApplication.translate("BLE", u"\u30ea\u30d5\u30ec\u30c3\u30b7\u30e5", None))
    # retranslateUi

