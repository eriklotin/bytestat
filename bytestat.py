# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, './gui')
from PyQt4 import QtGui, QtCore
from gui_main import Ui_MainWindow
from gui_about import Ui_aboutwin
from gui_result import Ui_resultwin
from gui_alert import Ui_alertwin
import BSlib

class BytestatMainWindow(QtGui.QMainWindow):
	
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.connect(self.ui.action_Open, QtCore.SIGNAL("triggered()"), self.selectFileDialog)
		self.connect(self.ui.actionExit, QtCore.SIGNAL("triggered()"), QtCore.SLOT('close()'))
		self.connect(self.ui.actionAbout_Bytestat, QtCore.SIGNAL("triggered()"), self.drawAboutWindow)
		
		self.connect(self.ui.btn_analize, QtCore.SIGNAL("clicked()"), self.startAnalize)

	def drawAboutWindow(self):
		self.aboutWindow = QtGui.QDialog(self)
		self.aboutWindow.ui = Ui_aboutwin()
		self.aboutWindow.ui.setupUi(self.aboutWindow)
		self.aboutWindow.connect(self.aboutWindow.ui.closebtn, QtCore.SIGNAL("clicked()"), self.closeAboutWindow)
		self.aboutWindow.show()
		
	def closeAboutWindow(self):
		self.aboutWindow.close()
		
	def selectFileDialog(self):
		filename = unicode(QtGui.QFileDialog.getOpenFileName(self, u'File for analysis', ''))
		self.ui.inp_filefullpath.setText(filename);
		
	def saveOutput(self, text):
		filepath = QtGui.QFileDialog.getSaveFileName(self, u'Save result', '')
		try:
			fp = open(unicode(filepath), 'w') 
		except:
			return self.bytestatAlert(u'Write error')
		fp.write(text)	
		return self.bytestatAlert(u'File was successfully saved')
			
	def startAnalize(self):
		resultText = unicode(self.ui.inp_filefullpath.text())
		analizeStatus, analizeOutput = BSlib.analizeFile(resultText)
		if analizeStatus == False:
			self.bytestatAlert(analizeOutput);
		else:
			self.drawResultWindow(analizeOutput)
		
	def drawResultWindow(self, resultText):
		self.resultWindow = QtGui.QDialog(self)
		self.resultWindow.ui = Ui_resultwin()
		self.resultWindow.ui.setupUi(self.resultWindow)
		
		self.resultWindow.ui.txtarea_result.setText(resultText)
		
		self.resultWindow.connect(self.resultWindow.ui.btn_reswin_close, QtCore.SIGNAL("clicked()"), self.resultWindow.close)
		self.resultWindow.connect(self.resultWindow.ui.btn_res_save, QtCore.SIGNAL("clicked()"), lambda: self.saveOutput(resultText))
	
		self.resultWindow.show()
		
	def bytestatAlert(self, outputText=""):
		self.alertWindow = QtGui.QDialog(self)
		self.alertWindow.ui = Ui_alertwin()
		self.alertWindow.ui.setupUi(self.alertWindow)
		
		self.alertWindow.ui.alertText.setText(outputText)
		self.alertWindow.connect(self.alertWindow.ui.btn_alertOk, QtCore.SIGNAL("clicked()"), self.alertWindow.close)
		
		self.alertWindow.show()
		
app = QtGui.QApplication(sys.argv)
main = BytestatMainWindow()
main.show()

sys.exit(app.exec_())