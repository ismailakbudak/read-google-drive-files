
import json   
from apiclient.http import MediaFileUpload

def write(response):
    print '===================   '+ response['title'] +' information    ==================='
    print 'Title : ' + response['title']
    print 'Size : ' + response['quotaBytesUsed']
    print 'Download : ' + response['webContentLink']
    print 'Show : ' + response['alternateLink']

def read(drive_service): 
    print '\n/********* List of files *******/'
    
    # Get all files from drive service
    result = []
    page_token = None
    while True:
      param = {}
      if page_token:
        param['pageToken'] = page_token
      files = drive_service.files().list(**param).execute()

      result.extend(files['items'])
      page_token = files.get('nextPageToken')
      if not page_token:
        break 
    # Write all filse content
    for response in result:
        json.dumps(response, sort_keys=True, indent=4)
        if int(response['quotaBytesUsed']) > 0 :
          write(response)  # this method from initialize.py 

def upload(drive_service):
    # Path to the file to upload
    FILENAME = 'text.txt'

    # Insert a file
    media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
    body = {
      'title': 'My google-python document',
      'description': 'A test document',
      'mimeType': 'text/plain'
    }

    response = drive_service.files().insert(body=body, media_body=media_body).execute()

    json.dumps(response, sort_keys=True, indent=4)

    print '\nFile uploaded successfully..'

    # this method from initialize.py 
    write(response)

    # or you can use
    #pprint.pprint(response) 