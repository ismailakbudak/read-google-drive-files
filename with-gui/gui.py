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
import json, os, sys #, httplib2, oauth2client.client
#from apiclient.http import MediaFileUpload  
#from apiclient.discovery import build
#from config import *
from Status import Status
from gui_helper import *
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
class Ui_MainWindow(helper):
    
    #/**************  Added for drive api gloabal variable *******************/
    #flow = ''
    #http = httplib2.Http()
    #drive_service = None
    #credentials = None
    #service_status = False
    #/************** End of drive api gloabal variable *******************/
    #,nymphdataGui,managerNymphData
    def __init__(self,nymphdataGui,managerNymphData):
        super(Ui_MainWindow,self).__init__(nymphdataGui,managerNymphData)
     
    def listen_url_Handler(self,data):
        if self.check_manager_error():
            try:
                self.tabWidget.setCurrentIndex(0)
                # data["result"]['0-1-2'] nyphdata
                # data["result"]['3'] content url
                # data["result"]['4'] content title
                self.labelStatusMain.setText( "There is file for you and it is already downloaded.." )
                message = data["result"]['4'] + " : " + data["result"]['3']
                nymphdata_sender=nymphdata(data["result"]['0'], data["result"]['1'], int(data["result"]['2']) )
                self.add_new_message( nymphdata_sender , message ,'url' ) 
            except Exception, error:
                 self.log('An error occurred: %s' % error)
        self.log_data(data)
    
    def listen_message_Handler(self,data):
        if self.check_manager_error():
            try:
                self.tabWidget.setCurrentIndex(0) 
                # data["result"]['0-1-2'] nyphdata
                # data["result"]['3'] content message 
                self.labelStatusMain.setText("There is message for you." )
                nymphdata_sender=nymphdata(data["result"]['0'], data["result"]['1'], int(data["result"]['2']) )        
                message =  data["result"]['3']   
                self.add_new_message( nymphdata_sender , message  ) 
            except Exception, error:
                 self.log('An error occurred: %s' % error)
        self.log_data(data)
    
    def read_Handler(self,data):
        if self.check_manager_error():
            if data==None:
                self.labelStatusRead.setText('There is an error!')
            else:
                self.labelStatusRead.setText( 'List of all files from drive..') 
                self.setTableData(data["result"]) 
        self.log_data(data)
    
    def upload_Handler(self,data):
        if self.check_manager_error():
            if data==None:
                self.labelStatusSettings.setText('There is an error!')
            else:
                try:
                    status = Status.getStatusText(data['result'][0])
                    #self.readg()
                    self.labelStatusRead.setText(status) 
                    self.labelStatusUpload.setText(status)
                    #self.tabWidget.setCurrentIndex(2)  
                    print(data)
                    nymphdata_receiver=None
                    if self.checkBoxShare.isChecked():
                        if self.checkBoxNodeInfo.isChecked():
                            NAME=self.lineEditNameUpload.text()   
                            HOST=self.lineEditIPUpload.text()   
                            PORT=self.lineEditPortUpload.text()
                            NAME=str(NAME)
                            HOST=str(HOST)
                            PORT=int(str(PORT))
                            nymphdata_receiver=nymphdata(NAME,HOST,PORT)    
                        else:    
                            id = self.comboBoxNodesUpload.currentIndex()
                            if id < len(nodes):
                                try:
                                    nymphdata_receiver= nodes[id]
                                except Exception, error:
                                    self.log('There is no nymph data coming from nodes. An error occurred: %s' % error)
                    if nymphdata_receiver:
                        self.talk(nymphdata_receiver, data['result'][1][3] ,'url', data['result'][1][0])
                        self.log("url is sended")
                except Exception, error:
                    self.log('An error occurred: %s' % error)            
        self.log_data(data)        
                 
    def init_Handler(self,data):
        if self.check_manager_error():
            self.tabWidget.setCurrentIndex(0) 
            self.labelStatusMain.setText("Your configuration is initialized..")
        self.log_data(data)

    def get_authorize_url_Handler(self,data):
        if self.check_manager_error():
            if data==None:
                self.labelStatusSettings.setText('There is an error!')
            else:
                authorize_url=data['result'] 
                self.labelStatusSettings.setText(authorize_url)
        self.log_data(data)
                
    def set_credentials_Handler(self,data):
        if self.check_manager_error():
            if data==None:
                self.labelStatusSettings.setText('There is an error!')
            else:        
                if data['result']==True:
                    self.labelStatusSettings.setText("Configuration has been set successfully..")
                else:
                    self.labelStatusSettings.setText("Configuration could not be set..")
        self.log("credentials handler finished")   

    def download_Handler(self,data):
        if self.check_manager_error():
            self.tabWidget.setCurrentIndex(0) 
            self.labelStatusMain.setText("File has been downloaded successfully..")
        self.log_data(data)
        
    def error_Manager_Handler(self,data):
        if self.check_manager_error():
            try:
                if data['result'][1]=="offline_node":
                    self.tabWidget.setCurrentIndex(0)
                    self.labelStatusMain.setText("There is an error..")
                    self.add_new_message(self.managerNymphData,"Sory!! There is an error... Error: %s" % "The user is not online..." )
            except Exception, error:
                 self.log('An error occurred: %s' % error)
        self.log(data)

    def fill_fields(self):
        self.fill_combobox()
        self.set_edit_line()
        self.talkWith(self.managerNymphData)
        if self.error!=None:
            self.tabWidget.setCurrentIndex(1)
            self.labelStatusSettings.setText( "Error : " + self.error + " -- Your manager is not working now.. Try connect manager.." )
        else:
            self.labelStatusSettings.setText( "You have been connected your manager.." ) 
   
    def fill_combobox(self):
        #self.comboBoxNodesUpload.insertItem (self, int index, QString text, QVariant userData = QVariant())
        #self.comboBoxNodesUpload.currentIndex()
        #self.comboBoxNodesUpload.currentText()
        #index = comobox.findData(lineedit.text())
        #combobox.setCurrentIndex(index)
        for key in nodes:
            self.comboBoxNodes.addItem( nodes[key].NAME, key )
            self.comboBoxNodesUpload.addItem( nodes[key].NAME, key ) 
    
    def add_new_message(self, nyphdata, content , type='message'  ):
        if type=='message':
            info =  "%s : %s " % ( nyphdata.NAME, content )
        else:
            info =  "%s : %s " % ( nyphdata.NAME, content )
        item = QtGui.QListWidgetItem()
        item.setText( info )
        self.listViewMessages.addItem(item)
     
    def set_edit_line(self):
        NAME=self.managerNymphData.NAME
        HOST=self.managerNymphData.HOST
        PORT=str(self.managerNymphData.PORT) 

        self.lineEditNameUpload.setText(NAME)
        self.lineEditIPUpload.setText(HOST)
        self.lineEditPortUpload.setText(PORT)
        self.lineEditName.setText(NAME)
        self.lineEditIP.setText(HOST)
        self.lineEditPort.setText(PORT)
        self.lineEditNameMain.setText(NAME)
        self.lineEditIPMain.setText(HOST)
        self.lineEditPortMain.setText(PORT)

    def setupUi(self, MainWindow): 
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Google drive services from Ismail AKBUDAK", None))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        font.setPointSize(11)
        fontBig = QtGui.QFont()
        fontBig.setPointSize(14)

        # Tabs initialized
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 540))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))        
        # Tab main initialized
        self.tabMain = QtGui.QWidget()
        self.tabMain.setObjectName(_fromUtf8("tabMain"))
        # Main - Send  button
        self.pushButtonSend = QtGui.QPushButton(self.tabMain)
        self.pushButtonSend.setGeometry(QtCore.QRect(30, 420, 211, 30))
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.pushButtonSend.setText(_translate("MainWindow", "Send", None))
        self.pushButtonSend.clicked.connect(self.send_message)
        # Main - List view messages
        self.listViewMessages = QtGui.QListWidget(self.tabMain)
        self.listViewMessages.setGeometry(QtCore.QRect(30, 60, 731, 231))
        self.listViewMessages.setEditTriggers(QtGui.QAbstractItemView.CurrentChanged|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.SelectedClicked)
        self.listViewMessages.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.listViewMessages.setObjectName(_fromUtf8("listViewMessages"))
        # Main - Message
        self.textEditMessage = QtGui.QLineEdit(self.tabMain)
        self.textEditMessage.setGeometry(QtCore.QRect(30, 350, 541, 30))
        self.textEditMessage.setObjectName(_fromUtf8("textEditMessage"))
        # Main - nypmhdata name
        self.labelNameMain = QtGui.QLabel(self.tabMain)
        self.labelNameMain.setGeometry(QtCore.QRect(580, 320, 58, 25))
        self.labelNameMain.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNameMain.setObjectName(_fromUtf8("labelNameMain"))
        self.labelNameMain.setText(_translate("MainWindow", "Name :", None))
        # Main -  nypmhdata port
        self.label_PortMain = QtGui.QLabel(self.tabMain)
        self.label_PortMain.setGeometry(QtCore.QRect(580, 380, 58, 25))
        self.label_PortMain.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_PortMain.setObjectName(_fromUtf8("label_PortMain"))
        self.label_PortMain.setText(_translate("MainWindow", "Port :", None))
        # Main -  nypmhdata IP
        self.label_IPMain = QtGui.QLabel(self.tabMain)
        self.label_IPMain.setGeometry(QtCore.QRect(580, 350, 58, 25))
        self.label_IPMain.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_IPMain.setObjectName(_fromUtf8("label_IPMain"))
        self.label_IPMain.setText(_translate("MainWindow", "IP :", None))
        # Main - edit line name
        self.lineEditNameMain = QtGui.QLineEdit(self.tabMain)
        self.lineEditNameMain.setGeometry(QtCore.QRect(650, 320, 113, 25))
        self.lineEditNameMain.setObjectName(_fromUtf8("lineEditNameMain")) 
        # Main - edit line ıp
        self.lineEditIPMain = QtGui.QLineEdit(self.tabMain)
        self.lineEditIPMain.setGeometry(QtCore.QRect(650, 350, 113, 25))
        self.lineEditIPMain.setObjectName(_fromUtf8("lineEditIPMain"))
        # Main - edit line port
        self.lineEditPortMain = QtGui.QLineEdit(self.tabMain)
        self.lineEditPortMain.setGeometry(QtCore.QRect(650, 380, 113, 25))
        self.lineEditPortMain.setObjectName(_fromUtf8("lineEditPortMain"))    
        # Main - nodes 
        self.comboBoxNodes = QtGui.QComboBox(self.tabMain)
        self.comboBoxNodes.setGeometry(QtCore.QRect(360, 420, 211, 30))
        self.comboBoxNodes.setObjectName(_fromUtf8("comboBoxNodes"))
        #self.comboBoxNodes.addItem(_fromUtf8("")) 
        # They getting from initialize
        #for node in key:
        #self.comboBoxNodes.addItem( key[node].NAME )
        #self.comboBoxNodes.setItemText(1, _translate("MainWindow", "as", None)) 
        # Main - label receiver
        self.labelNodes = QtGui.QLabel(self.tabMain)
        self.labelNodes.setGeometry(QtCore.QRect(250, 420, 91, 30))
        self.labelNodes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNodes.setObjectName(_fromUtf8("labelNodes"))
        self.labelNodes.setText(_translate("MainWindow", "Receiver  :", None))
        # Main - program status
        self.labelStatusMain = QtGui.QLabel(self.tabMain)
        self.labelStatusMain.setGeometry(QtCore.QRect(40, 460, 721, 30))
        self.labelStatusMain.setFont(font)
        self.labelStatusMain.setObjectName(_fromUtf8("labelStatusMain"))
        self.labelStatusMain.setText(_translate("MainWindow", "Program status....", None))

        # Main - messages label title
        self.labelTitleList = QtGui.QLabel(self.tabMain)
        self.labelTitleList.setGeometry(QtCore.QRect(30, 10, 731, 45))
        self.labelTitleList.setFont(fontBig)
        self.labelTitleList.setObjectName(_fromUtf8("labelTitleList"))
        self.labelTitleList.setText(_translate("MainWindow", "Messages from your firieds  :", None))
        # Main - message label title
        self.labelTitleList_2 = QtGui.QLabel(self.tabMain)
        self.labelTitleList_2.setGeometry(QtCore.QRect(30, 300, 511, 45))
        self.labelTitleList_2.setFont(fontBig)
        self.labelTitleList_2.setObjectName(_fromUtf8("labelTitleList_2"))
        self.labelTitleList_2.setText(_translate("MainWindow", "Your message :", None))

        # Tab settings initialized
        self.tabSettings = QtGui.QWidget()
        self.tabSettings.setObjectName(_fromUtf8("tabSettings")) 
        # Settings - information label 
        self.labelInfo = QtGui.QLabel(self.tabSettings)
        self.labelInfo.setGeometry(QtCore.QRect(50, 10, 100, 20))
        self.labelInfo.setObjectName(_fromUtf8("labelInfo"))
        self.labelInfo.setText( "Verification code: ") 
        # Settings - label status 
        self.labelStatusSettings = QtGui.QLineEdit(self.tabSettings)
        self.labelStatusSettings.setGeometry(QtCore.QRect(50, 80, 550, 25))
        self.labelStatusSettings.setObjectName(_fromUtf8("labelStatusSettings"))  
        self.labelStatusSettings.setText(_translate("MainWindow", "Program status will be here", None))  
         # Settings - edit line for verification code
        self.lineCode = QtGui.QLineEdit(self.tabSettings)
        self.lineCode.setGeometry(QtCore.QRect(160, 8, 550, 25))
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
        # Settings - button connect with manager
        self.pushButtonConnectManager = QtGui.QPushButton(self.tabSettings)
        self.pushButtonConnectManager.setGeometry(QtCore.QRect(180, 130, 200, 30))
        self.pushButtonConnectManager.setObjectName(_fromUtf8("pushButtonConnectManager"))
        self.pushButtonConnectManager.setText(_translate("MainWindow", "Connect to manager", None))
        self.pushButtonConnectManager.clicked.connect(self.connectManager)  
        # Settings - nypmhdata name
        self.labelName = QtGui.QLabel(self.tabSettings)
        self.labelName.setGeometry(QtCore.QRect(580, 320, 58, 25))
        self.labelName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.labelName.setText(_translate("MainWindow", "Name :", None))
        # Settings -  nypmhdata port
        self.label_Port = QtGui.QLabel(self.tabSettings)
        self.label_Port.setGeometry(QtCore.QRect(580, 380, 58, 25))
        self.label_Port.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Port.setObjectName(_fromUtf8("label_Port"))
        self.label_Port.setText(_translate("MainWindow", "Port :", None))
        # Settings -  nypmhdata IP
        self.label_IP = QtGui.QLabel(self.tabSettings)
        self.label_IP.setGeometry(QtCore.QRect(580, 350, 58, 25))
        self.label_IP.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_IP.setObjectName(_fromUtf8("label_IP"))
        self.label_IP.setText(_translate("MainWindow", "IP :", None))
        # Settings - edit line name
        self.lineEditName = QtGui.QLineEdit(self.tabSettings)
        self.lineEditName.setGeometry(QtCore.QRect(650, 320, 113, 25))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        # Settings - button add user
        self.pushButtonAddNode = QtGui.QPushButton(self.tabSettings)
        self.pushButtonAddNode.setGeometry(QtCore.QRect(620, 420, 141, 30))
        self.pushButtonAddNode.setObjectName(_fromUtf8("pushButtonAddNode"))
        self.pushButtonAddNode.setText(_translate("MainWindow", "Add New User", None))
        # Settings - edit line ıp
        self.lineEditIP = QtGui.QLineEdit(self.tabSettings)
        self.lineEditIP.setGeometry(QtCore.QRect(650, 350, 113, 25))
        self.lineEditIP.setObjectName(_fromUtf8("lineEditIP"))
        # Settings - edit line port
        self.lineEditPort = QtGui.QLineEdit(self.tabSettings)
        self.lineEditPort.setGeometry(QtCore.QRect(650, 380, 113, 25))
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))      


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
        self.pushButtonUpload.clicked.connect(self.uploadg)
        self.pushButtonUpload.setText(_translate("MainWindow", "Upload File", None))
        # Upload - share button
        self.checkBoxShare = QtGui.QCheckBox(self.tabUpload)
        self.checkBoxShare.setGeometry(QtCore.QRect(300, 45, 89, 21))
        self.checkBoxShare.setObjectName(_fromUtf8("checkBoxShare"))
        self.checkBoxShare.setText("Share with:")
        self.checkBoxShare.setChecked(True)
        #self.comboBoxNodes.addItem(_fromUtf8("")) 
        # They getting from initialize
        #for node in key:
        #self.comboBoxNodes.addItem( key[node].NAME )
        #self.comboBoxNodes.setItemText(1, _translate("MainWindow", "as", None))
        # Upload - nodes 
        self.comboBoxNodesUpload = QtGui.QComboBox(self.tabUpload)
        self.comboBoxNodesUpload.setGeometry(QtCore.QRect(440, 30, 200, 30)) 
        self.comboBoxNodesUpload.setObjectName(_fromUtf8("comboBoxNodesUpload")) 
        # Upload - or information
        self.labelNameUpload = QtGui.QLabel(self.tabUpload)
        self.labelNameUpload.setGeometry(QtCore.QRect(400, 70, 200, 25))
        self.labelNameUpload.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNameUpload.setObjectName(_fromUtf8("labelNameUpload"))
        self.labelNameUpload.setFont(fontBig)
        self.labelNameUpload.setText(_translate("MainWindow", "--------- OR ---------", None))
        # Upload - 
        self.labelNameUpload = QtGui.QLabel(self.tabUpload)
        self.labelNameUpload.setGeometry(QtCore.QRect(400, 110, 60, 25))
        self.labelNameUpload.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNameUpload.setObjectName(_fromUtf8("labelNameUpload"))
        self.labelNameUpload.setText(_translate("MainWindow", "Name :", None))
        # Upload - port
        self.label_PortUpload = QtGui.QLabel(self.tabUpload)
        self.label_PortUpload.setGeometry(QtCore.QRect(400, 140, 60, 25))
        self.label_PortUpload.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_PortUpload.setObjectName(_fromUtf8("label_PortUpload"))
        self.label_PortUpload.setText(_translate("MainWindow", "IP :", None))
        # Upload - 
        self.label_IPUpload = QtGui.QLabel(self.tabUpload)
        self.label_IPUpload.setGeometry(QtCore.QRect(400, 170, 60, 25))
        self.label_IPUpload.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_IPUpload.setObjectName(_fromUtf8("label_IPUpload"))
        self.label_IPUpload.setText(_translate("MainWindow", "Port :", None))
        # Upload -
        self.lineEditNameUpload = QtGui.QLineEdit(self.tabUpload)
        self.lineEditNameUpload.setGeometry(QtCore.QRect(480, 110, 140, 25))
        self.lineEditNameUpload.setObjectName(_fromUtf8("lineEditNameUpload")) 
        # Upload - 
        self.lineEditIPUpload = QtGui.QLineEdit(self.tabUpload)
        self.lineEditIPUpload.setGeometry(QtCore.QRect(480, 140, 140, 25))
        self.lineEditIPUpload.setObjectName(_fromUtf8("lineEditIPUpload"))
        # Upload - 
        self.lineEditPortUpload = QtGui.QLineEdit(self.tabUpload)
        self.lineEditPortUpload.setGeometry(QtCore.QRect(480, 170, 140, 25))
        self.lineEditPortUpload.setObjectName(_fromUtf8("lineEditPortUpload"))
        # Upload - 
        self.checkBoxNodeInfo = QtGui.QCheckBox(self.tabUpload)
        self.checkBoxNodeInfo.setGeometry(QtCore.QRect(440, 200, 170, 30))
        self.checkBoxNodeInfo.setObjectName(_fromUtf8("checkBoxNodeInfo"))
        self.checkBoxNodeInfo.setText(_translate("MainWindow", "Use this information", None))
        self.checkBoxNodeInfo.setChecked(False)

        # Tab read file initialized
        self.tabRead = QtGui.QWidget()
        self.tabRead.setObjectName(_fromUtf8("tabRead"))        
        # Read - read files button
        self.pushButtonRead = QtGui.QPushButton(self.tabRead)
        self.pushButtonRead.setGeometry(QtCore.QRect(50, 30, 110, 30))
        self.pushButtonRead.setObjectName(_fromUtf8("pushButtonRead"))
        self.pushButtonRead.clicked.connect(self.readg)
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
        
        # Tab main initialized
        self.tabNode = QtGui.QWidget()
        self.tabNode.setObjectName(_fromUtf8("tabNode"))

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

        # Fill with data
        self.fill_fields()
    
    def connectManager(self):
        self.error=None 
        self.talkWith(self.managerNymphData)
        if self.error!=None:
            self.labelStatusSettings.setText( "Error : " + self.error + " -- Sorry!! Your manager is not working now.." )
        else:
            self.labelStatusSettings.setText( "You have been connected your manager.." )
           
    # Common Part -  Set table items
    def setTableData(self, datas):
        row = 0
        self.tableWidget.setRowCount(datas.__len__())
        for data in datas: 
            item = QtGui.QTableWidgetItem()
            item.setText(  data[0] ) # title
            self.tableWidget.setItem(row, 0, item)
            item = QtGui.QTableWidgetItem()
            item.setText( data[1]  ) # quotaBytesUsed
            self.tableWidget.setItem(row, 1, item)
            item = QtGui.QTableWidgetItem()
            item.setText( str(data[2])  ) # shared
            self.tableWidget.setItem(row, 2, item)
            item = QtGui.QTableWidgetItem()
            item.setText( data[3] ) # webContentLink or downloadUrl
            self.tableWidget.setItem(row, 3, item)
            row = row + 1

    # Send message
    def send_message(self):
        if self.check_manager_error():
            message =  self.textEditMessage.text()
            message =  str(message).strip() 
            if len(message) > 3:
                nymphdata_receiver=None
                id = self.comboBoxNodes.currentIndex()
                if id < len(nodes):
                    try:
                        nymphdata_receiver= nodes[id]
                    except Exception, error:
                        self.log('There is no nymph data coming from nodes. An error occurred: %s' % error)
                if nymphdata_receiver:
                    self.talk( nymphdata_receiver, message ,'message') 
                    self.add_new_message( self.managerNymphData, message ) 
                    self.labelStatusMain.setText( "Your message has been sended.." )
                    self.textEditMessage.setText("")
                    self.log('message is sended')
            else:
                self.labelStatusMain.setText("Message field must be at least 4 characters..")
    
    # Read - read cloud files        
    def readg(self):
        if self.check_manager_error():
            self.read()
 
    # Upload - upload file to cloud
    def uploadg(self):
        if self.check_manager_error():
            filename = self.labelFile.text() #'text.txt'
            filename = str(filename).strip()
            if len( filename ) > 0 and os.path.isfile(filename) :
                #self.labelFile.setText(_translate("MainWindow", filename, None))
                is_share=0 
                if self.checkBoxShare.isChecked():
                    is_share=1  
                self.upload(filename, is_share)
            else:
                self.labelFile.setText( 'The file path will be here..' )
                self.labelStatusUpload.setText("Please choose file...")
                self.labelStatusUpload.setText("Please choose file...")
                 
    # Settings - get authorize url
    def settings(self):
        if self.check_manager_error():
            self.get_authorize_url()

    # Settings  - set settings    
    def configSet(self):
        if self.check_manager_error():
            code =  self.lineCode.text()
            code =  str(code).strip() 
            if len(code) > 10:
                self.set_credentials(code)
            else:
                self.labelStatusSettings.setText("Code field must be bigger than 20 characters..")     
    
    def log_data(self,data):
        #print(data)
        pass
    
    def check_manager_error(self):
        self.labelStatusMain.setText("")
        self.labelStatusSettings.setText( "")
        if self.error!=None:
            self.tabWidget.setCurrentIndex(1)
            self.labelStatusSettings.setText( "Error : " + self.error )
            self.labelStatusMain.setText("There is an error..")
            return False
        else:
            return True     

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

