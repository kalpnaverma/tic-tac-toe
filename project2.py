
def print_board(board):
    """Print the current state of the board."""
    print("\n" + " | ".join(board[0:3]))
    print("---------")
    print(" | ".join(board[3:6]))
    print("---------")
    print(" | ".join(board[6:9]) + "\n")
    
def check_winner(board, player):
    """Check if the current player has won the game."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    """Check if the board is full (no empty spaces)."""
    return ' ' not in board


def tic_tac_toe():
    """Main function to play the game."""
    board = [' '] * 9
    current_player = 'X'
    
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")
          
        move = int(move) - 1

        # Make the move
        board[move] = current_player
        
        # Check for a win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()