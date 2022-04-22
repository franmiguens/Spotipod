from googleapiclient.discovery import build
import creds

youtube_api_key=creds.get_youtube_api_key()

#We have gotten the tracks, make use of youtube api
youtube=googleapiclient.discovery.build('youtube','v3',developerKey=youtube_api_key)
request=youtube.search().list(part='snippet', maxResults=25, q='drugs tai verdes')
response=request.execute()
print(response['items'][9]['id'])
with open("C:/Users/Fran/Desktop/Testing.txt", 'w') as f:
    for y in response['items']:
        if(y['id']['kind'] == 'youtube#video'):
            f.write("https://www.youtube.com/watch?v="+y['id']['videoId']+'\n')
#Can make searches. From searches find length closest to song length on spotify. If >30 seconds return in the errors file. put URL into txt


