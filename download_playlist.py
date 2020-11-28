#! python3

from pytube import Playlist
import sys

playlist = Playlist(sys.argv[1])

folder = playlist.title.replace(' ', '_')

print()
print(f'Downloading: {playlist.title}')
print(f'Folder: {folder}')
print()

for video in playlist.videos:
	print(video.streams.first().download(folder))
	print()

