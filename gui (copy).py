# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Nov 28 01:22:09 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

 
#/**************  Added for drive api *******************/
import json   
from apiclient.http import MediaFileUpload
import httplib2  
from apiclient.discovery import build
import oauth2client.client
#/************** End of drive api   *******************/


from PyQt4 import QtCore, QtGui

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

    
    #/**************  Added for drive api *******************/
    credentials =  oauth2client.client.Credentials.new_from_json(open('conf.json','r').read())
    http = httplib2.Http()
    http = credentials.authorize(http)
    drive_service = build('drive', 'v2', http=http)
    #/************** End of drive api   *******************/

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(550, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.pushButtonUpload = QtGui.QPushButton(self.centralwidget)
        self.pushButtonUpload.setGeometry(QtCore.QRect(140, 40, 89, 27))
        self.pushButtonUpload.setObjectName(_fromUtf8("pushButtonUpload"))
        self.pushButtonUpload.clicked.connect(self.upload)

        self.pushButtonRead = QtGui.QPushButton(self.centralwidget)
        self.pushButtonRead.setGeometry(QtCore.QRect(260, 40, 89, 27))
        self.pushButtonRead.setObjectName(_fromUtf8("pushButtonRead"))
        self.pushButtonRead.clicked.connect(self.read)

        self.listViewFiles = QtGui.QListView(self.centralwidget)
        self.listViewFiles.setGeometry(QtCore.QRect(50, 120, 431, 70)) # X - X - width - height
        self.listViewFiles.setObjectName(_fromUtf8("listViewFiles"))
        #self.setContent()
        
        # Label
        self.labelStatus = QtGui.QLabel(self.centralwidget)
        self.labelStatus.setGeometry(QtCore.QRect(50, 80, 431, 21))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))    
        
        # Table  
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 200, 431, 151))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        

        # Link label
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 410, 58, 15)) 
        self.label.setObjectName(_fromUtf8("label"))

        MainWindow.setCentralWidget(self.centralwidget)  
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButtonUpload.setText(_translate("MainWindow", "Upload ", None))
        self.pushButtonRead.setText(_translate("MainWindow", "Read Files", None))
        self.labelStatus.setText(_translate("MainWindow", "Program status will be here", None))
        
        # Table view
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Download", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        #self.setTable()
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        # Link label
        self.label.setText(_translate("MainWindow", "<html> <a style = \'text-decoration:none\' href =\'www.google.com\'>Sign In</a></html>", None))
    
    #setTable
    def setTable(self):
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)

        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "ok", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "test", None))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "ok", None))

    # Prepare content for list view
    def setContent(self):
        model = QtGui.QStandardItemModel(self.listViewFiles)
        foods = [
            'Cookie dough', # Must be store-bought
            'Hummus', # Must be homemade
            'Spaghetti', # Must be saucy
            'Dal makhani', # Must be spicy
            'Chocolate whipped cream' # Must be plentiful
        ]
        for food in foods:
            # Create an item with a caption
            item = QtGui.QStandardItem(food)
         
            # Add a checkbox to it
            item.setCheckable(True)
         
            # Add the item to the model
            model.appendRow(item)
        self.listViewFiles.setModel(model)

    def setListContent(self, datas):
        model = QtGui.QStandardItemModel(self.listViewFiles)
        for data in datas: 
            item = QtGui.QStandardItem(data) 
            model.appendRow(item)
        self.listViewFiles.setModel(model)

    #setTable
    def setTableData(self, datas):
        row = 0
        self.tableWidget.setRowCount(datas.__len__())
        for data in datas: 
            item = QtGui.QTableWidgetItem()
            item.setText( "ok" )
            self.tableWidget.setItem(row, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText( "test" )
            self.tableWidget.setItem(row, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText( "ok3" )
            self.tableWidget.setItem(row, 2, item)
            row = row + 1
            

    def read(self):
        # Get all files from drive service
        result = []
        page_token = None
        while True:
          param = {}
          if page_token:
            param['pageToken'] = page_token
          files = self.drive_service.files().list(**param).execute()
          result.extend(files['items'])
          page_token = files.get('nextPageToken')
          if not page_token:
            break
        datas = []    
        for response in result:
            json.dumps(response, sort_keys=True, indent=4)
            if int(response['quotaBytesUsed']) > 0 :
                val = []
                val.append( response['title'])
                val.append( response['quotaBytesUsed'])
                val.append( response['webContentLink'])
                datas.append(val)

        self.labelStatus.setText( 'List of files ')
        #self.setListContent( datas)
        self.setTableData(datas)   

    def upload(self):
        # Path to the file to upload
        FILENAME = 'text.txt'
        # Insert a file
        media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
        body = {
          'title': 'My google-python document',
          'description': 'A test document',
          'mimeType': 'text/plain'
        }
        response = self.drive_service.files().insert(body=body, media_body=media_body).execute()
        json.dumps(response, sort_keys=True, indent=4)
        val = [ response['title'],  
                response['quotaBytesUsed'],
                response['webContentLink'] 
              ]        
        self.labelStatus.setText('File uploaded successfully..')
        #self.setListContent( datas)
        self.setTableData([val])   
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
