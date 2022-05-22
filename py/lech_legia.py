# Decide which one of these football clubs is better than the other one
# The football clubs are:
# 1. Legia Warszawa 
# 2. Lech Poznan

# The program should ask the user to enter the name of the first football club

# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import datetime
import time
import pyfiglet

# Print the text in ASCII
print(pyfiglet.figlet_format("Lech czy Legia?", font="slant"))

# Print welcome message
print("------------------------------------------------------")
print("Witaj w tym programie, zdecydujemy który klub piłkarski jest lepszy!")
print("Wykonane przez: @theAsyncStudios")
print("github.com/theAsyncStudios")
# print the current date and time
print("Aktualna data i godzina: " + str(datetime.datetime.now()))
print("------------------------------------------------------")

# the Wikipedia page with the football clubs
url = "https://pl.wikipedia.org/wiki/Legia_Warszawa_(pi%C5%82ka_no%C5%BCna)"
url1 = "https://pl.wikipedia.org/wiki/Lech_Pozna%C5%84"

# get the content of the page
page = requests.get(url)
page1 = requests.get(url1)

# analize which one of the two football clubs is better
if page.text.find("Lech") > page1.text.find("Lech"):
    print("Lech jest lepszy!")
    print("KOLEJORZ JEST ZAWSZE LEPSZY")
    print("------------------------------------------------------")
else:
    print("Legia jest lepsza!")
    print("------------------------------------------------------")

# exit the program
input("Naciśnij ENTER aby zakończyć...")

