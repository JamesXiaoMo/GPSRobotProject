# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControllerSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)
import resources_rc

class Ui_ControllerSettings(object):
    def setupUi(self, ControllerSettings):
        if not ControllerSettings.objectName():
            ControllerSettings.setObjectName(u"ControllerSettings")
        ControllerSettings.resize(350, 100)
        icon = QIcon()
        icon.addFile(u":/images/assets/images/controller.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ControllerSettings.setWindowIcon(icon)
        self.label = QLabel(ControllerSettings)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 20, 81, 16))
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(ControllerSettings)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 20, 171, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_3 = QLabel(ControllerSettings)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 40, 71, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(ControllerSettings)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 40, 54, 16))
        self.label_5 = QLabel(ControllerSettings)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 60, 71, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(ControllerSettings)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 60, 54, 16))
        self.label_7 = QLabel(ControllerSettings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 20, 60, 60))
        self.label_7.setPixmap(QPixmap(u":/images/assets/images/controller.png"))
        self.label_7.setScaledContents(True)

        self.retranslateUi(ControllerSettings)

        QMetaObject.connectSlotsByName(ControllerSettings)
    # setupUi

    def retranslateUi(self, ControllerSettings):
        ControllerSettings.setWindowTitle(QCoreApplication.translate("ControllerSettings", u"\u30b3\u30f3\u30c8\u30ed\u30fc\u30e9\u30fc\u306e\u8a2d\u5b9a", None))
        self.label.setText(QCoreApplication.translate("ControllerSettings", u"\u30b3\u30f3\u30c8\u30ed\u30fc\u30e9:", None))
        self.label_2.setText(QCoreApplication.translate("ControllerSettings", u"\u672a\u63a5\u7d9a", None))
        self.label_3.setText(QCoreApplication.translate("ControllerSettings", u"\u524d\u5f8c\u306e\u5236\u5fa1:", None))
        self.label_4.setText(QCoreApplication.translate("ControllerSettings", u"0%", None))
        self.label_5.setText(QCoreApplication.translate("ControllerSettings", u"\u5de6\u53f3\u306e\u5236\u5fa1:", None))
        self.label_6.setText(QCoreApplication.translate("ControllerSettings", u"0%", None))
        self.label_7.setText("")
    # retranslateUi

