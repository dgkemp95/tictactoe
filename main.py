# User 1 input move('X', row, column)
# User 2 input move('O', row, column)

print("Welcome to Tic Tac Toe.\nTo make a move, use move('X', row, column) for Player 1 and move('O', row, column) for Player 2 respectively.\nPlayer 1's move.")
board = [["_", "_", "_", 0], ["_", "_", "_", 1], ["_", "_", "_", 2]]
print( "  0    1    2")
for row in board:
  print(row)

def move(player, horizontal, vertical):
  if player == "X":
    board[horizontal][vertical] = "X"
    print("\nPlayer 2's move")
    print( "  0    1    2")
    for row in board:
      print(row)
  if player == "O":
    board[horizontal][vertical] = "O"
    print("\nPlayer 1's move")
    print( "  0    1    2")
    for row in board:
      print(row)
