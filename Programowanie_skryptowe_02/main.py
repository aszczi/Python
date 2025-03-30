import os
import sys
import csv

# zad 1
def writeToFile():
    text = input("Podaj tekst : ")
    with open("plik.txt", "w") as file:
        file.write(text)
    file = open("plik.bin", "wb")
    binary_text = text.encode("utf-8")
    file.write(binary_text)
    file.close()


# zad 2
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


# zad 3
def readWriteFile(file_name, text):
    if os.path.exists(file_name):
        with open(file_name, "a") as file:
            file.write(text)
    else:
        with open(file_name, "w") as file:
            file.write(text)


# zad 4
def readingNumbers():
    while True:
        try:
            number = int(input('Podaj liczbe (nie litere): '))
            break
        except:
            print("bledna wartosc, podaj ponownie")


# zad 5
def readingOddEvenNumbers():
    while True:
        try:
            number = int(input('Podaj liczbe: '))
            if number == 0:
                break
            if number % 2 == 0:
                readWriteFile("even.txt", f"{number} ")
            else:
                readWriteFile("odd.txt", f"{number} ")

        except:
            print("bledna wartosc, podaj ponownie")


# zad 6
def openingFileWithFinally(file_name):
    f = None
    try:
        f = open(file_name, "r")
        print(f.read())
    except FileNotFoundError as ef:
        print(ef)
    finally:
        if f is not None:
            f.close()


