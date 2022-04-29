import googleapiclient
from googleapiclient.discovery import build
import creds
import youtube_dl
def my_hook(d):
    if d['status'] == 'finished':
        print('done')
youtube_api_key=creds.get_youtube_api_key()

#We have gotten the tracks, make use of youtube api
youtube=googleapiclient.discovery.build('youtube','v3',developerKey=youtube_api_key)
request=youtube.search().list(part='snippet', maxResults=25, q='drugs tai verdes')
response=request.execute()
print(response['items'][10]['id'])
with open("C:/Users/Fran/Desktop/Testing.txt", 'w') as f:
    for y in response['items']:
        if(y['id']['kind'] == 'youtube#video'):
            f.write("https://www.youtube.com/watch?v="+y['id']['videoId']+'\n')

request=youtube.videos().list(part= "contentDetails", id="otyPTI9iMjw")
response1=request.execute()
print(response1)
ydl_opts = {
    'format' : 'bestaudio/best',
    'postprocessors' : [{
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'm4a',
        'preferredquality' : '256'
    }],
    'progress_hooks' : [my_hook]

}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=otyPTI9iMjw'])
#Can make searches. From searches find length closest to song length on spotify. If >30 seconds return in the errors file. put URL into txt

def get_videos(search):
    request = youtube.search().list(part='snippet', maxResults=25, q=search)
    response = request.execute()
    for x in response['items']:
        if(x['id']['kind'] == 'youtube#video'):
            return x['id']['videoId']

#def download_audio(url):





