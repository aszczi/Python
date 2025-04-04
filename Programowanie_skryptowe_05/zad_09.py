
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
    iterations = 0
    while(continue_game and iterations < 9):
        iterations += 1
        i = int(input("Enter the field\n"))
        column = (i-1)%3
        row = (i-1)//3
        if(GamerO):
            GamerX = True
            GamerO = False
            X_or_O = "O"
        else:
            GamerX = False
            GamerO = True
            X_or_O = "X"

        game_board[row][column] = X_or_O

        print(game_board[0])
        print(game_board[1])
        print(game_board[2])


        #rows
        if (game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X"):
            print("X wins")
            continue_game = False
        elif (game_board[1][0]== "X" and game_board[1][1]== "X" and game_board[1][2] == "X"):
            print("X wins")
            continue_game = False
        elif (game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X"):
            print("X wins")
            continue_game = False
            # columns
        elif (game_board[0][0]  == "X" and game_board[1][0] == "X" and game_board[2][0] == "X"):
            print("X wins")
            continue_game = False
        elif (game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X"):
            print("X wins")
            continue_game = False
        elif (game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X"):
            print("X wins")
            continue_game = False
            # crosses
        elif (game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X"):
            print("X wins")
            continue_game = False
        elif (game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X"):
            print("X wins")
            continue_game = False
        #rows
        elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
            print("O wins")
            continue_game = False
        elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
            print("O wins")
            continue_game = False
        elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
            print("O wins")
            continue_game = False
        # columns
        elif game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
            print("O wins")
            continue_game = False
        elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
            print("O wins")
            continue_game = False
        elif game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
            print("O wins")
            continue_game = False
        #crosses
        elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
            print("O wins")
            continue_game = False
        elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
            print("O wins")
            continue_game = False

    print("Game over")