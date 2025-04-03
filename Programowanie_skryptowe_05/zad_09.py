
'''Napisz grę “kółko i krzyżyk”, gra powinna działać w następujący sposób: do stworzenia planszy 3x3 wykorzystaj listę list. Stwórz dwa tryby rozgrywki:
    - Gracz z graczem - gracze na przemian umieszczają swoje znaczniki na planszy
    - Gracz z komputerem - w trybie gracz z komputerem ruch komputera może być losowany na podstawie wolnych miejsc na planszy.
 Po każdym ruchu sprawdzaj czy któryś z graczy wygrał, jeżeli tak to zakończ rozgrywkę i poinformuj użytkownika.
 W przypadku braku dostępnych ruchów lub wygranej poinformuj o remisie. Gra powinna zapamiętywać wyniki rozgrywanych rozgrywek. Po każdej rozgrywce przedstaw statystyki wygranych. '''



def kolko_i_krzyzyk():
    continue_game = True
    game_board_show = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    game_board= [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    print("Before you start: please pick a number to put your symbol")
    print("The board looks like this: \n")
    print(game_board_show[0])
    print(game_board_show[1])
    print(game_board_show[2])
    GamerX = True
    GamerO = False
    X_or_O = ""
    while(continue_game):
        i = int(input("podaj pole"))
        column = i%3
        row = (i-1)//3
        if(GamerO):
            GamerX = True
            GamerO = False
            X_or_O = "O"
        else:
            GamerX = False
            GamerO = True
            X_or_O = "X"

        gameboard[row][column] = X_or_O

        print(game_board[0])
        print(game_board[1])
        print(game_board[2])

        if(game_board[0][0] == game_board[0][1] && game_board[0][0] == game_board[0][2]):
            continue_game =False
        #TODO dokonczyc

