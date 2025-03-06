tekst = ("Ala ma kota a kot ma Ale")
samogloski = ['a','e', 'i', 'o', 'u', 'y']
licznik = [0,0,0,0,0,0]
print(tekst[5])
for i, s in enumerate(tekst):

    #print(f"{i}, {s}")

    if s.lower() in samogloski:
        print(f"index: {i}, samogloska: {s}")
        licznik[samogloski.index(s.lower())] += 1

for s,l in zip(samogloski,licznik):
     print(f"samogloska: {s} ma {l} wystapien")
#print(licznik)
