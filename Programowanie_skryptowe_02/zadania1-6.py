import os
import sys
#zrobic zadania od 1 do 9 zadania i wrzucic na moodle
# 10 i 11 dla chetnych
'''
7. Napisz program, który będzie przechowywał informacje o studentach w postaci słownika, każdy student powinien mieć przypisane imię, nazwisko, listę oceny.
   Dane przechowuj w pliku tekstowym. Program powinien zawierać następujące funkcje: zapisanie danych do pliku i odczyt danych z pliku. 
   Zademonstruj działanie programu poprzez zapis danych do pliku i odczyt ich. 
 
8. Napisz program, który symuluje prostą książkę telefoniczną działającą na podstawie danych zapisanych w pliku CSV.Program powinien umożliwiać użytkownikowi:
      a. Dodawanie nowych kontaktów (imię, nazwisko, numer telefonu),
       b. Wyświetlanie wszystkich zapisanych kontaktów, 
        c. Usuwanie wybranych kontaktów z książki telefonicznej. Wszystkie zmiany (dodawanie, usuwanie kontaktów) muszą być trwale zapisywane w pliku,
           tak aby dane były dostępne po ponownym uruchomieniu programu. Zaprezentuj przykładowe działanie programu. 
           
9. Zapoznaj się z modułem CSV i przebuduj program z zadania 8 tak aby do zapisu i odczytu wykorzystywał metody z modułu CSV
    szczegóły: https://www.google.com/url?q=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcsv.html 
'''

#zad 1
def writeToFile():
    text = input("Podaj tekst : ")
    with open("plik.txt", "w") as file:
        file.write(text)
    file = open("plik.bin", "wb")
    binary_text = text.encode("utf-8")
    file.write(binary_text)
    file.close()

#zad 2
def readFile(file_name):
    text = ""
    if ".bin" in file_name or ".dat" in file_name:
        file = open("plik.bin", "rb")
        binary_text = file.read()
        text = binary_text.decode("utf-8")
        print(text)
        file.close()
    elif ".txt" in file_name or ".csv" in file_name:
        with open(file_name, "r") as file:
            text = file.read()
            print(text)
    else:
        print("zly format pliku")

#zad 3
def readWriteFile(file_name, text):
    if os.path.exists(file_name):
            with open(file_name, "a") as file:
              file.write(text)
    else:
        with open(file_name, "w") as file:
            file.write(text)

#zad 4
def readingNumbers():
    while True:
        try:
                number = int(input('Podaj liczbe (nie litere): '))
                break
        except:
            print("bledna wartosc, podaj ponownie")

#zad 5
def readingOddEvenNumbers():
    while True:
        try:
            number = int(input('Podaj liczbe: '))
            if number == 0:
                break
            if number%2 == 0:
                readWriteFile("even.txt", f"{number} ")
            else:
                readWriteFile("odd.txt", f"{number} ")

        except:
            print("bledna wartosc, podaj ponownie")

#zad 6
def openingFileWithFinally(file_name):
    f = None
    try:
        f =open(file_name, "r")
        print(f.read())
    except FileNotFoundError as ef:
        print(ef)
    finally:
        if f is not None:
            f.close()


if __name__ == "__main__":
  #  writeToFile()
  #  readFile("plik.bin")

  #  readingNumbers()
  #  readWriteFile("plik.txt", "nowy tekst ")
    readingOddEvenNumbers()
    openingFileWithFinally("plik.txt")
