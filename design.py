# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QGridLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QStatusBar, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(712, 323)
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(16)
        font.setBold(True)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background: #121212;\n"
"	font-family: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid white;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #888 ;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"QTextEdit{\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.reload = QPushButton(self.centralwidget)
        self.reload.setObjectName(u"reload")
        self.reload.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.reload, 0, 1, 1, 3)

        self.copy = QPushButton(self.centralwidget)
        self.copy.setObjectName(u"copy")
        self.copy.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.copy, 0, 4, 1, 1)

        self.digits = QCheckBox(self.centralwidget)
        self.digits.setObjectName(u"digits")
        self.digits.setChecked(True)
        self.digits.setFont(font)
        self.digits.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.digits, 1, 0, 1, 1)

        self.spec = QCheckBox(self.centralwidget)
        self.spec.setObjectName(u"spec")
        self.spec.setFont(font)
        self.spec.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.spec, 2, 0, 1, 5)

        self.low_case = QCheckBox(self.centralwidget)
        self.low_case.setObjectName(u"low_case")
        self.low_case.setChecked(True)
        self.low_case.setFont(font)
        self.low_case.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.low_case, 3, 0, 1, 1)

        self.up_case = QCheckBox(self.centralwidget)
        self.up_case.setObjectName(u"up_case")
        self.up_case.setFont(font)
        self.up_case.setChecked(True)
        self.up_case.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.up_case, 4, 0, 1, 1)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setAlignment(Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setMinimum(6)
        self.spinBox.setMaximum(20)

        self.gridLayout.addWidget(self.spinBox, 5, 2, 1, 1)

        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName(u"generate")
        self.generate.setCursor(QCursor(Qt.PointingHandCursor))
        self.generate.setStyleSheet(u"element.styel {\n"
"border: 3px red;\n"
"}")

        self.gridLayout.addWidget(self.generate, 5, 3, 1, 2)

        self.pas_len = QSlider(self.centralwidget)
        self.pas_len.setObjectName(u"pas_len")
        self.pas_len.setCursor(QCursor(Qt.ClosedHandCursor))
        self.pas_len.setMinimum(6)
        self.pas_len.setMaximum(20)
        self.pas_len.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.pas_len, 5, 0, 1, 1)

        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setFont(font)
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setReadOnly(True)

        self.gridLayout.addWidget(self.password, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.password.raise_()
        self.digits.raise_()
        self.up_case.raise_()
        self.spec.raise_()
        self.low_case.raise_()
        self.generate.raise_()
        self.pas_len.raise_()
        self.spinBox.raise_()
        self.reload.raise_()
        self.copy.raise_()
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Password Generator", None))
        self.reload.setText(QCoreApplication.translate("mainWindow", u"Reload", None))
        self.copy.setText(QCoreApplication.translate("mainWindow", u"Copy", None))
        self.digits.setText(QCoreApplication.translate("mainWindow", u"Digits", None))
        self.spec.setText(QCoreApplication.translate("mainWindow", u"Specials (! \" # $ % & ( ) * + , - . / : ; < = > ? @ [  ] ^ )", None))
        self.low_case.setText(QCoreApplication.translate("mainWindow", u"Lower Case", None))
        self.up_case.setText(QCoreApplication.translate("mainWindow", u"Upper Case", None))
        self.spinBox.setPrefix("")
        self.generate.setText(QCoreApplication.translate("mainWindow", u"Generate", None))
        self.password.setText("")
    # retranslateUi

