import pyfiglet
import datetime
import os
import sys
import time

# Print the ASCII art
print(pyfiglet.figlet_format("BMI Calculator", font="slant"))

# Print welcome message
print("------------------------------------------------------")
print("Witaj w Kalkulatorze BMI!")
print("Zrobione przez: @theAsyncStudios")
print("github.com/theAsyncStudios")
# print the current date and time
print("Aktualna data i godzina: " + str(datetime.datetime.now()))
print("------------------------------------------------------")



h = float(input("Podaj wzrost w metrach: "))
print("------------------------------------------------------")
w = float(input("Podaj wagę w kg: "))



time.sleep(2)
BMI = w / (h * h)
print("------------------------------------------------------")
print ("Twoje BMI wynosi: ", BMI)
print("------------------------------------------------------")

if (BMI>0):
    if (BMI<=16):
        print("Masz dużą niedowagę")
    elif (BMI<18.5):
        print ("Niedowaga")
    elif (BMI<25):
        print ("Waga prawidłowa")
    elif (BMI<30):
        print ("Nadwaga")
    else:
        print ("Otyłość")
else:
    print("Błędne dane")
print("------------------------------------------------------")

# Prevent the program from closing
input("Naciśnij ENTER aby wyjść")

