from initialize import * 

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

