#!/usr/bin/python
import httplib2
import pprint
from config import *
from apiclient.discovery import build
import oauth2client.client
      
# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

# Run through the OAuth flow and retrieve credentials
flow = oauth2client.client.OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print ("\nGo to the permission link : \n"  + authorize_url)
code = raw_input('\nVerification code: ').strip()
credentials = flow.step2_exchange(code)

# Save your credentials to file
open('conf.json','w').write(credentials.to_json())

# Load your credentials from file
# Remove comment for this and add comment to credentials generater
#credentials =  oauth2client.client.Credentials.new_from_json(open('conf.json','r').read())

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)
drive_service = build('drive', 'v2', http=http)