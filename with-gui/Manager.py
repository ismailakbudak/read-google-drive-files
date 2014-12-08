#from nymph.Nymph import *
from nymph.IP import *
import json, os, sys, httplib2, oauth2client.client
from apiclient.http import MediaFileUpload  
from apiclient.discovery import build

class status(object):
    uploaded=0
    uploaded_shared=1
    uploaded_could_not_shared=2
    could_not_uploaded=3
    uploaded_not_shared=4

class GDManager(nymph):

    # Google drive global flow
    #gdmanager_ 
    flow = None
    def __init__(self, nymphData,interfaceNymphData):
        super(GDManager, self).__init__(nymphData)
        self.interfaceNymphData=interfaceNymphData
        self.http = httplib2.Http()
        self.init()


    '''
    initialize global variables 
    Args: 
      None
    Returns:
      Boolean Service status
    '''
    def init(self):
        try:
            self.credentials    = oauth2client.client.Credentials.new_from_json(open('conf.json','r').read())
            self.http           = self.credentials.authorize(self.http)
            self.drive_service  = build('drive', 'v2', http=self.http)
            self.service_status = True
        except Exception, error:
            print 'An error occurred: %s' % error
            self.drive_service  = None
            self.http           = None
            self.credentials    = None 
            self.service_status = False
        return self.service_status
    '''
    Nymph listen method override
    Args: 
      words: string comming message
    Returns:
      None
    '''
    def listen(self,words):
        
        print(words)
        if words=="read":
            #args None
            #return Array file_informations
            ret= self.read() 

            self.say("read_OK")
        elif words=="upload":
            #args string filename
            #args boolean is_sharable
            #return  True or False
            ret= self.upload("test_start.py",True)
            self.say("upload_OK")
        elif words=="get_authorize_url":
            #args None 
            #return string  authorize_url  or ''  
            ret= self.get_authorize_url()

            self.say("authorization_OK")
        elif words=="set_credentials":
            #args string code
            #return True or False
            ret= self.set_credentials("asdasdasdasd")

            self.say("credentials_OK")
        elif words=="init":
            #args None
            #return True or False - self.service_status 
            ret= self.init()

            self.say("init_OK") 
        elif words=="talk":
            #args nymphdata value
            #args string message
            #return  boolean True, False

            #TODO
            #self.talkWith()#nymphdata
            #self.say()#message
            self.talkWith(self.interfaceNymphData)
            self.say("talk_OK")
            ret=True
        else:
            ret=False 
        open('data.json','w').write( json.JSONEncoder().encode({'result': ret}) )

    '''
    Message format for ui
    Args: 
      words: string comming message
    Returns:
      String 
    '''
    def sayFormat(self,words):
        return words

    '''
    Read cloud files
    Args: 
      None
    Returns:
      Array datas
    '''
    def read(self):
        datas = []   
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
            for response in result:
                json.dumps(response, sort_keys=True, indent=4)
                datas.append(response)
        except Exception, error:
            print 'An error occurred: %s' % error
            datas = []
        ## Get a few properties
        files = []
        for data in datas:
            item = []  
            item.append( data['title']          )  
            item.append( data['quotaBytesUsed'] )  
            item.append( str(data['shared'])    )  
            item.append( data['webContentLink'] )
            files.append(item)  
          
        return files 
      
    '''
    Insert a new permission.
    Args: 
      file_id: ID of the file to insert permission for.
    Returns:
      True or False.
    '''
    def insert_permission(self, file_id):
        '''
        value: User or group e-mail address, domain name or None for 'default'
               type.
        perm_type: The value 'user', 'group', 'domain' or 'default'.
        role: The value 'owner', 'writer' or 'reader'.
        '''
        value       = 'anyone'
        perm_type   = 'anyone'
        role        = 'writer'
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
     
    '''
    Upload file to cloud
    Args: 
      filename: string filename
      is_share: boolean file is sharable or not
    Returns:
      string status
    '''
    def upload(self,filename,is_share):
        Status=status()
        try:
            media_body  = MediaFileUpload(filename, mimetype='text/plain', resumable=True)
            doc_names   = filename.split('/');
            doc_name    = doc_names[ len(doc_names)-1 ]
            body        = { 
                'title': doc_name,
                'description': 'A document from google drive sevice',
                'mimeType': 'text/plain'   
            }
            response = self.drive_service.files().insert(body=body, media_body=media_body).execute()
            json.dumps(response, sort_keys=True, indent=4)
            if is_share:
               if self.insert_permission( response['id']) :
                  _status = Status.uploaded_shared 
               else :
                  _status = Status.uploaded_could_not_shared
            else :
                _status = Status.uploaded_not_shared 
        except Exception, error:
            print 'An error occurred: %s' % error
            _status = Status.could_not_uploaded
        return _status     
 
    '''
    Get new authorize url.
    Args: 
      None
    Returns:
      String url
    '''
    def get_authorize_url(self):
        import config as con
        OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
        REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
        try:
            self.flow = oauth2client.client.OAuth2WebServerFlow(con.CLIENT_ID, con.CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
            authorize_url = self.flow.step1_get_authorize_url()
        except Exception, error:
            print 'An error occurred: %s' % error 
            authorize_url = ''    
        return authorize_url  
     
    '''
    Create new credentials
    Args: 
      authorization_code: string authorization code from your browser 
    Returns:
      True or False.
    '''   
    def set_credentials(self, authorization_code):
        try:   
            self.credentials = self.flow.step2_exchange(authorization_code)
            open('conf.json','w').write(self.credentials.to_json())
        except Exception, error:
            print 'An error occurred: %s' % error
            return False 
        return True    

    '''Update an existing file's metadata and content.
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
    '''
    def update_file(self, file_id ): 
        try:
            # First retrieve the file from the API.
            file = self.drive_service.files().get(fileId=file_id).execute()
            new_filename = 'ok2.txt'
            description = 'test deneme2'
            new_mime_type = 'text/plain'
            # File's new metadata.
            file['title'] = new_filename
            file['description'] = description
            file['mimeType'] = new_mime_type 
            # Send the request to the API.
            updated_file = self.drive_service.files().update(
                fileId=file_id,
                body=file ).execute()
            return updated_file
        except errors.HttpError, error:
            print 'An error occurred: %s' % error
            return None    
