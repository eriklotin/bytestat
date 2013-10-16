# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_designer/gui_alert.ui'
#
# Created: Thu Oct 17 00:55:04 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_alertwin(object):
    def setupUi(self, alertwin):
        alertwin.setObjectName(_fromUtf8("alertwin"))
        alertwin.setWindowModality(QtCore.Qt.WindowModal)
        alertwin.resize(400, 100)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(alertwin.sizePolicy().hasHeightForWidth())
        alertwin.setSizePolicy(sizePolicy)
        alertwin.setMinimumSize(QtCore.QSize(400, 100))
        alertwin.setMaximumSize(QtCore.QSize(400, 100))
        self.btn_alertOk = QtGui.QPushButton(alertwin)
        self.btn_alertOk.setGeometry(QtCore.QRect(150, 70, 98, 27))
        self.btn_alertOk.setObjectName(_fromUtf8("btn_alertOk"))
        self.alertText = QtGui.QLabel(alertwin)
        self.alertText.setGeometry(QtCore.QRect(15, 17, 371, 41))
        self.alertText.setObjectName(_fromUtf8("alertText"))

        self.retranslateUi(alertwin)
        QtCore.QMetaObject.connectSlotsByName(alertwin)

    def retranslateUi(self, alertwin):
        alertwin.setWindowTitle(QtGui.QApplication.translate("alertwin", "Message", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_alertOk.setText(QtGui.QApplication.translate("alertwin", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.alertText.setText(QtGui.QApplication.translate("alertwin", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

