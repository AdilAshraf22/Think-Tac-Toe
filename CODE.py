import random
import time

# Set up the game board
board = ["-"] * 9

# Winning combinations
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
]

# Print the game board
def print_board():
    print("\n" + board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8] + "\n")

# Check for a winner
def check_winner():
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "-":
            return board[combo[0]]
    return None

# Check if the board is full
def is_draw():
    return "-" not in board

# Function to handle the player's turn
def take_turn():
    print("Your turn.")
    position = input("Choose a position (1-9): ")
    while position not in [str(i) for i in range(1, 10)] or board[int(position) - 1] != "-":
        position = input("Invalid input. Choose a valid position (1-9): ")
    board[int(position) - 1] = "X"
    print_board()

# **Easy AI: Chooses a random available move**
def easy_ai():
    available_positions = [i for i in range(9) if board[i] == "-"]
    move = random.choice(available_positions)
    board[move] = "O"
    print("AI chose position:", move + 1)
    print_board()

# **Minimax Algorithm for Medium & Hard AI**
def minimax(is_maximizing, alpha=-float('inf'), beta=float('inf')):
    winner = check_winner()
    if winner == "X": return -1  # Human wins
    if winner == "O": return 1   # AI wins
    if is_draw(): return 0       # Tie

    best_score = -float('inf') if is_maximizing else float('inf')
    for i in range(9):
        if board[i] == "-":
            board[i] = "O" if is_maximizing else "X"
            score = minimax(not is_maximizing, alpha, beta)
            board[i] = "-"  # Undo move

            if is_maximizing:
                best_score = max(best_score, score)
                alpha = max(alpha, score)
            else:
                best_score = min(best_score, score)
                beta = min(beta, score)

            if beta <= alpha:
                break  # Alpha-beta pruning

    return best_score

# **AI Move using Minimax**
def ai_move(use_alpha_beta=False):
    best_score = -float('inf')
    best_move = None

    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(False, -float('inf'), float('inf')) if use_alpha_beta else minimax(False)
            board[i] = "-"  # Undo move

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"
        print("AI chose position:", best_move + 1)
        print_board()

# **Game Loop**
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Choose AI difficulty: (1) Easy, (2) Medium, (3) Hard: ")

    print_board()

    while True:
        take_turn()  # Player's turn

        if check_winner():
            print("You win!")
            break
        if is_draw():
            print("It's a tie!")
            break

        print("AI is thinking...\n")
        time.sleep(1)

        if mode == "1":  # Easy AI (Random)
            easy_ai()
        elif mode == "2":  # Medium AI (Minimax)
            ai_move()
        elif mode == "3":  # Hard AI (Minimax with Alpha-Beta Pruning)
            ai_move(use_alpha_beta=True)

        if check_winner():
            print("AI wins!")
            break
        if is_draw():
            print("It's a tie!")
            break

# Start the game
play_game()
