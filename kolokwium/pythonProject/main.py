#zadanie 2
import random

def utworz_i_wstaw(rozmiar_listy, cztery_zmiennoprzecinkowe):
    nowa_lista = []
    for floacik in range(rozmiar_listy):
        nowa_lista.append(random.uniform(1,10))
    #mamy dodane liczby zmiennoprzecinkowych

    nowa_lista.sort()
    print(nowa_lista)

    for _ in range(4):
        for k in range(len(nowa_lista)):
            if k < (len(nowa_lista) - 1):
                if cztery_zmiennoprzecinkowe[i] < nowa_lista[0]:
                    nowa_lista.insert(0,cztery_zmiennoprzecinkowe[i])
                    break
                elif nowa_lista[k] <= cztery_zmiennoprzecinkowe[i] <= nowa_lista[k + 1]:
                    nowa_lista.insert(k+1, cztery_zmiennoprzecinkowe[i])
                    break
            elif k == (len(nowa_lista) - 1):
                if nowa_lista[k] > cztery_zmiennoprzecinkowe[i]:
                    nowa_lista.insert(k,cztery_zmiennoprzecinkowe[i])
                else:
                    nowa_lista.insert(k+1, cztery_zmiennoprzecinkowe[i])
    #po tym kroku mamy dodane nasze liczby podane przez uzytkownika
    return nowa_lista



if __name__ == '__main__':
    rozmiar = int(input("podaj rozmiar listy: "))
    l_zmiennoprzecinkowe = input("podaj 4 liczby zmiennoprzecinkowe (rozdzielone spacjami) :")
    liczby_zmiennoprzecinkowe = l_zmiennoprzecinkowe.split()
    zmiennoprzecinkowe_float = []

    for i in range(4):
        zmiennoprzecinkowe_float.append(float(liczby_zmiennoprzecinkowe[i]))
    print(zmiennoprzecinkowe_float)

    #wywolanie funkcji
    print(utworz_i_wstaw(rozmiar, zmiennoprzecinkowe_float))

