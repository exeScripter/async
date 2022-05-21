import string
import random
import os
import time
import sys
import getpass
import requests


## characters to generate password from
alphabets = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list(string.punctuation)
characters = alphabets + numbers + special_characters

## version of the program
version = "1.25b"
## check the version by URL
## the URL has the most recent version
url = "https://pastebin.com/raw/Gh0rjw2D"

# ASCII
import pyfiglet


# Print the ASCII art
print(pyfiglet.figlet_format("Generator Hasel", font="slant"))
def generate_random_password():
    ## Print a welcome message
    print("------------------------------------------------")
    print("Witaj w Generatorze Haseł!")
    print("Autorstwa: Oliwer Noga")
    print("Aktualna Data i Godzina: " + time.strftime("%d/%m/%Y %H:%M:%S")) 
    ## checking is the version is correct
    print("------------------------------------------------")
    try:
        ## check the version by URL
        update = requests.get(url)
        ## check if the version is the same
        if update.text == version:
            print("Używasz najnowszej wersji oprogramowania!")
            print("Aktualna wersja: " + version)
        else:
            print("Jest nowsza wersja oprogramowania!")
            print("Ty używasz wersji: " + version)
            print("Najnowsza wersja to: " + update.text)
            print("Uaktualnij program wpisując: " + os.path.basename(__file__) + " -u")
        expect: input("Naciśnij ENTER aby kontynuować...")
    except:
        print("ERROR: Nie można sprawdzić wersji")
        expect: input("Naciśnij ENTER aby kontynuować...")


    print("------------------------------------------------")

    time.sleep(3.0)

    ## length of password from the user
    password_length = int(input("Jaka ma być długośc twojego hasła? - [np. 29]  "))

    ## number of character types
    alphabets_count = int(input("Ile ma się znajdować liter z alfabetu? - "))
    numbers_count = int(input("Ile cyfr ma się znajdować w twoim haśle? -  "))
    special_characters_count = int(input("Ile znaków specjalnych ma się znajdować w twoim haśle? -  "))

    characters_count = alphabets_count + numbers_count + special_characters_count

    ## check the total length with characters sum count
    ## print not valid if the sum is greater than length
    if characters_count > password_length:
        print("------------------------------------------------")
        print("Nie można wygenerować takiego hasla. Zbyt dużo znaków.")
        print("------------------------------------------------")
        ##  if the sum is greated than length ask the user if he wants to start the program again
        start_again = input("Czy chcesz spróbować ponownie? [T/N] - ")
        print("------------------------------------------------")
        if start_again == "T":
            generate_random_password()
        if start_again == "N":
            exit()
    
    ## intializing the password
    password = []

    ## picking random alphabets
    time.sleep(0.5)
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    ## piking random numbers
    time.sleep(0.5)
    for i in range(numbers_count):
        password.append(random.choice(numbers))
    
    ## picking random special characters
    time.sleep(0.5)
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    ## if the total characters count is less than password length
    ## add random character to make the length equal
    time.sleep(0.5)
    if characters_count < password_length:
        random.shuffle(characters)
        ## pick random character from characters    
        for i in range(password_length - characters_count):
            password.append(random.choice(characters))
        
    ## shuffling the resultant password
    random.shuffle(password)
    ## sleep 1.0s
    time.sleep(1.0)
    ## ask if the user wants to change the name of the file 
    ## if yes, ask for the name and save the password to the file
    ## if no, save the password to the file without asking for the name
    print("------------------------------------------------")
    save_password = input("Czy chcesz zapisać hasło do pliku? [T/N] - ")
    print("------------------------------------------------")
    if save_password == "T":
        file_name = input("Podaj nazwę pliku do którego chcesz zapisać hasło - ")
        file_name = file_name + ".txt"
        file = open(file_name, "w")
        file.write(str(password))
        file.close()


        ## if the file with the exact same name already exists
        ## ask the user if he wants to overwrite the file
        ## if yes, overwrite the file
        ## if no, ask the user if he wants to save the file with a different name
        if os.path.isfile(file_name):
            print("------------------------------------------------")
            overwrite = input("Plik o takiej nazwie już istnieje. Czy chcesz go nadpisać? [T/N] - ")
            if overwrite == "T":
                file = open(file_name, "w")
                file.write("".join(password))
                file.close()
            if overwrite == "N":
                print("------------------------------------------------")
                new_name = input("Ta funkcja nie działa!")
                file.close()

                ## delete the old file
                os.remove(file_name)
        print("------------------------------------------------")
        print("Twoje hasło zostało pomyślnie zapisane do pliku!")
        print("------------------------------------------------")
            
        print("Hasło zapisane do pliku: " + file_name)
        print("------------------------------------------------")


    ## save the generated password to a file
    with open(file_name, "w") as file:
        file.write("".join(password))
        ## sleep for half a second
        time.sleep(0.5)
        ## print a message about the file extension and name
        print("Nazwa pliku: " + file_name)
        print("Rozszerzenie pliku: txt")
        print("Rozmiar pliku: ", os.path.getsize(file_name), "KB")
        ## check where the saved file is located 
        ## then print a message where is it located
        print("Plik został zapisany w: " + os.path.abspath(file_name))

        print("------------------------------------------------")

    


    ## converting the list to string
    ## printing the list
    print("Tutaj znajdziesz swoje hasło: ", "".join(password))
    print("------------------------------------------------")
 
    input("Naciśnij ENTER aby wyjść")
    print("------------------------------------------------")


## invoking the function
generate_random_password()
