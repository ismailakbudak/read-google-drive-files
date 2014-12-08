from nymph.Nymph import *




###
#	helper is the object interface for GDManager 
#	its responsible comminication between GDManager and user class
###
class helper(nymph):
    # helper is a nymph
    def __init__(self,nymphdata):
        super.(helper,self).__init__(nymphdata)
    
    #listen is processes coming data to other nymph
    #
    #parameters:
    #	words
    #
    #return:
    def listen(self,words):
    	print(words)
    
    #sayFormat processes sending data to other nymph
    #
    #parameters:
    #	words
    #
    #return:
    def sayFormat(self,words):
    	return words
    
    #read trigger read proccess and return results
    #
    #parameters:
    #	words
    #
    #return:
    def read(self):
    	self.say("read")
    	
    #upload trigger upload proccess for filename 
    #
    #parameters:
    #	filename
    #	is_share
    #
    #return:
    def upload(self,filename,is_share):
    	self.say("upload")
    	
    #return an authorize url
    #
    #parameters:
    #
    #return:
    def get_authorize_url(self):
    	self.say("get_authorize_url")
    	
    	
    #set the credentials  
    #
    #parameters:
    #	authorization_code
    #
    #return:
    def set_credentials(self, authorization_code):
    	self.say("set_credentials")
    	
    #download the url	
    #
    #parameters:
    #	url
    #
    #return:
    def download(self,url):
    	self.say("download")
    
    #sends Message to Other GDManager Node
    #
    #parameters:
    #	message
    #
    #return:
    def sendMessage(self,message):
    	self.say("download")
    	
    #set the Other GDManager Node
    #
    #parameters:
    #	words
    #
    #return:
    def setNode(self,nymphdata):
    	self.say("setNode")