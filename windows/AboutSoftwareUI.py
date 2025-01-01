# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutSoftware.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QWidget)
import resources_rc
import resources_rc

class Ui_AboutSoftware(object):
    def setupUi(self, AboutSoftware):
        if not AboutSoftware.objectName():
            AboutSoftware.setObjectName(u"AboutSoftware")
        AboutSoftware.resize(400, 200)
        icon = QIcon()
        icon.addFile(u":/images/assets/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AboutSoftware.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(AboutSoftware)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(AboutSoftware)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 20, 64, 64))
        self.label.setPixmap(QPixmap(u":/images/assets/images/icon.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(AboutSoftware)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 40, 221, 31))
        font = QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_3 = QLabel(AboutSoftware)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 70, 54, 16))
        self.label_4 = QLabel(AboutSoftware)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 90, 321, 61))
        self.label_4.setWordWrap(True)
        self.label_5 = QLabel(AboutSoftware)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 155, 231, 16))
        self.label_5.setWordWrap(False)
        self.label_6 = QLabel(AboutSoftware)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 170, 191, 16))

        self.retranslateUi(AboutSoftware)
        self.buttonBox.accepted.connect(AboutSoftware.accept)
        self.buttonBox.rejected.connect(AboutSoftware.reject)

        QMetaObject.connectSlotsByName(AboutSoftware)
    # setupUi

    def retranslateUi(self, AboutSoftware):
        AboutSoftware.setWindowTitle(QCoreApplication.translate("AboutSoftware", u"\u30bd\u30d5\u30c8\u30a6\u30a7\u30a2\u306b\u3064\u3044\u3066", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("AboutSoftware", u"GPS Robot Project", None))
        self.label_3.setText(QCoreApplication.translate("AboutSoftware", u"Alpha.0.1", None))
        self.label_4.setText(QCoreApplication.translate("AboutSoftware", u"  \u3053\u306e\u30bd\u30d5\u30c8\u30a6\u30a7\u30a2\u306f\u3001GPS\u30ed\u30dc\u30c3\u30c8\u7528\u306e\u30db\u30b9\u30c8\u30b3\u30f3\u30d4\u30e5\u30fc\u30bf\u30bd\u30d5\u30c8\u30a6\u30a7\u30a2\u3067\u3059\u3002\u30bd\u30d5\u30c8\u30a6\u30a7\u30a2\u306fMIT\u30e9\u30a4\u30bb\u30f3\u30b9\u306b\u57fa\u3065\u3044\u305f\u30aa\u30fc\u30d7\u30f3\u30bd\u30fc\u30b9\u3067\u3059", None))
        self.label_5.setText(QCoreApplication.translate("AboutSoftware", u"Designed by Wu in Fukuyama University", None))
        self.label_6.setText(QCoreApplication.translate("AboutSoftware", u"Team Members:Oki, Wu, Li, Jiang", None))
    # retranslateUi

