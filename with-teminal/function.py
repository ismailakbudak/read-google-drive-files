
import json   
from apiclient.http import MediaFileUpload
from apiclient import errors
import pprint

# Write file information
def write(response):
    print '===================   '+ response['title'] +' information    ==================='
    print 'Title : ' + response['title']
    print 'Size : ' + response['quotaBytesUsed']
    print 'Download : ' + response['webContentLink']
    print 'Show : ' + response['alternateLink']
    print 'Shared : ' + str(response['shared'])

# Add new permission to file, Provides sgared file
def insert_permission(service, file_id ):
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
  value = 'anyone'
  perm_type = 'anyone'
  role = 'writer'
  new_permission = {
      'value': value,
      'type': perm_type,
      'role': role
  }
  try:
    return service.permissions().insert(
        fileId=file_id, body=new_permission).execute()
  except errors.HttpError, error:
    print 'An error occurred: %s' % error
  return None

# Update file information
def update_file(service, file_id ):
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
    # File's new content.
    #media_body = MediaFileUpload( new_filename, mimetype='text/plain', resumable=True)
    # Send the request to the API.
    updated_file = service.files().update(
        fileId=file_id,
        body=file ).execute()
    return updated_file
  except errors.HttpError, error:
    print 'An error occurred: %s' % error
    return None

# Read google drive files
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
    i = 0
    for response in result: 
        # Write to file information
        #open('text'+str(i)+'.txt','w').write(json.dumps(response, sort_keys=True, indent=4))
        i = i +1
        json.dumps(response, sort_keys=True, indent=4)
        #insert_permission(drive_service, response['id'] )
        #update_file(drive_service, response['id'] )
        if int(response['quotaBytesUsed']) > 0 :
          write(response)  # this method from initialize.py 

# Upload file to drive
def upload(drive_service):
    # Path to the file to upload
    FILENAME = 'text.txt'
    # Insert a file
    media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
    body = {
      'title': 'My google-python document',
      'description': 'A test document',
      'mimeType': 'text/plain',
      'shared': 'true',
      'userPermission': {
       'type': 'anyone',
       'role': 'writer'
      }
    }
    response = drive_service.files().insert(body=body, media_body=media_body).execute()
    json.dumps(response, sort_keys=True, indent=4)
    print '\nFile uploaded successfully..'
    # this method from initialize.py 
    write(response)
    # or you can use
    #pprint.pprint(response) 