import sys

from PyQt4 import QtCore, QtGui

from file_with_ui import Ui_MainWindow

class Main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

    def browse(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        fname = open(filename)
        data = fname.read()
        self.textEdit.setText(data)
        fname.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())