# @Dhhearj Kumar Rao
import httplib2
import requests
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
import io
from apiclient.http import MediaIoBaseDownload

def getDriveService():
    ClientID = '1059750178555435-b9qcloldt31nf754ojtmh63i7n8t8s40.apps.googleusercontent.com'
    ClientSecret = ''
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    flow = OAuth2WebServerFlow(ClientID, ClientSecret, OAUTH_SCOPE, REDIRECT_URI)
    flow.redirect_uri = REDIRECT_URI
    authorize_url = flow.step1_get_authorize_url()
    print (authorize_url)
    code = input('Enter verification code: ').strip()
    credentials = flow.step2_exchange(code)          
    http = httplib2.Http()
    http = credentials.authorize(http)

    return build('drive', 'v2', http=http)
#print(getDriveService());
drive_service = getDriveService()
files = drive_service.files().list().execute()

file_id = files['items'][0]['id']


drive_file = drive_service.files().get(fileId=file_id).execute()

print(drive_file);
print ('Title: %s' % drive_file['title'])
#print ('Description: %s' % drive_file['description'])
print ('MIME type: %s' % drive_file['mimeType'])
print ('MIME type: %s' % drive_file['webContentLink'])
