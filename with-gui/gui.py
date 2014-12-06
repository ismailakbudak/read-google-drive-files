# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Nov 28 01:22:09 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
# Developer
# Ismail AKBUDAK
# ismailakbudak.com


#/**************  Added for drive api *******************/
import json, os, sys, httplib2, oauth2client.client
from apiclient.http import MediaFileUpload  
from apiclient.discovery import build
from config import *
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

# Application UI
class Ui_MainWindow(object):
    #/**************  Added for drive api gloabal variable *******************/
    flow = ''
    http = httplib2.Http()
    drive_service = None
    credentials = None
    service_status = False
    #/************** End of drive api gloabal variable *******************/
    def setupUi(self, MainWindow): 
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Google drive services from Ismail AKBUDAK", None))
        # Tabs initialized
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 540))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        # Tab main initialized
        self.tabMain = QtGui.QWidget()
        self.tabMain.setObjectName(_fromUtf8("tabMain"))
        # Tab settings initialized
        self.tabSettings = QtGui.QWidget()
        self.tabSettings.setObjectName(_fromUtf8("tabSettings")) 
        # Settings - information label 
        self.labelInfo = QtGui.QLabel(self.tabSettings)
        self.labelInfo.setGeometry(QtCore.QRect(50, 10, 100, 20))
        self.labelInfo.setObjectName(_fromUtf8("labelInfo"))
        self.labelInfo.setText( "Verification code: ") 
        # Settings - label status 
        self.labelStatusSettings = QtGui.QLabel(self.tabSettings)
        self.labelStatusSettings.setGeometry(QtCore.QRect(50, 80, 430, 20))
        self.labelStatusSettings.setObjectName(_fromUtf8("labelStatusSettings"))  
        self.labelStatusSettings.setText(_translate("MainWindow", "Program status will be here", None))  
         # Settings - edit line for verification code
        self.lineCode = QtGui.QLineEdit(self.tabSettings)
        self.lineCode.setGeometry(QtCore.QRect(160, 8, 350, 25))
        self.lineCode.setObjectName(_fromUtf8("lineCode"))
        # Settings - get authorize button 
        self.pushButtonConfig = QtGui.QPushButton(self.tabSettings)
        self.pushButtonConfig.setGeometry(QtCore.QRect(50, 40, 130, 30))
        self.pushButtonConfig.setObjectName(_fromUtf8("pushButtonConfig")) 
        self.pushButtonConfig.clicked.connect(self.settings)
        self.pushButtonConfig.setText(_translate("MainWindow", "Get Authorize Code", None))
        # Settings - set authorize file button 
        self.pushButtonConfigSet = QtGui.QPushButton(self.tabSettings)
        self.pushButtonConfigSet.setGeometry(QtCore.QRect(180, 40, 130, 30))
        self.pushButtonConfigSet.setObjectName(_fromUtf8("pushButtonConfigSet")) 
        self.pushButtonConfigSet.clicked.connect(self.configSet)
        self.pushButtonConfigSet.setText(_translate("MainWindow", "Set Config File", None))
        # Tab upload file initialized
        self.tabUpload = QtGui.QWidget()
        self.tabUpload.setObjectName(_fromUtf8("tabUpload"))
        # Upload - label uploaded file
        self.labelInfoFile = QtGui.QLabel(self.tabUpload)
        self.labelInfoFile.setGeometry(QtCore.QRect(50, 10, 100, 20))
        self.labelInfoFile.setObjectName(_fromUtf8("labelInfoFile"))
        self.labelInfoFile.setText("Path : ")  
         # Upload - label for open files information
        self.labelFile = QtGui.QLabel(self.tabUpload)
        self.labelFile.setGeometry(QtCore.QRect(90, 10, 250, 20))
        self.labelFile.setObjectName(_fromUtf8("labelFile"))
        self.labelFile.setText( 'File path will be here..' )
        # Upload - label status 
        self.labelStatusUpload = QtGui.QLabel(self.tabUpload)
        self.labelStatusUpload.setGeometry(QtCore.QRect(50, 80, 430, 20))
        self.labelStatusUpload.setObjectName(_fromUtf8("labelStatusUpload"))  
        self.labelStatusUpload.setText(_translate("MainWindow", "Program status will be here", None)) 
        # Upload - choose file button 
        self.pushButtonChoose = QtGui.QPushButton(self.tabUpload)
        self.pushButtonChoose.setGeometry(QtCore.QRect(50, 40, 110, 30))
        self.pushButtonChoose.setObjectName(_fromUtf8("pushButtonChoose"))
        self.pushButtonChoose.clicked.connect(self.openFile)
        self.pushButtonChoose.setText(_translate("MainWindow", "Choose File", None))
        # Upload - upload file button 
        self.pushButtonUpload = QtGui.QPushButton(self.tabUpload)
        self.pushButtonUpload.setGeometry(QtCore.QRect(170, 40, 110, 30))
        self.pushButtonUpload.setObjectName(_fromUtf8("pushButtonUpload"))
        self.pushButtonUpload.clicked.connect(self.upload)
        self.pushButtonUpload.setText(_translate("MainWindow", "Upload File", None))
        # Upload - share button
        self.checkBoxShare = QtGui.QCheckBox(self.tabUpload)
        self.checkBoxShare.setGeometry(QtCore.QRect(300, 45, 89, 21))
        self.checkBoxShare.setObjectName(_fromUtf8("checkBoxShare"))
        self.checkBoxShare.setText("Share")
        self.checkBoxShare.setChecked(True) 
        # Tab read file initialized
        self.tabRead = QtGui.QWidget()
        self.tabRead.setObjectName(_fromUtf8("tabRead"))        
        # Read - read files button
        self.pushButtonRead = QtGui.QPushButton(self.tabRead)
        self.pushButtonRead.setGeometry(QtCore.QRect(50, 30, 110, 30))
        self.pushButtonRead.setObjectName(_fromUtf8("pushButtonRead"))
        self.pushButtonRead.clicked.connect(self.read)
        self.pushButtonRead.setText(_translate("MainWindow", "Read Files", None))
        # Read - label status 
        self.labelStatusRead = QtGui.QLabel(self.tabRead)
        self.labelStatusRead.setGeometry(QtCore.QRect(50, 80, 430, 20))
        self.labelStatusRead.setObjectName(_fromUtf8("labelStatusRead"))  
        self.labelStatusRead.setText(_translate("MainWindow", "Program status will be here", None)) 
        # Read - table  views  
        self.tableWidget = QtGui.QTableWidget(self.tabRead)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 762, 350)) # X - Y - width - height 
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,60)
        self.tableWidget.setColumnWidth(2,60)
        self.tableWidget.setColumnWidth(3,440)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        # Table view Header
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size (kb)", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Shared", None)) 
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Download", None)) 
        # Main window
        # Because of dialog exception 
        # MainWindow.setCentralWidget(self.centralwidget)  
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.addTab(self.tabMain, _fromUtf8(""))
        self.tabWidget.addTab(self.tabSettings, _fromUtf8(""))
        self.tabWidget.addTab(self.tabRead, _fromUtf8(""))
        self.tabWidget.addTab(self.tabUpload, _fromUtf8(""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), _translate("MainWindow", "Main Menu", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", "Settings ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRead), _translate("MainWindow", "Read File", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabUpload), _translate("MainWindow", "Upload File ", None))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.initialize()
    
    # Conf.json - initialize check
    def get_authorize_check(self):
        if self.service_status == False:
            self.labelStatusSettings.setText("You should authorize your account before the process..") 
            self.tabWidget.setCurrentIndex(1)
            return
         
    # Load credentials from conf.json
    def initialize(self):
        try:
            self.credentials =  oauth2client.client.Credentials.new_from_json(open('conf.json','r').read())
            self.http = self.credentials.authorize(self.http)
            self.drive_service = build('drive', 'v2', http=self.http)
            self.service_status = True
        except Exception, error:
            print 'An error occurred: %s' % error
            self.drive_service = None
            self.credentials = None
            self.labelStatusSettings.setText("You should authorize your account..") 
            self.tabWidget.setCurrentIndex(1)
            self.service_status = False

    # Common Part -  Set table items
    def setTableData(self, datas):
        row = 0
        self.tableWidget.setRowCount(datas.__len__())
        for data in datas: 
            item = QtGui.QTableWidgetItem()
            item.setText(  data['title'] )
            self.tableWidget.setItem(row, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText( data['quotaBytesUsed']  )
            self.tableWidget.setItem(row, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText( str(data['shared'])  )
            self.tableWidget.setItem(row, 2, item)
            item = QtGui.QTableWidgetItem()
            item.setText( data['webContentLink'] )
            self.tableWidget.setItem(row, 3, item)
            row = row + 1

    # Read - read cloud files        
    def read(self):
        self.get_authorize_check()
        try:
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
                    val = response
                    datas.append(val)
            self.labelStatusRead.setText( 'List of all files from drive..') 
            self.setTableData(datas)   
        except Exception, error:
            print 'An error occurred: %s' % error
            self.labelStatusRead.setText( 'The files could not listed..')  
     
    # Upload - upload file to cloud
    def upload(self):  
        self.get_authorize_check() 
        # Path to the file to upload
        FILENAME = self.labelFile.text() #'text.txt'
        FILENAME = str(FILENAME).strip()          
        if len( FILENAME ) > 0 and os.path.isfile(FILENAME) : 
            #self.labelFile.setText(_translate("MainWindow", filename, None))
            try:
                media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
                doc_names = FILENAME.split('/');
                doc_name = doc_names[len(doc_names)-1]
                body = {
                  'title': doc_name,
                  'description': 'A test document',
                  'mimeType': 'text/plain'   }
                response = self.drive_service.files().insert(body=body, media_body=media_body).execute()
                json.dumps(response, sort_keys=True, indent=4)
                 
                if self.checkBoxShare.isChecked():
                   if self.insert_permission( response['id']) :
                      status = 'The file uploaded and shared successfully..'
                      #response['shared'] = True # Change the local variable data
                   else :
                      status = 'The file uploaded successfully.. But could not shared..'
                else :
                    status = 'The file uploaded successfully but not shared..'    
                self.read()
                self.labelStatusRead.setText(status) 
                self.labelStatusUpload.setText(status) 
                #val = response       
                #self.setTableData([val])
                self.tabWidget.setCurrentIndex(2)  
            except Exception, e:
                print 'An error occurred: %s' % e
                self.labelStatusUpload.setText("The file could not uploaded...")  
        else:
            self.labelFile.setText( 'The file path will be here..' )
            self.labelStatusUpload.setText("Please choose file...")
        return  
    
    # Settings - get authorize url
    def settings(self):
        global flow  
        OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
        REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
        flow = oauth2client.client.OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
        authorize_url = flow.step1_get_authorize_url()
        #print ("\nGo to the permission link : \n"  + authorize_url )
        self.labelStatusSettings.setText('<html> <a style = \'text-decoration:none\' href =\''+authorize_url+'\'>Go to Authorize Url</a></html>')
    
    # Settings  - set settings    
    def configSet(self):
        global flow   
        #code = raw_input('\nVerification code: ').strip()
        try:
            code =  self.lineCode.text()
            code =  str(code).strip() 
            if len(code) > 10:  
                credentials = flow.step2_exchange(code)
                open('conf.json','w').write(credentials.to_json())
                self.labelStatusSettings.setText("Configuration has been set successfully..")
                self.lineCode.setText('')
                self.initialize()
            else:
                self.labelStatusSettings.setText("Code field must be bigger than 10 characters..")                  
        except Exception, error:
            print 'An error occurred: %s' % error
            self.labelStatusSettings.setText("There is something wrong..")
    
    # Upload - open file dialog
    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'),"")
        filename = str(filename).strip()
        if len( filename) > 0 and os.path.isfile(filename)   : 
            self.labelFile.setText(_translate("MainWindow", filename, None))
            self.labelStatusUpload.setText("File choosed successfully..")
        else:
            self.labelFile.setText( 'File path will be here..' )
            self.labelStatusUpload.setText("Please choose file...")

    def insert_permission(self, file_id ):
      """Insert a new permission.
      Args:
        service: Drive API service instance.
        file_id: ID of the file to insert permission for.
        value: User or group e-mail address, domain name or None for 'default'
               type.
        perm_type: The value 'user', 'group', 'domain' or 'default'.
        role: The value 'owner', 'writer' or 'reader'.
      Returns:
        The inserted permission if successful, None otherwise.
      """
      self.get_authorize_check() 
      value = 'anyone'
      perm_type = 'anyone'
      role = 'writer'
      new_permission = {
          'value': value,
          'type': perm_type,
          'role': role
      }
      try:
        self.drive_service.permissions().insert(
            fileId=file_id, body=new_permission).execute()
        return True
      except errors.HttpError, error:
        print 'An error occurred: %s' % error
      return False

    def update_file(self, file_id ):
      """Update an existing file's metadata and content.
      Args:
        service: Drive API service instance.
        file_id: ID of the file to update.
        new_title: New title for the file.
        new_description: New description for the file.
        new_mime_type: New MIME type for the file.
        new_filename: Filename of the new content to upload.
        new_revision: Whether or not to create a new revision for this file.
      Returns:
        Updated file metadata if successful, None otherwise.
      """
      self.get_authorize_check() 
      try:
        # First retrieve the file from the API.
        file = service.files().get(fileId=file_id).execute()
        new_filename = 'ok2.txt'
        description = 'test deneme2'
        new_mime_type = 'text/plain'
        # File's new metadata.
        file['title'] = new_filename
        file['description'] = description
        file['mimeType'] = new_mime_type 
        # Send the request to the API.
        updated_file = service.files().update(
            fileId=file_id,
            body=file ).execute()
        return updated_file
      except errors.HttpError, error:
        print 'An error occurred: %s' % error
        return None    
         
class Win(QtGui.QDialog,Ui_MainWindow):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

# Main application
if __name__ == "__main__":
    import sys 
    app = QtGui.QApplication(sys.argv)
    MWindow = Win()
    MWindow.show()
    sys.exit(app.exec_())
