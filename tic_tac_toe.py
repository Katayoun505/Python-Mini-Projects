# Tic-Tac-Toe game

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False


def get_player_move(board, player):
    while True:
        move = int(input(f"Player {player}, enter your move (1-9): "))
        if move < 1 or move > 9 or board[move-1] != " ":
            print("Invalid move, try again.")
            continue
        return move - 1


def game_loop():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = 0

    while True:
        display_board(board)
        move = get_player_move(board, players[current_player])
        board[move] = players[current_player]

        if check_win(board, players[current_player]):
            display_board(board)
            print(f"Player {players[current_player]} wins!")
            return

        if " " not in board:
            display_board(board)
            print("It's a tie!")
            return

        current_player = (current_player + 1) % len(players)


if __name__ == "__main__":
    game_loop()
