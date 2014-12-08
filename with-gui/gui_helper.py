from nymph.Nymph import *
class helper(nymph):
    def __init__(self,nymphdata):
        super.(helper,self).__init__(nymphdata)
    
    def listen(self,words):
    	print(words)
    
    def sayFormat(self,words):
    	return words
    
    def read(self):
    	pass
    	
    def upload(self,filename,is_share):
    	pass
    	
    def get_authorize_url(self):
    	pass
    	
    def set_credentials(self, authorization_code):
    	pass
    	
    def download(self,url):
    	pass
    
    def sendMessage(self,message):
    	pass
    	
    def setNode(self,nymphdata):
    	pass