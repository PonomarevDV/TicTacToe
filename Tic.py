from colorama import Fore, Back, Style, init
init(autoreset=True)


def draw_board(board):
    for i in range(3):
        colored_row = []
        for cell in board[i]:
            if cell == "X":
                colored_row.append(Fore.RED + cell)
            elif cell == "O":
                colored_row.append(Fore.BLUE + cell)
            else:
                colored_row.append(Back.YELLOW + " ")
        print(' | '.join(colored_row))
        if i < 2:
            print("---------")

def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(player, board, x, y)

def ask_move(player, board):
    x, y = input(f'Player {player} enter x and y coordinates (e.g. 0 0): ').strip().split()
    x, y = int(x), int(y)
    if (0 <= x < 3) and (0 <= y < 3) and (board[x][y] == " "):
        return (x, y)
    else:
        print('Invalid coordinates')
        return ask_move(player, board)

def make_move(player, board, x, y):
    if board[x][y] != " ":
        print('Invalid coordinates')
        return False
    board[x][y] = player
    return True

def check_win(player, board):
    for i in range(3):
        if board[i] == [player, player, player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    while True:
        board = [[' ' for i in range(3)] for _ in range(3)]
        player = "X"

        while True:
            draw_board(board)

            ask_and_make_move(player, board)

            if check_win(player, board):
                print(f'Player {player} wins!')
                break

            has_empty = any(cell == " " for row in board for cell in row)
            if not has_empty:
                print('Draw')
                break

            player = "O" if player == "X" else "X"

        restart = input(f'Player {player} restart? (y/n): ').strip().lower()
        if restart != 'y':
            break

if __name__ == "__main__":
    tic_tac_toe()







