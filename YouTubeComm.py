import googleapiclient
from googleapiclient.discovery import build
import creds
import youtube_dl
from requests import get
import yt_dlp


def my_hook(d):
    if d['status'] == 'finished':
        print('done')


youtube_api_key = creds.get_youtube_api_key()

# We have gotten the tracks, make use of youtube api
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=youtube_api_key)



# print(video)


# request=youtube.search().list(part='snippet', maxResults=25, q='drugs tai verdes')
# response=request.execute()
# print(response['items'][10]['id'])


# with open("C:/Users/Fran/Desktop/Testing.txt", 'w') as f:
#    for y in response['items']:
#        if(y['id']['kind'] == 'youtube#video'):
#            f.write("https://www.youtube.com/watch?v="+y['id']['videoId']+'\n')
# Remove this


# request=youtube.videos().list(part= "contentDetails", id="otyPTI9iMjw")
# response1=request.execute()
# print(response1)
# ydl_opts = {
#        'format': 'bestaudio/best',
#        'outtmpl': '/Users/franciscomiguens/Desktop/Coding/music/'+'playlist'+'/%(title)s.%(ext)s',
#        'ffmpeg_location': '/Users/franciscomiguens/Desktop/Coding/ffmpeg/ffmpeg',
#        'postprocessors': [{
#            'key': 'FFmpegExtractAudio',
#            'preferredcodec': 'm4a',
#            'preferredquality': '256'
#        }],
#        'progress_hooks': [my_hook]
#    }
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#    ydl.download(['https://www.youtube.com/watch?v=oTwVce9eWb4'])
# Can make searches. From searches find length closest to song length on spotify. If >30 seconds return in the errors file. put URL into txt
def get_videos(search, duration,cookiefile):
    # request = youtube.search().list(part='snippet', maxResults=25, q=search)
    # response = request.execute()
    # for x in response['items']:
    #    if (x['id']['kind'] == 'youtube#video'):
    #        return x['id']['videoId']
    ydl_opts = {
        'quiet': True,
        'cookiefile': cookiefile,
        'skip_download': True,
        'forcetitle': True,
        'forceurl': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        infoSearched = ydl.extract_info("ytsearch10:" + search)
    for x in infoSearched['entries']:
#        print(str(abs(x['duration']) - duration)+'\n')
        if abs(x['duration'] - duration) < 10:
            return x['webpage_url']
#    print(infoSearched['entries'])
    return infoSearched['entries'][0]['webpage_url']


def download_audio(url, playlist, song_title, uni_output, cookiefile, ffmpeg):
    output = uni_output + playlist + '\\' + song_title + '.%(ext)s'
    print(cookiefile)
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output,
        'cookiefile': cookiefile,
        'ffmpeg_location': ffmpeg,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '256'
        }],
        'progress_hooks': [my_hook]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.cache.remove()
            ydl.download([url])
            return False
        except yt_dlp.DownloadError as error:
            return True
