from apiclient.discovery import build
import json
from passwords import GOOGLE_API_KEY
def youtube(str):
    youtube = build("youtube", "v3", developerKey=GOOGLE_API_KEY)
    search_response = youtube.search().list(q=str,part="id,snippet",maxResults=1).execute()
    link = search_response['items'][0]['id']['videoId']
    return "https://www.youtube.com/watch?v={}".format(link)
