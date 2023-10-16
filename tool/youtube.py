# first step that you want to download these youtube videos:
# pip install yt-dlp

import yt_dlp

url=input("enter video url: ")
# When I was 14, my best friend committed suicide. It was the most lost and broken point of my life, and this was the song played for her funeral. At first I couldn’t listen to this song without breaking down, but now I listen to this song to help me through the hard moments. It gives me a calming feeling that she’s right beside me. Thank you, Beatles, for creating a song that can be just as beautiful as it is tragic. Thank you for allowing her to live on.

# It's hard to believe that this song is over 50 years old and it still brings tears to my eyes every time I hear Paul sing his song.   Thank you Paul, for this beautiful song.


'''
https://www.youtube.com/watch?v=QDYfEBY9NM4

When I find myself in times of trouble, Mother Mary comes to me
Speaking words of wisdom, let it be
And in my hour of darkness she is standing right in front of me
Speaking words of wisdom, let it be
Let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be
And when the broken hearted people living in the world agree
There will be an answer, let it be
For though they may be parted, there is still a chance that they will see
There will be an answer, let it be
Let it be, let it be, let it be, let it be
There will be an answer, let it be
Let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be
Let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be, be
And when the night is cloudy there is still a light that shines on me
Shinin' until tomorrow, let it be
I wake up to the sound of music, Mother Mary comes to me
Speaking words of wisdom, let it be
And let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be
And let it be, let it be, let it be, let it be
Whisper words of wisdom, let it be
'''

ydl_opts={}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
# 
print("video download suceessful!!!")
