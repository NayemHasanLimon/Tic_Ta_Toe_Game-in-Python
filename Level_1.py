
# draw board
def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw(board):
    return " " not in board

def play_game():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    current_player = "X"

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose position (1-9): ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input! Choose 1-9.")
            continue

        move = int(move) - 1

        if board[move] != " ":
            print("Position already taken!")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
    

if __name__ == '__main__':
    
    play_game()

