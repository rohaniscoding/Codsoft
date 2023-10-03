import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

# Function to check if the game is a draw
def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to evaluate the board for the AI player
def evaluate(board):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    else:
        return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    elif is_draw(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_eval = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

# Main game loop
def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)

        player_move = input("Enter your move (row and column, e.g., 1 2): ")
        row, col = map(int, player_move.split())

        if board[row - 1][col - 1] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row - 1][col - 1] = 'O'

        if check_win(board, 'O'):
            print_board(board)
            print("You win!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'

        if check_win(board, 'X'):
            print_board(board)
            print("AI wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()