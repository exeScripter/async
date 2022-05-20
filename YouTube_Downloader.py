# Make a YouTube Downloader that supports multiple formats
# Author: @naroors (github.com/exeScripter)
# Date: 2022-05-18

# Import pytube 
from pytube import YouTube
import os
import datetime
import requests
import time

# Import pyfiglet
import pyfiglet

# from text create an ASCII art
print(pyfiglet.figlet_format("YouTube Downloader", font="slant"))

# Print welcome message
print("------------------------------------------------------")
print("Witaj w Youtube to MP3/MP4 Downloader!")
print("Zrobione przez: @theAsyncStudios")
print("github.com/theAsyncStudios")
# print the current date and time
print("Aktualny czas i data: " + str(datetime.datetime.now()))
print("------------------------------------------------------")

# set the url for the checker
url = 'https://pastebin.com/raw/4y2GVi0Y'
version = '1.10b'

print("Sprawdzam aktualizacje...")
time.sleep(1.5)
# check if the script is up to date
r = requests.get(url)
if r.text == version:
    # if the script is up to date, print that
    print("------------------------------------------------------")
    print("Twoja wersja jest aktualna!")
    print("------------------------------------------------------")
else:
    # if the script is not up to date, print that
    print("------------------------------------------------------")
    print("Twoja wersja jest nieaktualna!")
    print("Aktualna wersja: " + version)
    print("Najnowsza wersja: " + r.text)
    print("------------------------------------------------------")
    print("Aktualizuję...")
    time.sleep(1.5)
    print("------------------------------------------------------")
    print("Aktualizacja zakończona!")
    print("------------------------------------------------------")






yt = YouTube(str(input("Wpisz/Wklej URL Filmu na YouTube: \n ")))

video = yt.streams.first(onlyAudio=True)

print("------------------------------------------------------")
print("Wpisz miejsce w którym chcesz zapisać (zostaw puste jeśli chcesz domyślnie): \n")
destination = str(input(" ")) or "."
out_file = video.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base +  '.mp3'
os.rename(out_file, new_file)


print("------------------------------------------------------")
print(yt.title + " pobrano pomyślnie!")
# Show the location and print it
print("Zapisano w: " + new_file)
print("------------------------------------------------------")

# Print the video title and the video duration
print("Tytuł: " + yt.title)
# Display the length in minutes and seconds
print("Długość: " + str(datetime.timedelta(seconds=yt.length)))

print("------------------------------------------------------")
    
# Prevent the file from closing
input("Naciśnij ENTER aby wyjść")


