from __future__ import unicode_literals
import youtube_dl


def all_youtube():
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=9KZsgt5ENB4'])
