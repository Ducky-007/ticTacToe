board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def printBoard():
  print("\n")
  print("\t     |     |")
  print("\t {}   |  {}  |  {}".format(board[0][0], board[0][1], board[0][2]))
  print('\t_____|_____|_____')

  print("\t     |     |")
  print("\t {}   |  {}  |  {}".format(board[1][0], board[1][1], board[1][2]))
  print('\t_____|_____|_____')
  
  print("\t     |     |")
  print("\t {}   |  {}  |  {}".format(board[2][0], board[2][1], board[2][2]))
  print( "\t     |     |")
  print( "\n")

def checkWinner(currPlayer, board):
  for row in range(0,3):
    if board[row][0]==board[row][1]==board[row][2] and board[row][0] != '-':
      if board[row][0]==currPlayer:
        print(f"Player {currPlayer} wins!")
        return True

  for col in range(0,3):
    if board[0][col]==board[1][col]==board[2][col] and board[0][col] != "-":
      if board[0][col] == currPlayer:
        print(f"Player {currPlayer} wins!")
        return True

  if board[0][0]==board[1][1]==board[2][2] and board[0][0] != "-":
    if board[0][0] == currPlayer:
      print(f"Player {currPlayer} wins!")
      return True

  if board[0][2]==board[1][1]==board[2][0] and board[0][2] != "-":
    if board[0][2] == currPlayer:
      print(f"Player {currPlayer} wins!")
      return True
  return False

printBoard()

col = 0
row = 0
playerTurn = "X"

for counter in range(1, 10):
  validMove = False
  while (validMove == False):
    col = 0
    row = 0
    while (col < 1 or col > 3):
      col = int(input(playerTurn + " player, select a column 1-3: "))
      if (col < 1 or col > 3):
        print("The column must be between 1 and 3.")
    while (row < 1 or row > 3):
      row = int(input(playerTurn + " player, select a row 1-3: "))
      if (row < 1 or row > 3):
        print("The row must be between 1 and 3.")
    col -= 1
    row -= 1

    if board[row][col] == "-":
      board[row][col] = playerTurn
      validMove = True;
    else:
      print("Oops, that spot was already taken.")
  printBoard()
  if (checkWinner(playerTurn, board)):
    break

  if playerTurn == "X":
    playerTurn = "O"
  else:
    playerTurn = "X"
