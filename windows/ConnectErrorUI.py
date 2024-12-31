# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConnectError.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
import resources_rc

class Ui_ConnectError(object):
    def setupUi(self, ConnectError):
        if not ConnectError.objectName():
            ConnectError.setObjectName(u"ConnectError")
        ConnectError.resize(300, 100)
        icon = QIcon()
        icon.addFile(u":/images/assets/images/error.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ConnectError.setWindowIcon(icon)
        self.label = QLabel(ConnectError)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(35, 10, 230, 50))
        self.pushButton = QPushButton(ConnectError)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(112, 60, 75, 24))

        self.retranslateUi(ConnectError)
        self.pushButton.clicked.connect(ConnectError.accept)

        QMetaObject.connectSlotsByName(ConnectError)
    # setupUi

    def retranslateUi(self, ConnectError):
        ConnectError.setWindowTitle(QCoreApplication.translate("ConnectError", u"\u63a5\u7d9a\u30a8\u30e9\u30fc", None))
        self.label.setText(QCoreApplication.translate("ConnectError", u"\u30de\u30a4\u30af\u30ed\u30b3\u30f3\u30c8\u30ed\u30fc\u30e9\u30fc\u306b\u63a5\u7d9a\u3067\u304d\u307e\u305b\u3093", None))
        self.pushButton.setText(QCoreApplication.translate("ConnectError", u"\u78ba\u8a8d", None))
    # retranslateUi

