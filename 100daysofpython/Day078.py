'''
Day 78: Download Files
Create a script to download files from a website.
'''

import yt_dlp

ydl_opts = {
    'format': 'best',
    'outtmpl': 'video.mp4'
}

url = input('Url video: ')

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])