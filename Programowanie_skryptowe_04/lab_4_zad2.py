poczatek =5

def function(n, liczebnosc):
    
    if(liczebnosc < 150):
        print(liczebnosc)
        function(n+1, (liczebnosc-n)*2)
    else:
        print(liczebnosc) # ostatni wytnik poprzekroczeniu
        return liczebnosc

function(1, poczatek)
