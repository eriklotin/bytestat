# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qt_designer/gui_result.ui'
#
# Created: Thu Oct 17 00:55:31 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_resultwin(object):
    def setupUi(self, resultwin):
        resultwin.setObjectName(_fromUtf8("resultwin"))
        resultwin.resize(271, 370)
        resultwin.setMinimumSize(QtCore.QSize(270, 370))
        self.btn_res_save = QtGui.QPushButton(resultwin)
        self.btn_res_save.setGeometry(QtCore.QRect(10, 10, 141, 27))
        self.btn_res_save.setObjectName(_fromUtf8("btn_res_save"))
        self.btn_reswin_close = QtGui.QPushButton(resultwin)
        self.btn_reswin_close.setGeometry(QtCore.QRect(160, 10, 101, 27))
        self.btn_reswin_close.setObjectName(_fromUtf8("btn_reswin_close"))
        self.txtarea_result = QtGui.QTextEdit(resultwin)
        self.txtarea_result.setGeometry(QtCore.QRect(10, 50, 251, 311))
        self.txtarea_result.setReadOnly(True)
        self.txtarea_result.setObjectName(_fromUtf8("txtarea_result"))

        self.retranslateUi(resultwin)
        QtCore.QMetaObject.connectSlotsByName(resultwin)

    def retranslateUi(self, resultwin):
        resultwin.setWindowTitle(QtGui.QApplication.translate("resultwin", "Analysis result", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_res_save.setText(QtGui.QApplication.translate("resultwin", "Save to file", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reswin_close.setText(QtGui.QApplication.translate("resultwin", "Close", None, QtGui.QApplication.UnicodeUTF8))

