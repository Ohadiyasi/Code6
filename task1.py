
import random


board = ['_' for _ in range(9)]


def print_board():
    
    print( board[0], board[1], board[2])
    
    print( board[3],board[4], board[5])
   
    print( board[6], board[7],board[8],)
    


def check_win(player):

    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
  
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
   
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False


def ai_move():

    for i in range(9):
        if board[i] == '_':
            board[i] = 'O'
            if check_win('O'):
                return
            else:
                board[i] = '_'

   
    for i in range(9):
        if board[i] == '_':
            board[i] = 'X'
            if check_win('X'):
                board[i] = 'O'
                return
            else:
                board[i] = '_'


    while True:
        move = random.randint(0, 8)
        if board[move] == '_':
            board[move] = 'O'
            return


def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    while True:
        
        while True:
            player_move = int(input("Enter your move (1-9): ")) - 1
            if board[player_move] == '_':
                board[player_move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        
        print_board()

        
        if check_win('X'):
            print("Congratulations! You win!")
            break

        
        if '_' not in board:
            break

     
        ai_move()
        print("AI's move:")
        print_board()

     
        if check_win('O'):
            print("AI wins! Better luck next time.")
            break


play_game()