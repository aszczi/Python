'''. Stwórz program “Zgadnij jakie to słowo”. Program ma działać w następujący sposób: program powinien przechowywać kilka słów do odgadnięcia wraz z krótkim opisem.
 Na początku rozgrywki program losuje słowo, następnie każda litera ze sowa jest zamieniania na znak podłogi “_” i wyświetla użytkownikowi.
 Zadaniem gracz jest odgadnięcie słowa, gracz może podawać po jednym literze i jeżeli będzie występować dana litera w słowie to wyświetl w odpowiednim miejscu.
 Gracz może podać całe słowo sprawdź czy podane słowo zgadza się z zagadką, jeżeli tak to poinformuj o poprawnym odgadnięciu, jeżeli nie to poinformuj o dalszych próbach.
 Program powinien zliczać po którym kroku gracz odgadł szukane słowo.'''
from zad_06 import guess_word


def print_hi(name):

    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    guess_word()