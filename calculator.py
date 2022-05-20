import time as t

# ta funkcja dodaje dwie liczby
def add(x, y):
    return x + y

# ta funkcja odejmuje dwie liczby
def subtract(x, y):
    return x - y

# ta funkcja mnozy dwie liczby
def multiply(x, y):
    return x * y

# ta funkcja dzieli dwie liczby
def divide(x, y):
    return x / y

# ta funkcja oblicza reszte z dzielenia
def mod(x, y):
    return x % y

# ta funkcja oblicza procent z liczby
def percent(x):
    return x / 100

# ta funkcja oblicza liczbę do potęgi 
def power(x, y):
    return x ** y

# ta funckja oblicza pierwiastek kwadratowy z liczby
def sqrt(x):
    return x ** 0.5

# ta funkcja oblicza pierwiastek sześcienny z liczby
def cbrt(x):
    return x ** (1/3)
# ta funkcja oblicza logarytm naturalny z liczby
def log(x):
    return x ** (1/2)

# ta funkcja oblicza sinus z liczby
def sin(x):
    return x ** (1/2)
# ta funkcja oblicza cosinus z liczby
def cos(x):
    return x ** (1/2)
# ta funkcja oblicza tangens z liczby
def tan(x):
    return x ** (1/2)

# ASCII
import pyfiglet


# Print the ASCII art
print(pyfiglet.figlet_format("Kalkulator", font="slant"))

print("------------------------------------------------")
print("Witaj w kalkulatorze!")
print("Zrobione przez: @theAsyncStudios")
print("github.com/theAsyncStudios")
print("Aktualna Data i Godzina: " + t.strftime("%d/%m/%Y %H:%M:%S"))
print("------------------------------------------------")
t.sleep(1.5)
print("Wybierz działanie: ")
print("------------------------------------------------")
t.sleep(1.5)
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Reszta z dzielenia")
print("6. Procent")
print("7. Potęgowanie")
print("8. Pierwiastek kwadratowy")
print("9. Pierwiastek sześcienny")
print("10. Logarytm naturalny")
t.sleep(1.5)
print("--------------- BARDZIEJ ZAAWANSOWANE ----------------")
print("11. Sinus")
print("12. Cosinus")
print("13. Tangens")
print("------------------------------------------------")
t.sleep(1.5)
print("14. Wyjście")
print("------------------------------------------------")

while True:
    # weź wybór użytkownika
    t.sleep(1.5)
    choice = input("Wybierz działanie (1-14): ")

    # sprawdź czy wybór jest jednym z poniższych
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1, num2))

        elif choice == '6':
            print(num1, "%", num2, "=", percent(num1))

        elif choice == '7':
            print(num1, "^", num2, "=", power(num1, num2))

        elif choice == '8':
            print(num1, "sqrt", "=", sqrt(num1))

        elif choice == '9':
            print(num1, "cbrt", "=", cbrt(num1))

        elif choice == '10':
            print(num1, "log", "=", log(num1))
        
        elif choice == '11':
            print(num1, "sin", "=", sin(num1))
        
        elif choice == '12':
            print(num1, "cos", "=", cos(num1))
        
        elif choice == '13':
            print(num1, "tan", "=", tan(num1))

        elif choice == '14':
            print("------------------------------------------------")
            print("Dziękuję za skorzystanie z kalkulatora!")
            print("------------------------------------------------")
            input("Naciśnij ENTER aby zakończyć program")
            print("------------------------------------------------")
            break

        # sprawdź czy użytkownik chce kontynuować
        # wyświetl pusty wiersz
        print("------------------------------------------------")
        next_calculation = input("Wykonać następną kalkulację? [t/n]: ")
        print("------------------------------------------------")
        if next_calculation == "n":
            break
        if next_calculation == "t":
            continue
        else:
            break

    else:
        # jeśli wybór jest niepoprawny to wyświetl komunikat
        print("------------------------------------------------")
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
        print("------------------------------------------------")


