from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.setEnabled(True)
        mainWindow.resize(640, 460)
        mainWindow.setMinimumSize(QtCore.QSize(640, 460))
        mainWindow.setMaximumSize(QtCore.QSize(800, 641))
        self.mainWidget = QtGui.QWidget(mainWindow)
        self.mainWidget.setEnabled(True)
        self.mainWidget.setMinimumSize(QtCore.QSize(800, 600))
        self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
        self.buttonWidget = QtGui.QWidget(self.mainWidget)
        self.buttonWidget.setGeometry(QtCore.QRect(-1, 0, 641, 61))
        self.buttonWidget.setObjectName(_fromUtf8("buttonWidget"))
        self.uploadButton = QtGui.QPushButton(self.buttonWidget)
        self.uploadButton.setGeometry(QtCore.QRect(550, -1, 91, 61))
        self.uploadButton.setMouseTracking(False)
        self.uploadButton.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("old-go-top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadButton.setIcon(icon)
        self.uploadButton.setIconSize(QtCore.QSize(32, 32))
        self.uploadButton.setObjectName(_fromUtf8("uploadButton"))
        self.uploadButton.clicked.connect(self.browse)
        self.stopButton = QtGui.QPushButton(self.buttonWidget)
        self.stopButton.setGeometry(QtCore.QRect(460, -1, 91, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setIconSize(QtCore.QSize(32, 32))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.stopButton.clicked.connect(self.browse)
        self.dirButton = QtGui.QPushButton(self.buttonWidget)
        self.dirButton.setGeometry(QtCore.QRect(0, 0, 91, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("_ajusted_glass_folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dirButton.setIcon(icon2)
        self.dirButton.setIconSize(QtCore.QSize(32, 32))
        self.dirButton.setObjectName(_fromUtf8("dirButton"))
        self.dirButton.clicked.connect(self.browse)
        self.doneFrame = QtGui.QFrame(self.mainWidget)
        self.doneFrame.setGeometry(QtCore.QRect(0, 300, 461, 141))
        self.doneFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.doneFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.doneFrame.setObjectName(_fromUtf8("doneFrame"))
        self.doneBox = Qsci.QsciScintilla(self.doneFrame)
        self.doneBox.setGeometry(QtCore.QRect(-16, 0, 475, 140))
        self.doneBox.setToolTip(_fromUtf8(""))
        self.doneBox.setWhatsThis(_fromUtf8(""))
        self.doneBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.doneBox.setObjectName(_fromUtf8("doneBox"))
        self.progressBar = QtGui.QProgressBar(self.mainWidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 440, 641, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.queueFrame = QtGui.QFrame(self.mainWidget)
        self.queueFrame.setGeometry(QtCore.QRect(459, 59, 181, 381))
        self.queueFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.queueFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.queueFrame.setObjectName(_fromUtf8("queueFrame"))
        self.queueBox = Qsci.QsciScintilla(self.queueFrame)
        self.queueBox.setGeometry(QtCore.QRect(-16, 0, 197, 381))
        self.queueBox.setToolTip(_fromUtf8(""))
        self.queueBox.setWhatsThis(_fromUtf8(""))
        self.queueBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.queueBox.setObjectName(_fromUtf8("queueBox"))
        mainWindow.setCentralWidget(self.mainWidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


    def browse(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        fname = open(filename)
        data = fname.read()
        self.textEdit.setText(data)
        fname.close()


    
    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtGui.QApplication.translate("mainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadButton.setText(QtGui.QApplication.translate("mainWindow", " Upload\n"
" Photos", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("mainWindow", "    Stop\n"
" Upload", None, QtGui.QApplication.UnicodeUTF8))
        self.dirButton.setText(QtGui.QApplication.translate("mainWindow", "Choose \n"
"Directory", None, QtGui.QApplication.UnicodeUTF8))





from PyQt4 import Qsci

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())