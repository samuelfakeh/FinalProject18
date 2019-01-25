import random

print("Welcome to an INTENSE game of TicTacToe with a (drumroll please) COMPUTER!! The rules are simple first one to three in a row wins, doesn't matter which way. Good Luck :)")

print("     ---------------------------------------------")

print("                     1 | 2 | 3")
print("                   --------------")
print("                     4 | 5 | 6")
print("                   --------------")
print("                     7 | 8 | 9")

print("                                                      ")

def character():
    character = input("Choose a letter: ")
    while not (character == 'X' or character == 'O'):
        print("  Choose your letter and choose wisely (X's or O's)")

    if character == 'X':
      return ['X', 'O']
    else:
      return ['O', 'X']


def firstPlayer():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'



def makeChoice(board, character, choice):
    board[choice] = character

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def playAgain():
    print('I think you want to play again, right? (yes or no)')
    return input().lower().startswith('y')

def isSpaceOpen(board, choice):

    return board[choice] == ' '

def getPlayerChoice(board):
    choice = ' '
    while choice not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceOpen(board, int(choice)):
        print('Choose wisely, what is your choice? (1-9)')
        choice = input()
    return int(choice)
    if character == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def RandomChoiceList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceOpen(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getcomputerChoice(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceOpen(copy, i):
            makeChoice(copy, computerLetter, i)
            if whoWon(copy, computerLetter):
                return i


    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceOpen(copy, i):
            makeChoice(copy, playerLetter, i)
            if whoWon(copy, playerLetter):
                return i


    choice = RandomChoiceList(board, [1, 3, 7, 9])
    if choice != None:
        return choice
    if isSpaceOpen(board, 5):
        return 5

    return RandomChoiceList(board, [2, 4, 6, 8])

def gameBoard(board):
  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |')


def boardFull(board):
    for i in range(1, 10):
        if isSpaceOpen(board, i):
            return False
    return True

def whoWon(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))


while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = character()
    turn = firstPlayer()
    print('The ' + turn + ' will go first.')
    gameOn = True

    while gameOn:
        if turn == 'player':
            gameBoard(theBoard)
            choice = getPlayerChoice(theBoard)
            makeChoice(theBoard, playerLetter, choice)

            if whoWon(theBoard, playerLetter):
                gameBoard(theBoard)
                print('Hooray! You have won the game!')
                gameOn = False
            else:
                if boardFull(theBoard):
                    gameBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            choice = getcomputerChoice(theBoard, computerLetter)
            makeChoice(theBoard, computerLetter, choice)

            if whoWon(theBoard, computerLetter):
                gameBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameOn = False
            else:
                if boardFull(theBoard):
                    gameBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break