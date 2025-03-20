import os
import sys
#zrobic zadania od 1 do 9 zadania i wrzucic na moodle
# 10 i 11 dla chetnych


''' Napisz funkcję, która przyjmuje dwa argumenty: nazwę pliku oraz dane do zapisania. Funkcja powinna sprawdzić,
 czy plik o podanej nazwie istnieje. Jeżeli plik istnieje, funkcja powinna dopisać przekazane dane na końcu pliku. Jeżeli plik nie istnieje,
 funkcja powinna go stworzyć i zapisać w nim przekazane dane. przetestuj działanie funkcji na przykładowych danych. nie używaj do tego modułu os lub sys '''

def writeToFile():
    text = input("Podaj tekst : ")
    with open("plik.txt", "w") as file:
        file.write(text)
    file = open("plik.bin", "wb")
    binary_text = text.encode("utf-8")
    file.write(binary_text)
    file.close()

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

def readWriteFile(file_name, text):
    if os.path.exists(file_name):
            with open(file_name, "a") as file:
              file.write(text)
    else:
        with open(file_name, "w") as file:
            file.write(text)

def readingNumbers():
    while True:
        try:
                number = int(input('Podaj liczbe (nie litere): '))
                break
        except:
            print("bledna wartosc, podaj ponownie")


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
