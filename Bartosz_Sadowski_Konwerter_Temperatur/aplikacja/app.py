# app.py – Aplikacja do konwersji temperatur

from konwerter.temperatura import celsius_na_fahrenheit, fahrenheit_na_celsius

def menu():
    print("\n--- KONWERTER TEMPERATUR ---")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Wyjście")

while True:
    menu()
    wybor = input("Wybierz opcję: ")
    
    if wybor == "1":
        c = float(input("Podaj temperaturę w stopniach Celsjusza: "))
        print(f"{c}°C = {celsius_na_fahrenheit(c):.2f}°F")
    elif wybor == "2":
        f = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
        print(f"{f}°F = {fahrenheit_na_celsius(f):.2f}°C")
    elif wybor == "3":
        print("Zakończono działanie programu.")
        break
    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")
