from initialize import *

print '\n/********* List of files *******/'

# Get all files from drive service
result = []
page_token = None
while True:
    try:
      param = {}
      if page_token:
        param['pageToken'] = page_token
      files = drive_service.files().list(**param).execute()

      result.extend(files['items'])
      page_token = files.get('nextPageToken')
      if not page_token:
        break
    except errors.HttpError, error:
      print 'An error occurred: %s' % error
      break

# Write all filse content
for response in result:
    json.dumps(response, sort_keys=True, indent=4)
    if int(response['quotaBytesUsed']) > 0 :
      write(response)  # this method from initialize.py 
     