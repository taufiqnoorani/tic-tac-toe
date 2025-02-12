import random

def get_order():
     first = random.choice("X" "0")
     if first == "X":
          second = "0"
     else:
          second = "X"
     
     return first, second

board = ["| 1 |","| 2 |","| 3 |",\
"| 4 |","| 5 |","| 6 |",\
"| 7 |","| 8 |","| 9 |"]

def update_board(board, current_player, approved_move):
     board[approved_move] = f"| {current_player} |"

     for i in range(0, 9, 3):
          print("".join(board[i:i+3]))


def play(first, second):
     current_player = first
     game = True
     list = [" " for _ in range (1, 10)]
     while game:
          print(f"{current_player}'s move")
          move = int(input("Choose a number between 1-9 to select a position on the board: "))
          if move not in range(1, 10):
               print("Invalid move. please select a valid number")
               continue
          elif(list[move - 1] != " "):
               print("Position already used. Choose another position")
               continue
          else:
               approved_move = move - 1
               list[move - 1] = current_player
               update_board(board, current_player, approved_move)
               if (list[0] and list[1] and list[2] == current_player or list[3] and list[4] and list[5] == current_player or list[6] and list[7] and list[8] == current_player or \
                   list[0] and list[3] and list[6] == current_player or list[1] and list[4] and list[7] == current_player or list[2] and list[5] and list[8] == current_player or \
                    list[0] and list[4] and list[8] == current_player or list[2] and list[4] and list[6] == current_player):
                    print(f"{current_player} wins")
                    game = False

               elif(" " not in list):
                    print("It's a tie")
                    game = False
               
               if current_player == first:
                    current_player = second
               else:
                    current_player = first
     
first, second = get_order()
play(first, second)