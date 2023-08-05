# Tic-Tac-Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if a player has won
def check_win(player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for positions in winning_positions:
        if all(board[pos] == player for pos in positions):
            return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        display_board()
        print("It's Player", current_player, "turn.")
        position = int(input('Choose a position (1-9): ')) - 1

        if board[position] == ' ':
            board[position] = current_player
        else:
            print('Invalid move. Try again.')
            continue

        if check_win(current_player):
            display_board()
            print('Player', current_player, 'wins!')
            break
        elif ' ' not in board:
            display_board()
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
