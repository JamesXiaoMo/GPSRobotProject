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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QWidget)
import resources_rc

class Ui_ControllerSettings(object):
    def setupUi(self, ControllerSettings):
        if not ControllerSettings.objectName():
            ControllerSettings.setObjectName(u"ControllerSettings")
        ControllerSettings.resize(400, 200)
        icon = QIcon()
        icon.addFile(u":/images/assets/images/controller.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ControllerSettings.setWindowIcon(icon)

        self.retranslateUi(ControllerSettings)

        QMetaObject.connectSlotsByName(ControllerSettings)
    # setupUi

    def retranslateUi(self, ControllerSettings):
        ControllerSettings.setWindowTitle(QCoreApplication.translate("ControllerSettings", u"\u30b3\u30f3\u30c8\u30ed\u30fc\u30e9\u30fc\u306e\u8a2d\u5b9a", None))
    # retranslateUi

