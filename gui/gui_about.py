# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_designer/gui_about.ui'
#
# Created: Thu Oct 17 00:55:16 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_aboutwin(object):
    def setupUi(self, aboutwin):
        aboutwin.setObjectName(_fromUtf8("aboutwin"))
        aboutwin.resize(270, 120)
        aboutwin.setMinimumSize(QtCore.QSize(270, 120))
        aboutwin.setSizeGripEnabled(True)
        aboutwin.setModal(True)
        self.label = QtGui.QLabel(aboutwin)
        self.label.setGeometry(QtCore.QRect(10, 0, 251, 91))
        self.label.setObjectName(_fromUtf8("label"))
        self.closebtn = QtGui.QPushButton(aboutwin)
        self.closebtn.setGeometry(QtCore.QRect(170, 90, 98, 27))
        self.closebtn.setObjectName(_fromUtf8("closebtn"))

        self.retranslateUi(aboutwin)
        QtCore.QMetaObject.connectSlotsByName(aboutwin)

    def retranslateUi(self, aboutwin):
        aboutwin.setWindowTitle(QtGui.QApplication.translate("aboutwin", "About Bytestat", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("aboutwin", "<html><head/><body><p>Bytestat<br/>version: 1.0<br/>author: Erik Lotin, erik@lotin.pro<br/>created: 10.2012</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.closebtn.setText(QtGui.QApplication.translate("aboutwin", "Close", None, QtGui.QApplication.UnicodeUTF8))

