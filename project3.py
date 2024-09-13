board = [' '] *9
def print_board(board):
    
    print("\n" + " | ".join(board[0:3]))
    print("---------")
    print(" | ".join(board[3:6]))
    print("---------")
    print(" | ".join(board[6:9]) + "\n")
    
def check_winner(board, player):
   
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:

         if (board[condition[0]] == player and
            board[condition[1]] == player and
            board[condition[2]] == player):
            return True
    return False

def is_board_full(board):
    
    return ' ' not in board


def tic_tac_toe():

    current_player = 'X'
    
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")
          
        move = int(move) - 1
        if move < 0 or move > 8 or board[move] != ' ':
            print("already occupied. Try again.")
            continue
        board[move] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"congratulation Player {current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
        

    
        
tic_tac_toe()
print("thank you  ")