# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/CANO/Desktop/proje/proje.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-image: url(:/wallpaper/arkaplan.jpg);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formWidget = QtWidgets.QWidget(self.centralwidget)
        self.formWidget.setMinimumSize(QtCore.QSize(300, 400))
        self.formWidget.setStyleSheet("#formWidget{\n"
"background-color: rgb(208, 209, 212);\n"
"}")
        self.formWidget.setObjectName("formWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.formWidget)
        self.gridLayout_2.setContentsMargins(20, 20, 20, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.formWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:0, x2:0.5, y2:0.5, stop:0 rgba(0, 83, 255, 255), stop:0.930348 rgba(159, 255, 255, 255));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 9, 0, 1, 2)
        self.suresiz = QtWidgets.QPushButton(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suresiz.sizePolicy().hasHeightForWidth())
        self.suresiz.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.suresiz.setFont(font)
        self.suresiz.setObjectName("suresiz")
        self.gridLayout_2.addWidget(self.suresiz, 7, 0, 1, 2)
        self.bir = QtWidgets.QPushButton(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bir.setFont(font)
        self.bir.setObjectName("bir")
        self.gridLayout_2.addWidget(self.bir, 5, 1, 1, 1)
        self.otuz = QtWidgets.QPushButton(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.otuz.setFont(font)
        self.otuz.setObjectName("otuz")
        self.gridLayout_2.addWidget(self.otuz, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem3, 8, 0, 1, 1)
        self.gridLayout.addWidget(self.formWidget, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CANAYGLR"))
        self.suresiz.setText(_translate("MainWindow", "Süresiz Giriş"))
        self.bir.setText(_translate("MainWindow", "1 Saat"))
        self.otuz.setText(_translate("MainWindow", "30 Dakika"))

import icons_rc