# zad 7
def informacje_o_studentach():
    studenci = {}
    indeks = 0

    try:
        with open("studenci.txt", 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                dane = line.split(' ')
                if len(dane) >= 3:
                    imie = dane[0]
                    nazwisko = dane[1]
                    oceny = dane[2].split(',')
                    studenci[indeks] = {
                        'imię': imie,
                        'nazwisko': nazwisko,
                        'oceny': oceny
                    }
                    indeks += 1


    except FileNotFoundError:
        print("Plik nie istnieje - tworzę nową bazę danych.")

    i = int(input(
        '\nWybierz opcję:\n1. Zapisz nowych studentów do pliku\n2. Wyświetl listę studentów\n'))

    if i == 1:
        print("\nWpisz dane studentów. Wpisz 0 jako imię, aby zakończyć.\n")
        while True:
            imie = input('Podaj imię studenta: ')
            if imie == '0':
                break
            nazwisko = input('Podaj nazwisko studenta: ')
            oceny = input('Podaj oceny studenta rozdzielone przecinkami: ')

            studenci[indeks] = {
                'imię': imie,
                'nazwisko': nazwisko,
                'oceny': [o.strip() for o in oceny.split(',') if o.strip()]
            }
            indeks += 1

        with open("studenci.txt", 'w') as file:
            for dane in studenci.values():
                line = f"{dane['imię']} {dane['nazwisko']} {','.join(dane['oceny'])}\n"
                file.write(line)

        print("Dane zapisane do pliku.")

    elif i == 2:
        if not studenci:
            print("Brak studentów w bazie danych.")
        else:
            print("\nLista studentów:")
            for dane in studenci.values():
                print(f"Imię: {dane['imię']}")
                print(f"Nazwisko: {dane['nazwisko']}")
                print(f"Oceny: {', '.join(dane['oceny'])}\n")


# zad 8
def ksiazka_telefoniczna():
    plik_csv = "ksiazka_telefoniczna_zad8.csv"

    if not os.path.exists(plik_csv):
        with open(plik_csv, 'w') as file:
            text = f"Imie,Nazwisko,Numer\n"
            file.write(text)

    while True:
        print("1. Dodaj kontakt")
        print("2. Wyświetl kontakty")
        print("3. Usuń kontakt")
        print("4. Zakończ")
        opcja = int(input("Wybierz opcję: "))

        if opcja == 1:
            imie = input("Imię: ")
            nazwisko = input("Nazwisko: ")
            numer = input("Numer telefonu: ")
            with open(plik_csv, 'a') as file:
                text = f"{imie},{nazwisko},{numer}\n"
                file.write(text)
            print("Kontakt dodany.")

        elif opcja == 2:
            try:
                with open(plik_csv, 'r') as file:
                    linie = file.read().splitlines()
            except FileNotFoundError:
                print("Plik nie istnieje!")
                linie = []

            if not linie or len(linie) < 2:
                print("Brak kontaktów do wyświetlenia.")
            else:
                for linia in linie[1:]:
                    dane = linia.split(",")
                    if len(dane) < 3:
                        continue
                    imie, nazwisko, numer = dane[0], dane[1], dane[2]
                    print(f"Imie: {imie}")
                    print(f"Nazwisko: {nazwisko}")
                    print(f"Numer: {numer}\n")

        elif opcja == 3:
            try:
                with open(plik_csv, 'r') as file:
                    linie = file.read().splitlines()
            except FileNotFoundError:
                print("Plik nie istnieje!")
                linie = []

            if not linie:
                print("Brak danych w pliku.")
            else:
                naglowek = linie[0]
                kontakty = linie[1:]

                if not kontakty:
                    print("Brak kontaktów do usunięcia.")
                else:
                    # Wyświetlenie kontaktów
                    for i, linia in enumerate(kontakty, start=1):
                        dane = linia.split(",")
                        if len(dane) >= 3:
                            print(f"{i}. {dane[0]} {dane[1]} - {dane[2]}")
                        else:
                            print(f"{i}. Format danych jest nieprawidłowy: {linia}")

                    try:
                        nr = int(input("Podaj numer kontaktu do usunięcia: "))
                        if 1 <= nr <= len(kontakty):
                            usuniety = kontakty.pop(nr - 1)

                            with open(plik_csv, 'w') as file:
                                file.write(naglowek + "\n")
                                for lin in kontakty:
                                    file.write(lin + "\n")
                            print(f"Usunięto kontakt: {usuniety}")
                        else:
                            print("Nieprawidłowy numer.")
                    except ValueError:
                        print("Wprowadzono nieprawidłową wartość!")

        elif opcja == 4:
            print("Zakończono działanie programu.")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")


#zad 9
def ksiazka_telefoniczna_moduly_csv():
    plik_csv = "ksiazka_telefoniczna_zad9.csv"

    if not os.path.exists(plik_csv):
        with open(plik_csv, 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Imie", "Nazwisko", "Numer"])

    while True:
        print("1. Dodaj kontakt")
        print("2. Wyświetl kontakty")
        print("3. Usuń kontakt")
        print("4. Zakończ")
        opcja = int(input("Wybierz opcję: "))

        if opcja == 1:
            imie = input("Imię: ")
            nazwisko = input("Nazwisko: ")
            numer = input("Numer telefonu: ")
            with open(plik_csv, 'a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow([imie, nazwisko, numer])
            print("Kontakt dodany.")

        elif opcja == 2:
            with open(plik_csv, 'r', newline="") as file:
                reader = csv.reader(file)
                next(reader)  # pomijamy nagłówek
                kontakty = list(reader)
            if kontakty:
                for i, kontakt in enumerate(kontakty, start=1):
                    print(f"{i}. {kontakt[0]} {kontakt[1]} - {kontakt[2]}")
            else:
                print("Brak kontaktów.")

        elif opcja == 3:
            with open(plik_csv, 'r', newline="") as file:
                wiersze = list(csv.reader(file))
            naglowek, kontakty = wiersze[0], wiersze[1:]
            if kontakty:
                for i, kontakt in enumerate(kontakty, start=1):
                    print(f"{i}. {kontakt[0]} {kontakt[1]} - {kontakt[2]}")
                try:
                    numer_do_usuniecia = int(input("Podaj numer kontaktu do usunięcia: "))
                    if 1 <= numer_do_usuniecia <= len(kontakty):
                        usuniety = kontakty.pop(numer_do_usuniecia - 1)
                        with open(plik_csv, 'w', newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(naglowek)
                            writer.writerows(kontakty)
                        print(f"Usunięto: {usuniety[0]} {usuniety[1]} - {usuniety[2]}")
                    else:
                        print("Nieprawidłowy numer.")
                except ValueError:
                    print("Wprowadzono nieprawidłową wartość!")
            else:
                print("Brak kontaktów do usunięcia.")

        elif opcja == 4:
            print("Zakończono działanie programu.")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")


if __name__ == "__main__":
    #testowanie rozwiązań
#zad 1
    writeToFile()
#zad 2
    readFile("plik.bin")
#zad 3
    readingNumbers()
#zad 4
    readWriteFile("plik.txt", "nowy tekst ")
#zad 5
    readingOddEvenNumbers()
#zad 6
    openingFileWithFinally("plik.txt")
#zad 7
    informacje_o_studentach()
#zad 8
    ksiazka_telefoniczna()
#zad 9
    ksiazka_telefoniczna_moduly_csv()
