
# Importing necessary libraries
import pyshorteners
import os
import sys
import datetime
import pyfiglet 

# Print the ASCII art
print(pyfiglet.figlet_format("URL Shortener", font="slant"))

# Print welcome message
print("------------------------------------------------------")
print("Witaj w URL Shortenerze!")
print("Zrobione przez: @theAsyncStudios")
print("github.com/theAsyncStudios")
# print the current date and time
print("Current date and time: " + str(datetime.datetime.now()))
print("------------------------------------------------------")

s = pyshorteners.Shortener()

# ask user for the url
url = input("Podaj URL który chcesz skrócić:  ")
print("------------------------------------------------------")
print("Oto twój skrócony link: " + s.tinyurl.short(url))
print("------------------------------------------------------")
# Prevent the program from closing
input("Naciśnij ENTER aby wyjść")

