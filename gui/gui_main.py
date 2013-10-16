# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_designer/gui_main.ui'
#
# Created: Thu Oct 17 01:28:20 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(270, 215)
        MainWindow.setMinimumSize(QtCore.QSize(270, 215))
        MainWindow.setMaximumSize(QtCore.QSize(270, 215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/binary-tree.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 121))
        self.label.setStatusTip(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.inp_filefullpath = QtGui.QLineEdit(self.centralwidget)
        self.inp_filefullpath.setGeometry(QtCore.QRect(10, 130, 211, 27))
        self.inp_filefullpath.setObjectName(_fromUtf8("inp_filefullpath"))
        self.btn_analize = QtGui.QPushButton(self.centralwidget)
        self.btn_analize.setGeometry(QtCore.QRect(230, 130, 31, 27))
        self.btn_analize.setObjectName(_fromUtf8("btn_analize"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 25))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout_Bytestat = QtGui.QAction(MainWindow)
        self.actionAbout_Bytestat.setObjectName(_fromUtf8("actionAbout_Bytestat"))
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_Bytestat)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Bytestat", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"justify\">This program parses and outputs <br/>information about how much <br/>once a file is encountered every byte.</p><p>To get started, open the file:<br/><span style=\" font-style:italic;\">File -&gt; Open</span><br/>Or type the path: </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.inp_filefullpath.setStatusTip(QtGui.QApplication.translate("MainWindow", "Specify the full path to the file", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_analize.setStatusTip(QtGui.QApplication.translate("MainWindow", "Analyze file", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_analize.setText(QtGui.QApplication.translate("MainWindow", ":-)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setStatusTip(QtGui.QApplication.translate("MainWindow", "Open file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Close program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Bytestat.setText(QtGui.QApplication.translate("MainWindow", "About Bytestat", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Bytestat.setStatusTip(QtGui.QApplication.translate("MainWindow", "Show information", None, QtGui.QApplication.UnicodeUTF8))

