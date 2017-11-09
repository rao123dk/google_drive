# @Dhhearj Kumar Rao
import webbrowser
import httplib2
import os
import io
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
#from oauth2client.file import Storage
from apiclient.http import MediaIoBaseDownload

def download_file(file_id, mimeType, filename):
    if "google-apps" in mimeType:
        # skip google files
        return
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))


if __name__ == '__main__':
    flow = client.flow_from_clientsecrets(
      'client_secret.json',
      scope='https://www.googleapis.com/auth/drive.readonly',
      redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open(auth_uri)

    print (auth_uri)

    auth_code = input('Enter the auth code: ')

    credentials = flow.step2_exchange(auth_code)
    http_auth = credentials.authorize(httplib2.Http())

    drive_service = discovery.build('drive', 'v3', http_auth)
    files = drive_service.files().list().execute()
    for f in files['files']:
        print (f['name'])
        download_file(f['id'], f['mimeType'], f['name'])