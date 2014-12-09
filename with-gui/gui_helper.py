from nymph.Nymph import *
import json



###
#       helper is the object interface for GDManager 
#       its responsible comminication between GDManager and user class
###
class helper(nymph):
    # helper is a nymph
    def __init__(self,nymphdata,managerNymphData):
        super(helper,self).__init__(nymphdata)
        self.managerNymphData = managerNymphData
        self.talkWith(managerNymphData)

    
    #listen is processes coming data to other nymph
    #
    #parameters:
    #   words
    #
    #return:
    def listen(self,words):
        print(words)
        try:
            data=json.loads(open('data.json','r').read())
        except Exception, error:
            data=None
            print"en error occured: %s " % (error)
        func={
            'read_OK':              self.read_Handler,
            'upload_OK':            self.upload_Handler,
            'get_authorize_url_OK': self.get_authorize_url_Handler,
            'set_credentials_OK':   self.set_credentials_Handler,
            'download_OK':          self.download_Handler,
            'message_OK':           self.listen_message_Handler,  
            'url_OK':               self.listen_url_Handler,          
            'error_OK':             self.error_Manager_Handler,
        }
        if(words in func):
            func[words](data)
        else:
            self.error_Manager_Handler('')
        print(words)
        
    ###
    #	Handlers For events between two GDManager
    def listen_url_Handler(self,data):
        pass
    
    def listen_message_Handler(self,data):
        pass
    ###
    #	Handlers For events between gui and GDManager
    def read_Handler(self,data):
        pass
    
    def upload_Handler(self,data):
        pass
        
    def get_authorize_url_Handler(self,data):
        pass
                
    def set_credentials_Handler(self,data):
        pass
    
    def download_Handler(self,data):
        pass
        
    def sendMessage_Handler(self,data):
        pass
    
    def setNode_Handler(self,data):
        pass
    
    def error_Manager_Handler(self,data):
        pass
    #sayFormat processes sending data to other nymph
    #
    #parameters:
    #   words
    #
    #return:
    def sayFormat(self,words):
        # TODO
        # Check if connection is exist
        #self.talkWith(self.managerNymphData)
        return words
    
    #read trigger read proccess and return results
    #
    #parameters:
    #   words
    #
    #return:
    def read(self):
        self.say('{ "query": "read" }')
        
    #upload trigger upload proccess for filename 
    #
    #parameters:
    #   filename
    #   is_share
    #
    #return:
    def upload(self,filename,is_share):    
        self.say('{ "query": "upload", "0": "%s", "1": "%s" }' % ( filename, str(is_share) ))
        
    #return an authorize url
    #
    #parameters:
    #
    #return:
    def get_authorize_url(self):
        self.say('{ "query": "get_authorize_url" }')
        
        
    #set the credentials  
    #
    #parameters:
    #   authorization_code
    #
    #return:
    def set_credentials(self, authorization_code):
        self.say('{ "query": "set_credentials", "0": "%s" }' % (authorization_code) )
        
    #download the url   
    #
    #parameters:
    #   url
    #
    #return:
    def download(self,url):
        self.say('{ "query": "download", "0": "%s" }' % (url) )
    
    def init():
        self.say('{ "query": "init" }')    
    #set the Other GDManager Node
    #
    #parameters:
    #   nymphdata
    #
    #return:
    def talk(self,nymphdata,message,message_type):
        a = (nymphdata.NAME, nymphdata.HOST, str(nymphdata.PORT), message, message_type )
        self.say('{ "query": "talk", "0": "%s", "1": "%s", "2": "%s", "3": "%s", "4": "%s" }' % a)
        