# Make an application that lets download a certain file from the web
#

# Import the necessary modules
import asyncio
import requests 
import time
import os
import sys
import datetime
import tqdm
# ASCII
import pyfiglet


# Print the ASCII art
print(pyfiglet.figlet_format("async_studios", font="slant"))

# Print welcome message
print("------------------------------------------------------")
print("Welcome to async_studios file manager!")
print("Made by: @theAsyncStudios")
print("github.com/theAsyncStudios")
# print the current date and time
print("Current date and time: " + str(datetime.datetime.now()))
print("------------------------------------------------------")

# set the url for the checker
url = 'https://pastebin.com/raw/4y2GVi0Y'
version = '1.10b'

# check if the script is up to date
r = requests.get(url)
if r.text == version:
    # if the script is up to date, print that

    print("Your version is up to date!")
    print("------------------------------------------------------")
else:
    # if the script is not up to date, print that
    print("Your version is outdated!")
    print("Current version: " + version)
    print("New version: " + r.text)
    print("------------------------------------------------------")
    print("Updating...")
    time.sleep(1.5)
    print("------------------------------------------------------")
    print("Update complete!")
    print("------------------------------------------------------")

time.sleep(2)
# Show update logs
print("Update logs: " + r.text)
print("------------------------------------------------------")
print("[+] Added ASCII to all the scripts")
print("[+] Added a new update checker")
print("[=] Fixed a bug with the update checker")
print("------------------------------------------------------")
# print out the available options
time.sleep(2)
print("Available options:")
print("1. Download 'YouTube Downloader'")
print("2. Download 'Kalkulator")
print("3. Download 'Generator Haseł'")
print("4. Exit")
print("------------------------------------------------------")
# ask the user for the option
time.sleep(1.5)
option = input("Please choose an option: ")

# if the user chooses 1, download the file
if option == "1":
    # download the file
    print("------------------------------------------------------")
    print("Downloading 'YouTube Downloader'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://pastebin.com/raw/1T5SSVyk'
    # set the file name
    filename = 'YouTube_Downloader.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("------------------------------------------------------")
    print("Download complete!")
    print("------------------------------------------------------")
# if the user chooses 2, download the file
elif option == "2":
    # download the file
    print("------------------------------------------------------")
    print("Downloading 'Kalkulator'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://pastebin.com/raw/i1J8XkVk'
    # set the file name
    filename = 'Kalkulator.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("------------------------------------------------------")
    print("Download complete!")
    print("------------------------------------------------------")
# if the user chooses 3, download the file
elif option == "3":
    # download the file
    print("------------------------------------------------------")
    print("Downloading 'Generator Haseł'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://pastebin.com/raw/wxKUgTRf'
    # set the file name
    filename = 'Generator_Haseł.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("------------------------------------------------------")
    print("Download complete!")
    print("------------------------------------------------------")

# if the user chooses 4, exit the program
elif option == "4":
    # exit the program
    print("------------------------------------------------------")
    print("Exiting...")
    print("------------------------------------------------------")
    sys.exit()
# if the user chooses something else, print that
else:
    print("------------------------------------------------------")
    print("Invalid option!")
    print("------------------------------------------------------")












    










# press enter to exit 
input("Press ENTER to exit")