class Win(QtGui.QDialog,Ui_MainWindow):
    def __init__(self, nymphdataGui, nymphDataManager):
        Ui_MainWindow.__init__(self, nymphdataGui, nymphDataManager )
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

# Main application
if __name__ == "__main__":
    import sys
    from Manager import * 
    app = QtGui.QApplication(sys.argv)

    # Gui index  
    if sys.argv[1:]:
        index=sys.argv[1]
    else:
        gui_index=0
    try:
        gui_index=int(gui_index)
    except Exception, error:
        print("Please enter a integer number..")
        exit()
    if gui_index > len(nodes_gui) - 1:    
        print("Please enter a integer number less than %s.." % len(nodes))
        exit()

    # Manager index    
    if sys.argv[2:]:
        index_manager=sys.argv[2]
    else:
        index_manager=0
    try:
        index_manager=int(index_manager)
    except Exception, error:
        print("Please enter a integer number..")
        exit()
    if index_manager > len(nodes) - 1:    
        print("Please enter a integer number less than %s.." % len(nodes))
        exit()    

    # Our nodes    
    manager_node = nodes[index_manager]
    gui_node = nodes_gui[gui_index]
    if sys.argv[2:]: 
        manager = GDManager( manager_node, gui_node)       
    MWindow = Win( gui_node , manager_node)
    MWindow.show()
    sys.exit(app.exec_())
