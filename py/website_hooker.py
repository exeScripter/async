# Is it possible to make a website with python?

# Import modules
import os
import datetime
import requests
import time

import pyfiglet

# from text create an ASCII art
print(pyfiglet.figlet_format("Website Hooker", font="slant"))

# Print welcome message
print("------------------------------------------------------")
print("Witaj w Website Hookerze!")
print("Zrobione przez: @theAsyncStudios")
print("github.com/theAsyncStudios")
# print the current date and time
print("Aktualny czas i data: " + str(datetime.datetime.now()))
print("------------------------------------------------------")

# set the url for the checker
url = 'https://pastebin.com/raw/4y2GVi0Y'
version = '1.10b'

# check if the script is up to date
r = requests.get(url)
if r.text == version:
    # if the script is up to date, print that
    print("Twoja wersja jest aktualna!")
    print("------------------------------------------------------")
else:
    # if the script is not up to date, print that
    print("Twoja wersja jest nieaktualna!")
    print("Aktualna wersja: " + version)
    print("Najnowsza wersja: " + r.text)
    print("------------------------------------------------------")
    print("Aktualizuję...")
    time.sleep(1.5)
    print("------------------------------------------------------")
    print("Aktualizacja zakończona!")
    print("------------------------------------------------------")

# ask the user for the link too hook
link = str(input("Wpisz/Wklej link do strony: \n "))

# get the website
r = requests.get(link)

# get the html code
html = r.text
# print the html code
print("------------------------------------------------------")
print("Kod HTML: ")
print(html)
print("------------------------------------------------------")


# ask the user if he wants to save the html code
save = str(input("Czy chcesz zapisać Kod HTML? (y/n) \n "))

# if the user wants to save the html code
if save == "y":
    # ask the user for the name of the file
    filename = str(input("Podaj nazwę pliku: \n "))
    # save the html code to the file
    with open(filename, "w") as f:
        f.write(html)
    print("------------------------------------------------------")
    print("Zapisano Kod HTML do pliku: " + filename)
    print("------------------------------------------------------")
    # if the user does not want to save the html code
else:
    # print that the html code was not saved
    print("------------------------------------------------------")
    print("Kod HTML nie został zapisany!")
    print("------------------------------------------------------")

# Prevent the file from closing
input("\n\nPress the enter key to exit.")


