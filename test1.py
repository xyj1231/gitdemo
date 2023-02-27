# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 541)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("OneDrive/桌面/Code/08/image/图标 (7).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionping = QtWidgets.QAction(MainWindow)
        self.actionping.setObjectName("actionping")
        self.actionjilian = QtWidgets.QAction(MainWindow)
        self.actionjilian.setObjectName("actionjilian")
        self.menu.addSeparator()
        self.menu.addAction(self.actionnew)
        self.menu.addAction(self.actionping)
        self.menu.addAction(self.actionjilian)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Good"))
        self.menu.setTitle(_translate("MainWindow", "子窗体操作"))
        self.actionnew.setText(_translate("MainWindow", "新建"))
        self.actionping.setText(_translate("MainWindow", "平铺"))
        self.actionjilian.setText(_translate("MainWindow", "级联"))

import img_rc


if __name__ == "__main__":
	print("hot-fix test")
	print("gokakakhello")
	print("hotfix")
