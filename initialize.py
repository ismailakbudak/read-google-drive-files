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
#flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
#authorize_url = flow.step1_get_authorize_url()
#print ("\nGo to the permission link : \n"  + authorize_url)
#code = raw_input('\nVerification code: ').strip()
#credentials = flow.step2_exchange(code)

#cred = '{"_module": "oauth2client.client", "token_expiry": "2014-11-27T21:15:05Z", "access_token": "ya29.ywBKZh-P5xl-YOEQ38WZe1xgj6pz0exWSUMErHft_o7WPtNhDrDLxBPO11NYPe_UHEd6ucytQz_SQQ", "token_uri": "https://accounts.google.com/o/oauth2/token", "invalid": false, "token_response": {"access_token": "ya29.ywBKZh-P5xl-YOEQ38WZe1xgj6pz0exWSUMErHft_o7WPtNhDrDLxBPO11NYPe_UHEd6ucytQz_SQQ", "token_type": "Bearer", "expires_in": 3600, "refresh_token": "1/CPgbbEtneE5QepQKl0Qmmo4xut0zUm7MGZUwB1yllSw"}, "client_id": "592104992808-l2q8uaai8se5bsp2j50kmfq4n517ol2a.apps.googleusercontent.com", "id_token": null, "client_secret": "k-6pT_t4A1osT5MYSwmyLyhf", "revoke_uri": "https://accounts.google.com/o/oauth2/revoke", "_class": "OAuth2Credentials", "refresh_token": "1/CPgbbEtneE5QepQKl0Qmmo4xut0zUm7MGZUwB1yllSw", "user_agent": null}'
credentials =  oauth2client.client.Credentials.new_from_json(open('conf.json','r').read())
 
#open('conf.json','w').write(credentials.to_json())

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)