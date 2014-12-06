# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Thu Dec  4 23:15:38 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(552, 538)  
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

  
        self.progressbar = QtGui.QProgressBar( self.centralwidget)
        self.progressbar.setMinimum(1)
        self.progressbar.setMaximum(101)
        self.progressbar.setGeometry(QtCore.QRect(110, 0, 200, 21))

        self.button = QtGui.QPushButton(self.centralwidget)
        self.button.clicked.connect(self.handleButton) 
        self.button.setGeometry(QtCore.QRect(0, 80, 100, 21))
        self.button.setText("Start")   
        self._active = False

        MainWindow.setCentralWidget(self.centralwidget)

    def handleButton(self):
        if not self._active:
            self._active = True
            self.button.setText('Stop')
            if self.progressbar.value() == self.progressbar.maximum():
                self.progressbar.reset()
            QtCore.QTimer.singleShot(0, self.startLoop)
        else:
            self._active = False

    def closeEvent(self, event):
        self._active = False

    def startLoop(self):
        while True:
            time.sleep(0.05)
            value = self.progressbar.value() + 1
            self.progressbar.setValue(value)
            QtGui.qApp.processEvents()
            if (not self._active or
                value >= self.progressbar.maximum()):
                break
        self.button.setText('Start')
        self._active = False
 

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None)) 


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
