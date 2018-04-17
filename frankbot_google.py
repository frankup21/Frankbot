from googleapiclient.discovery import build
from passwords import GOOGLE_API_KEY
def google(str):
	service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
	res = service.cse().list(q=str, cx='016654653224191036952:bj0zhyarxza',).execute()
	return res['items'][0]['link']
