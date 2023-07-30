import random
'''making a board list to print like actual game '''
board = ['-','-','-',
         '-','-','-',
         '-','-','-',]
currentPlayer = 'X'
GameRunning =True
Winner = None

'''1'''
# function to print the structure using the indices as the board is a list
def printboard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

'''2'''
# fuction to take input for filling the empty spot using index
def playerInput(board):
    index = int(input('enter a number between 0-8: '))
    # fill only if it is empty
    if board[index] == '-':
        board[index] = currentPlayer
    else:
        print('choose an empty spot')
        playerInput(board)

'''3'''
#function to check the winner horizontally
def horizontalcheck(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!= '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!= '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!= '-':
        winner = board[6]
        return True
'''4'''
# checking vertically
def verticalcheck(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!= '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!= '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!= '-':
        winner = board[2]
        return True
'''5'''
# checking diagonally
def diagonalcheck(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!= '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!= '-':
        winner = board[2]
        return True

'''6'''
# check for tie , condition is if all the empty spaces are filled inthe board
def tiecheck(board):
    global GameRunning
    if '-' not in board:
        printboard(board)
        print("it's a tie")
        GameRunning = False
        return True

'''7'''
# calling all the functions of checking the winner in the wincheck function
def wincheck():
    global GameRunning
    if horizontalcheck(board) or verticalcheck(board) or diagonalcheck(board):
        printboard(board)
        # using global the value of winner var. has been changed
        print(f"the winner is {winner}")
        GameRunning = False
        return True


'''8'''
#switching the turns to play the game by making the predefined var global
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'

'''9 versus computer'''
def computer(board):
    # giving computer O player
    while currentPlayer == "O":
        pos = random.randint(0,8)
        if board[pos] == '-':
            board[pos] = 'O'
            switchPlayer()


'''10'''
# main funtion to implement the game by calling all the function
while GameRunning:
    printboard(board)
    playerInput(board)
    if wincheck():
        break
    if tiecheck(board):
        break
    switchPlayer()
    computer(board)
    if wincheck():
        break
    if tiecheck(board):
        break





