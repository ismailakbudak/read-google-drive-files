from nymph.Nymph import *




###
#       helper is the object interface for GDManager 
#       its responsible comminication between GDManager and user class
###
class helper(nymph):
    # helper is a nymph
    def __init__(self,nymphdata):
        super(helper,self).__init__(nymphdata)
    
    #listen is processes coming data to other nymph
    #
    #parameters:
    #   words
    #
    #return:
    def listen(self,words):
        data=json.loads(open('data.json','r').read())
        func={
            'read_OK':read_handler,
            'upload_OK':upload_Handler,
            'get_authorize_url_OK':get_authorize_url_Handler,
            'set_credentials_OK':set_credentials_Handler,
            'download_OK':download_Handler,
            'message_OK':listen_message_Handler,  
            'url_OK':listen_url_Handler,          
            'error_OK':error_Manager_Handler,
        }
        if(words in func):
            func[words](data)
        else:
            error_Manager_Handler('')
        print(words)
        

    
    def listen_url_Handler(self,data):
        pass
    
    def listen_message_Handler(self,data):
        pass
    
    
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
        self.say('{ "query": "upload", "0": "' + filename + '", "1": "' + is_share + '" }')
        
    #return an authorize url
    #
    #parameters:
    #
    #return:
    def get_authorize_url(self):
        '{ "query": "get_authorize_url" }'
        self.say("get_authorize_url")
        
        
    #set the credentials  
    #
    #parameters:
    #   authorization_code
    #
    #return:
    def set_credentials(self, authorization_code):
        self.say('{ "query": "set_credentials", "0": "' + authorization_code + '" }')
        
    #download the url   
    #
    #parameters:
    #   url
    #
    #return:
    def download(self,url):
        self.say('{ "query": "download", "0": "'+url+'" }')
    
        
    #set the Other GDManager Node
    #
    #parameters:
    #   nymphdata
    #
    #return:
    def talk(self,nymphdata,message):
        self.say('{ "query": "talk", "0": "'+nymphdata.NAME+'", "1": "'+nymphdata.HOST+'", "2": "'+nymphdata.PORT+'", "3": "'+message+'" }')
        