wyniki = [5,7,3,2,7,9,2,5,4]
wyniki.sort()
wyniki.reverse()

while True:
    i = input('wpisz jaka operacje chcesz wykonac 1- dodanie wyniku, 2- usuniecie wyniku, 3- sortowanie wynikow, 4- wyswietlanie wynikow, 5- wyjscie z programu \n')
    
    if i == "1":
        nowy_wynik = int(input('podaj nowy wynik: '))
        wyniki.append(nowy_wynik) 
        
    elif i == "2":
        wynik_do_usuniecia = int(input('podaj wynik do usuniecia: ')) 
        if wynik_do_usuniecia in wyniki:
            wyniki.remove(wynik_do_usuniecia)
        else:
            print("Podany wynik nie istnieje na liście.")
            
    elif i == "3":
        wyniki.sort()
        wyniki.reverse()
        
    elif i == "4":
        wyniki.sort()
        wyniki.reverse()
        k = 0
        print("oto najlepsze 5 wynikow: ")
        for wynik in wyniki:
            if k < 5:
                print(wynik)
                k += 1
                
    elif i == "5":
        print("Koniec programu.")
        break
        
    else:
        print("Nieprawidłowy wybór. Wybierz opcję od 1 do 5.")