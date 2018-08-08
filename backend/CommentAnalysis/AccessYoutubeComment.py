import os
import pickle

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

# Call the API's commentThreads.list method to list the existing comments.
def get_comments(youtube, video_id):
    results = youtube.commentThreads().list(
      part="snippet",
      videoId=video_id,
      textFormat="plainText"
    ).execute()

    filename= 'Classifier.sav'
    Classifier = pickle.load(open(filename,'rb'))

    for item in results["items"]:
      comment = item["snippet"]["topLevelComment"]
      author = comment["snippet"]["authorDisplayName"]
      text = comment["snippet"]["textDisplay"]
      print(Classifier.classify(text))


    return results["items"]

def start(video_id):
    youtube = get_authenticated_service()
    try:
        get_comments(youtube,video_id)
    except HttpError as e:
        print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
    else:
        print ("Inserted, listed and updated top-level comments.")

start("1ZAPwfrtAFY")
