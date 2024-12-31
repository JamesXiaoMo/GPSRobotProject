# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoScan.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QProgressBar,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import resources_rc

class Ui_AutoScan(object):
    def setupUi(self, AutoScan):
        if not AutoScan.objectName():
            AutoScan.setObjectName(u"AutoScan")
        AutoScan.resize(400, 200)
        icon = QIcon()
        icon.addFile(u":/images/assets/images/radar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AutoScan.setWindowIcon(icon)
        self.tableWidget = QTableWidget(AutoScan)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(25, 20, 350, 100))
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(174)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.progressBar = QProgressBar(AutoScan)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 125, 350, 23))
        self.progressBar.setValue(0)
        self.pushButton = QPushButton(AutoScan)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(45, 160, 100, 24))
        self.pushButton_2 = QPushButton(AutoScan)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(150, 160, 100, 24))
        self.pushButton_3 = QPushButton(AutoScan)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(255, 160, 100, 24))

        self.retranslateUi(AutoScan)
        self.pushButton_3.clicked.connect(AutoScan.reject)

        QMetaObject.connectSlotsByName(AutoScan)
    # setupUi

    def retranslateUi(self, AutoScan):
        AutoScan.setWindowTitle(QCoreApplication.translate("AutoScan", u"\u30aa\u30fc\u30c8\u30b9\u30ad\u30e3\u30f3", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AutoScan", u"IP\u30a2\u30c9\u30ec\u30b9", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AutoScan", u"\u30dd\u30fc\u30c8", None));
        self.pushButton.setText(QCoreApplication.translate("AutoScan", u"\u30aa\u30fc\u30c8\u30b9\u30ad\u30e3\u30f3", None))
        self.pushButton_2.setText(QCoreApplication.translate("AutoScan", u"\u78ba\u8a8d", None))
        self.pushButton_3.setText(QCoreApplication.translate("AutoScan", u"\u30ad\u30e3\u30f3\u30bb\u30eb", None))
    # retranslateUi

