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
        self.talkWith(interfaceNymphData)
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
            f = open('conf.json','r')
            try:
                conf = f.read()
                status=True 
            except Exception, error:
                print 'An error occurred: %s' % error
                status=False 
            finally:
                f.close()
            if status:
                self.credentials    = oauth2client.client.Credentials.new_from_json(conf)
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
        # format of json words
        # '{ "query": "function_name", "0": "first_arg", "1": "second_arg" }'
        try:
            words=json.loads( words );
        except Exception, error:
            print 'An error occurred: %s' % error
            ret=error
            words={'query': "error"} 

        if words['query']=="read":
            #args None
            #return Array file_informations
            ret= self.read() 
        elif words['query']=="upload":
            #args-0 string filename
            #args-1 boolean is_sharable
            #return  True or False
            ret= self.upload( words['0'], words['1'] )
        elif words['query']=="get_authorize_url":
            #args None 
            #return string  authorize_url  or ''  
            ret= self.get_authorize_url()
        elif words['query']=="set_credentials":
            #args-0 string code
            #return True or False
            ret= self.set_credentials( words['0'] )
        elif words['query']=="init":
            #args None
            #return True or False - self.service_status 
            ret= self.init()
        elif words['query']=="url":
            #sender nymphdata( words['0'], words['1'], int(words['2']))
            #message words['3']
            #args-0 nymphdata name value                 
            #args-1 nymphdata host value                 
            #args-2 nymphdata port value                 
            #args-3 string url
            #args-4 string title
            #return {"name": "n_name", "host":"n_host", "port":"n_port", "":"url" }       
            ret={   
                "0": words['0'], 
                "1": words['1'], 
                "2": str(words['2']), 
                "3": words['3'],
                "4": words['4'] 
            }
            self.download_url(words['3'], words['4'] )
            #nymphdata(name,host,port) and url
        elif words['query']=="message":
            #sender nymphdata( words['0'], words['1'], int(words['2']))
            #message words['3']
            #args-0 nymphdata name value                 
            #args-1 nymphdata host value                 
            #args-2 nymphdata port value                 
            #args-3 string message
            #return {"name": "n_name", "host":"n_host", "port":"n_port", "":"message" }  
            ret={   
                "0": words['0'], 
                "1": words['1'], 
                "2": str(words['2']), 
                "3": words['3'] 
            }
            #nymphdata(name,host,port) and message    
        elif words['query']=="talk":
            #args-0 nymphdata name value                 
            #args-1 nymphdata host value                 
            #args-2 nymphdata port value                 
            #args-3 string message                       
            #args-4 string message type - url or message 
            #return  boolean True, False
            # '{ "query": "talk", "0": "name", "1": "host", "2": "port", "3": "message_content", "4": "message" }'
            # '{ "query": "talk", "0": "name", "1": "host", "2": "port", "3": "url-link", "4": "url", "5": "title" }'
            self.error=None
            self.talkWith( nymphdata( words['0'], words['1'], int(words['2'])) )#nymphdata(name,host,port)
            if self.error!=None:
                ret=False
            else:    
                if words['4']=="url":
                    # format of message 
                    # '{ "query": "url-or-message", "0": "name", "1": "host", "2": "port", "3": "url-link", "4": "title" }'
                    a=(words['4'], self.myN.NAME, self.myN.HOST, str(self.myN.PORT), words['3'], words['5'] )
                    self.say( '{ "query": "%s", "0": "%s", "1": "%s", "2": "%s", "3": "%s", "4": "%s" }' % a  ) #nymphdata(name,host,port) and message
                elif words['4']=="message" :
                    # format of message 
                    # '{ "query": "url-or-message", "0": "name", "1": "host", "2": "port", "3": "message"  }'
                    a=(words['4'], self.myN.NAME, self.myN.HOST, str(self.myN.PORT), words['3'] )
                    self.say( '{ "query": "%s", "0": "%s", "1": "%s", "2": "%s", "3": "%s" }' % a  ) #nymphdata(name,host,port) and message
                else:
                    self.error="unexpected_event"

                if self.error!=None:
                    ret=False
                else:
                    self.talkWith(self.interfaceNymphData)
                    if self.error!=None:
                        ret=False
                    else:
                        ret=True 
        elif words['query']!="error": # there is an error above
            pass
        else: # default query
            words={'query': "error"} 
            ret=False

        # wrie and send response    
        f = open('data.json','w')
        try:
            f.write( json.JSONEncoder().encode({'result': ret}) )
        except Exception, error:
            print 'An error occurred: %s' % error
            words={'query': "error"} 
        finally:
            f.close()
        print(words)
        # TODO improvemnet
        # Check if connection is exist
        self.talkWith(self.interfaceNymphData).say( words['query']+'_OK' )  
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
        print("ok i got the message1")
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
        print("ok i got the message")
        files = []
        for data in datas:
            item = []  
            item.append( data['title']          )  
            item.append( data['quotaBytesUsed'] )  
            item.append( str(data['shared'])    )
            if 'downloadUrl' in data:  
                item.append(data['downloadUrl'])
            else:
                if 'webContentLink' in data:  
                    item.append(data['webContentLink'])
                else:    
                    item.append('null-url')    
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
    
    # Download file from url       
    def download_url(download_url,title):    
        # Download 
        if download_url:
            resp, content =  self.drive_service._http.request(download_url)
            if resp.status == 200:
                f = open(title,'w')
                try:
                    f.write(content)
                    status=True
                except Exception, error:
                    print 'An error occurred: %s' % error
                    status=False
                finally:
                    f.close()
            else:
              print 'An error occurred: %s' % resp
              status=False
        else:
            # The file doesn't have any content stored on Drive.
            print("you dont have this file")
            status=False
        return status 

    # Download file with coming in response  json        
    def download(response):    
        # Download
        download_url = response['downloadUrl']
        if download_url:
            resp, content =  self.drive_service._http.request(download_url)
            if resp.status == 200:
                f = open(response['title'],'w')
                try:
                    f.write(content)
                    status=True
                except Exception, error:
                    print 'An error occurred: %s' % error
                    status=False
                finally:
                    f.close()
            else:
              print 'An error occurred: %s' % resp
              status=False
        else:
            # The file doesn't have any content stored on Drive.
            print("you dont have this file")
            status=False
        return status     
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
        status=False
        try:   
            self.credentials = self.flow.step2_exchange(authorization_code)
            f = open('conf.json','w')
            try:
                f.write(self.credentials.to_json())
                status=True
            except Exception, error:
                print 'An error occurred: %s' % error
                status=False 
            finally:
                f.close()
        except Exception, error:
            print 'An error occurred: %s' % error
            status=False 
        if status:
            self.init()     
        return status    

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
