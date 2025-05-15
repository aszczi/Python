import os

print(os.getcwd())
print(__file__)
print(os.path.dirname(__file__))

if(os.path.isabs(__file__)):
    print("sciezka absolutna")
else:
    print("sciezka reletywna")


#tworzenie katalogow
if os.path.exists(os.path.join(os.getcwd(), "test")):
    print ("test istnieje")
else:
    print ("test nie istnieje")
    os.mkdir(os.path.join(os.getcwd(), "test"))


#sprawdzanie zawartosci katalogu

for f in os.listdir(os.getcwd()):
    if os.path.isfile(os.path.join(os.getcwd(), f)):
        print(f"{f} jest plikiem")
    elif os.path.isdir(os.path.join(os.getcwd(), f)):
        print(f"{f} jest katalogiem")
    else:
        print("inne")

#usuwa katalog
#os.rmdir(os.path.join(os.getcwd(), "test"))
#usuwa plik
#os.remove(os.path.join(os.getcwd(), "test.py"))

print(os.system("ipconfig"))
print(os.getlogin())
#otworzy notepad
os.system("notepad")

os.mkdir("test", 777)

#shutil.copy()
