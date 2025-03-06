import random

i = random.random

orly  = 0
reszki = 1

liczba_orlow=0
liczba_reszek=0

for x in range(100):
    wylosowana = random.randint(0,1)
    if wylosowana == orly:
        liczba_orlow+=1
    else:
        liczba_reszek+=1

print(f"liczba wylosowanych orlow: {liczba_orlow}, liczba wylosowanycch reszek: {liczba_reszek}")



