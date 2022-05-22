# Make a program that asks user for his grades in 3 subjects then predict how many % 
# he will get in the final exam.

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
import datetime
import time
import pyfiglet

# Print the text in ASCII
print(pyfiglet.figlet_format("Oblicz srednia", font="slant"))

# Print welcome message
print("------------------------------------------------------")
print("Witaj w tym programie obliczysz swoją średnią!")
print("Wykonane przez: @theAsyncStudios")
print("github.com/theAsyncStudios")
# print the current date and time
print("Aktualna data i godzina: " + str(datetime.datetime.now()))
print("------------------------------------------------------")

# ask the user for the grades in all the avaible subjects
print("Podaj swoje oceny w wszystkich dostępnych przedmiotach:")
# set the variables
print("------------------------------------------------------")
religion = float(input("Religia: "))
polish = float(input("Język polski: "))
english = float(input("Język angielski: "))
deutsch = float(input("Język niemiecki: "))
french = float(input("Język francuski: "))
philosophy = float(input("Filozofia: "))
history = float(input("Historia: "))
physics = float(input("Fizyka: "))
chemistry = float(input("Chemia: "))
geography = float(input("Geografia: "))
informatics = float(input("Informatyka: "))
pe = float(input("Wychowanie fizyczne: "))
edb = float(input("Edukacja dla bezpieczeństwa: "))
biology = float(input("Biologia: "))
maths = float(input("Matematyka: "))
pinformatics = float(input("Podstawy informatyki: "))
bhp = float(input("Bezpieczeństwo i higiena pracy: "))

# calculate the average
average = (religion + polish + english + french + philosophy + history + physics + chemistry + geography + informatics + pe + edb + biology + maths + pinformatics + bhp) / 16

# print the average
print("------------------------------------------------------")
print("Twoja średnia wynosi: " + str(average))
print("------------------------------------------------------")

# if the average is less than 4.5, print that
if average < 4.5:
    print("Twoja średnia jest na dobrym bądź słabym poziomie!")
    print("------------------------------------------------------")

# if the average is above 4.75 print that
if average > 4.75:
    print("Twoja średnia jest powyżej 4.75!")
    print("Gratulacje masz czerwony pasek!")
    print("------------------------------------------------------")
# if the average is equal to 6.00 print that
elif average == 6.00:
    print("Twoja średnia jest równa 6.00!")
    print("Jesteś kurwa kujonem!")
    print("------------------------------------------------------")

# exit the program
input("Naciśnij ENTER aby zakończyć...")

