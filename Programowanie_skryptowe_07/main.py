import sys
from random import randint


'''Napisz program, który generuje losową tablicę dwuwymiarową n×n (rozmiar n powinien być ustalany przez użytkownika z zakresu od 10 do 20), wypełniona
losowymi cyframi od 0 do 9. Program powinien wyszukać wszystkie wystapienia czterech takich samych cyfr ułożonych obok siebie w kolumnie, wierszu lub po przekątnej.
Program powinien wyświetlić na ekranie wygenerowana tablice, przy czym znalezione "czwórki" powinny być wyraźnie zaznaczone 
(np. otoczone nawiasami, oznaczone gwiazdka ’*’ lub innym czytelnym symbolem).
Program powinien umożliwiać wielokrotne przeprowadzenie symulacji (użytkownik decyduje, kiedy zakończyć działanie programu).
Program powinien zawierać co najmniej nastepujace funkcje:
• generate_random_grid(n) – tworzy losowa tablice o wymiarach n × n.
• display_grid(grid) – wyświetla tablice na ekranie w czytelnej postaci, z zaznaczonymi „czwórkami”.
• find_fours(grid) – wyszukuje wszystkie wystapienia czwórek jednakowych
cyfr ułożonych poziomo, pionowo oraz ukośnie i zwraca ich współrzedne.
• simulation() – umożliwia wielokrotne przeprowadzenie symulacji według decyzji użytkownika.
Program powinien być czytelny oraz wygodny w użytkowaniu'''


def generate_random_grid(n):
    grid = [[randint(0, 9) for _ in range(n)] for _ in range(n)]
    return grid



def display_grid(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end = "     ")
        print("\n")


def find_fours(grid):
    n = len(grid)
    fours = []

    #wiersze
    for i in range(n):
        for j in range(n - 3):
            if grid[i][j] == grid[i][j + 1] == grid[i][j + 2] == grid[i][j + 3]:
                fours.append([(i, j), (i, j + 1), (i, j + 2), (i, j + 3)])

    #kolumny
    for i in range(n - 3):
        for j in range(n):
            if grid[i][j] == grid[i + 1][j] == grid[i + 2][j] == grid[i + 3][j]:
                fours.append([(i, j), (i + 1, j), (i + 2, j), (i + 3, j)])

    #przekatne
    for i in range(n - 3):
        for j in range(n - 3):
            if grid[i][j] == grid[i + 1][j + 1] == grid[i + 2][j + 2] == grid[i + 3][j + 3]:
                fours.append([(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)])

            if grid[i][j + 3] == grid[i + 1][j + 2] == grid[i + 2][j + 1] == grid[i + 3][j]:
                fours.append([(i, j + 3), (i + 1, j + 2), (i + 2, j + 1), (i + 3, j)])

    return fours


def add_stars(grid, fours):
    pass

def simulation():

    new_grid = generate_random_grid(n_int)
    display_grid(new_grid)
    fours = find_fours(new_grid)
    print(fours)
    if len(fours) != 0:
        for x, y in fours[0]:
            new_grid[x][y] = str(new_grid[x][y]) + "*"
    display_grid(new_grid)



if __name__ == '__main__':
    grid = []
    for arg in sys.argv:
        n = arg
    n_int = int(n)
    print(f"n = {n}\n")

    while( n_int < 10 or n_int > 20):
        n_int = input("enter a value in range 10-20")

    simulation()


