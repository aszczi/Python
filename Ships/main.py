import random

def set_ships(board_size=10, num_ships=5):
    ships = set()
    while len(ships) < num_ships:
        row = random.randint(0, board_size - 1)
        col = random.randint(0, board_size - 1)
        print(row,col)
        ships.add((row, col))
    return ships


def print_board(board):
    print("   A B C D E F G H I J")
    for i, row in enumerate(board, 1):
        print(f"{i:2} {' '.join(row)}")
    print()


def game(board_size=10, num_ships=5):
    # Initialize the board
    board = [["."] * board_size for _ in range(board_size)]
    ships = set_ships(board_size, num_ships)
    attempts = 0
    hits = 0
    columns = "ABCDEFGHIJ"

    print("Let's play a game!")
    print_board(board)

    while hits < num_ships:
        try:
            move = input(f"Enter your move (e.g. A1 ): ").upper().strip()
            if len(move) < 2 or move[0] not in columns or not move[1:].isdigit():
                raise ValueError
            col = columns.index(move[0])
            row = int(move[1:]) - 1
            if row < 0 or row >= board_size or col < 0 or col >= board_size:
                raise IndexError
            
            if (row, col) in ships:
                board[row][col] = "X"
                ships.remove((row, col))
                hits += 1
            elif board[row][col] == "O" or board[row][col] == "X":
                print("Already targeted this location. Try again.")
            else:
                board[row][col] = "O"
            attempts += 1
            print_board(board)
        except ValueError:
            print("You have to enter a column letter followed by a row number e.g. A1")
        except IndexError:
            print(f"Please enter a row between 1 and {board_size} and a column between A and J.")

    print(f"Congratulations! You sunk all the ships in {attempts} moves.")


game()
