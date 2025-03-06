while True:
    liczba = int(input("podaj liczbe: "))
    czy_nie_pierwsza  = False
    if liczba >= 1:
        #sprawdzamy czy liczba jest liczba pierwszą
        for i in range(2, liczba+1):
            if liczba % i == 0:
                czy_nie_pierwsza = True
                break

        if czy_nie_pierwsza:
            print("podana liczba nie jest liczba pierwsza")
        else:
            print("podana liczba jest liczba pierwsza")

    else:
        break

## cos tu nie dzilaa xdd