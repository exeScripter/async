# MIT License
# github.com/exeScripter/async

# Import the necessary modules
import asyncio
import requests 
import time
import os
import sys
import datetime
import tqdm
import webbrowser
# ASCII
import pyfiglet

# Set the title of the program
async def title():
    # ASCII
    async with asyncio.get_running_loop().run_in_executor(None, pyfiglet.figlet_format, "async") as result:
        print(result)

# Print the ASCII art
print(pyfiglet.figlet_format("Async Manager", font="slant"))

# Print welcome message
print("------------------------------------------------------")
print("Welcome to async_studios file manager!")
print("Made by: @theAsyncStudios")
print("github.com/theAsyncStudios")
# print the current date and time
print("Current date and time: " + str(datetime.datetime.now()))
print("------------------------------------------------------")

# set the url for the checker
url = 'https://pastebin.com/raw/XhdfzGqe'
version = '3.0'

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
print("[+] Added two new scripts to the list!")
print("[+] Added a new feature!")
print("------------------------------------------------------")
# print out the available options
time.sleep(2)
print("Available options:")
print("1. Download 'YouTube Downloader'")
print("2. Download 'Kalkulator'")
print("3. Download 'Generator Haseł'")
print("4. Download 'Website Hooker'")
print("5. Download 'URL Shortener'")
print("6. Download 'Średnia'")
print("7. Download 'Lech czy Legia?'")
print("8. Join Discord Server")
print("9. Exit")
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
    url = 'https://raw.githubusercontent.com/exeScripter/async/main/py/youtube_downloader.py'
    # set the file name
    filename = 'YouTube_Downloader.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("Download complete!")
    print("------------------------------------------------------")
# if the user chooses 2, download the file
elif option == "2":
    # download the file
    print("------------------------------------------------------")
    print("Downloading 'Kalkulator'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://raw.githubusercontent.com/exeScripter/async/main/py/calculator.py'
    # set the file name
    filename = 'Kalkulator.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("Download complete!")
    print("------------------------------------------------------")
# if the user chooses 3, download the file
elif option == "3":
    # download the file
    print("------------------------------------------------------")
    print("Downloading 'Generator Haseł'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://raw.githubusercontent.com/exeScripter/async/main/py/generator_hase%C5%82.py'
    # set the file name
    filename = 'Generator_Haseł.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("Download complete!")
    print("------------------------------------------------------")

elif option == "4":
    # download the file
    print("------------------------------------------------------")
    print("Downloading 'Website Hooker'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://raw.githubusercontent.com/exeScripter/async/main/py/website_hooker.py'
    # set the file name
    filename = 'Website_Hooker.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("Download complete!")
    print("------------------------------------------------------")

elif option == "5":
    # download the file
    print("------------------------------------------------------")
    print("Downloading 'URL Shortener'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://raw.githubusercontent.com/exeScripter/async/main/py/url_shortener.py'
    # set the file name
    filename = 'URL_Shortener.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("Download complete!")
    print("------------------------------------------------------")

elif option == "6":
    # download the file
    print("------------------------------------------------------")
    print("Downloading 'Średnia'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://raw.githubusercontent.com/exeScripter/async/main/py/srednia.py'
    # set the file name
    filename = 'Średnia.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("Download complete!")
    print("------------------------------------------------------")

elif option == "7":
        # download the file
    print("------------------------------------------------------")
    print("Downloading 'Lech czy Legia?'")
    print("------------------------------------------------------")
    # set the url for the file
    url = 'https://raw.githubusercontent.com/exeScripter/async/main/py/lech_legia.py'
    # set the file name
    filename = 'Lech_czy_Legia.py'
    # download the file
    r = requests.get(url)
    # write the file to the disk
    with open(filename, 'wb') as f:
        f.write(r.content)
    # print that the file has been downloaded
    print("Download complete!")
    print("------------------------------------------------------")

elif option == "8":
    # ask the user for the discord server
    print("------------------------------------------------------")
    print("Please join our Discord server!")
    # set the url for the discord server
    url = 'https://discord.gg/T9rh6VMpSA'
    # open the discord server
    webbrowser.open(url)
    # print that the discord server has been opened
    print("------------------------------------------------------")
    print("Discord server opened!")
    # ask the user if they want to exit
    print("------------------------------------------------------")

# if the user chooses 7, exit the program
elif option == "9":
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
