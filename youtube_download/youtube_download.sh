#!/bin/bash

music_directory="$HOME/Music"

echo URL:
read url 

echo name:
read name

youtube-dl -o "$music_directory/$name.%(ext)s" --extract-audio --audio-format mp3 $url --no-mtime
