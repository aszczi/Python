def szyfrowanie():
    tekst = input('podaj tekst do zaszyfrowania: \n')
    liczba = int(input("podaj przesuniecie: \n"))
    tekst_do_wyswietlenia = ""
    znaki = [znak for znak in tekst]
    for znak in znaki:
        kod_ascii = ord(znak) + liczba
        znak = chr(kod_ascii)
        tekst_do_wyswietlenia =  tekst_do_wyswietlenia + znak
    print(tekst_do_wyswietlenia)
     
    
def deszyfrowanie():
    tekst = input('podaj tekst do odszyfrowania: \n')
    liczba = int(input("podaj przesuniecie: \n"))
    tekst_do_wyswietlenia = ""
    znaki = [znak for znak in tekst]
    for znak in znaki:
        kod_ascii = ord(znak) - liczba
        znak = chr(kod_ascii)
        tekst_do_wyswietlenia =  tekst_do_wyswietlenia + znak
    print(tekst_do_wyswietlenia)
    

    
szyfrowanie()    
deszyfrowanie()
