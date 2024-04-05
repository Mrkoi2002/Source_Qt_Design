# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PagesmnpLei.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)
# IMPORT QT CORE
from Qt_Core import *

class Ui_Application_Pages(object):
    def setupUi(self, Application_Pages):
        if not Application_Pages.objectName():
            Application_Pages.setObjectName(u"Application_Pages")
        Application_Pages.resize(1034, 568)
        self.Home_Pages = QWidget()
        self.Home_Pages.setObjectName(u"Home_Pages")
        self.verticalLayout = QVBoxLayout(self.Home_Pages)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.Home_Pages)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        Application_Pages.addWidget(self.Home_Pages)
        self.File_Pages = QWidget()
        self.File_Pages.setObjectName(u"File_Pages")
        self.verticalLayout_2 = QVBoxLayout(self.File_Pages)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.File_Pages)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        Application_Pages.addWidget(self.File_Pages)

        self.retranslateUi(Application_Pages)

        QMetaObject.connectSlotsByName(Application_Pages)
    # setupUi

    def retranslateUi(self, Application_Pages):
        Application_Pages.setWindowTitle(QCoreApplication.translate("Application_Pages", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("Application_Pages", u"Home", None))
        self.label_2.setText(QCoreApplication.translate("Application_Pages", u"File_Pages", None))
    # retranslateUi

