# Tic Tac Toe Game
# Test Branch Comment

import random

def drawField(field):
    # Print game field
    print(' ' + field[0] + ' | ' + field[1] + ' | ' + field[2])
    print('-----------')
    print(' ' + field[3] + ' | ' + field[4] + ' | ' + field[5])
    print('-----------')
    print(' ' + field[6] + ' | ' + field[7] + ' | ' + field[8])

def selectLetter():
    # Selection of player's letter.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Möchtest Du X oder O sein?')
        letter = input().upper()

    # Player's letter first, second computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoStartsFirst():
    # Random selection of the first player.
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Spieler'

def startAgain():
    # True = player wants to play again, False = player wants not to play again.
    print('Willst Du noch einmal spielen? (Ja oder Nein)')
    return input().lower().startswith('y')

def convertMoveToConvention(move):
    # converting from "nice" field indices to python convention
    return move - 1

def executeMove(field, letter, move):
    # Execute move in game field.
    field[move] = letter

def winGame(field, letter):
    # shorten parameter names for better overview. 
    fi = field
    le = letter
    
    # True when player wins.
    # fi instead of field, le instead of letter.
    return ((fi[6] == le and fi[7] == le and fi[8] == le) or # across the bottom
    (fi[3] == le and fi[4] == le and fi[5] == le) or # across the middle
    (fi[0] == le and fi[1] == le and fi[2] == le) or # across the top
    (fi[6] == le and fi[3] == le and fi[0] == le) or # down the left side
    (fi[7] == le and fi[4] == le and fi[1] == le) or # down the middle
    (fi[8] == le and fi[5] == le and fi[2] == le) or # down the right side
    (fi[6] == le and fi[4] == le and fi[2] == le) or # diagonal
    (fi[8] == le and fi[4] == le and fi[0] == le)) # diagonal

def makeFieldCopy(field):
    # Duplicate the field.
    dupeField = []
    for i in field:
        dupeField.append(i)
    return dupeField

def isSpaceFree(field, move):
    # True = passed move free on the passed field.
    return field[move] == ' '

def getPlayerMove(field):
    # Player can type in the move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(field, convertMoveToConvention(int(move))):
        print('Was ist dein nächster Zug? (1-9)')
        move = input()
    return int(convertMoveToConvention(int(move)))

def chooseRandomMoveFromList(field, movesList):
    # Valid move from passed list on the passed field.
    # None if no valid move remains.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(field, i):
            possibleMoves.append(i)
    
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(field, computerLetter):
    # Field and computer's letter. Determine and return the move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    
    # Tic Tac Toe Algorithm
    # Check if next move can win
    for i in range(0, 9):
        copy = makeFieldCopy(field)
        if isSpaceFree(copy, i):
            executeMove(copy, computerLetter, i)
            if winGame(copy, computerLetter):
                return i

    # Check if player can win with the next move.
    for i in range(0, 9):
        copy = makeFieldCopy(field)
        if isSpaceFree(copy, i):
            executeMove(copy, playerLetter, i)
            if winGame(copy, playerLetter):
                return i
    
    # Take a corner if one is free.
    move = chooseRandomMoveFromList(field, [0, 2, 6, 8])
    if move != None:
        return move
    
    # Take center if it is free.
    if isSpaceFree(field, 4):
        return 4
    
    # Move on one of the sides.
    return chooseRandomMoveFromList(field, [1, 3, 5, 7])

def isFieldFull(field):
    # True = all fields taken, False if not.
    for i in range(0, 9):
        if isSpaceFree(field, i):
            return False
    return True

# Execute game.
print('Willkommen zu Tic Tac Toe')

while True:
    # Reset the field.
    theField = [' '] * 10
    playerLetter, computerLetter = selectLetter()
    turn = whoStartsFirst()
    print('Der ' + turn + ' ist dran.')
    gameIsPlaying = True
   
    while gameIsPlaying:
        if turn == 'Spieler':
            # Player’s turn.
            drawField(theField)
            move = getPlayerMove(theField)
            executeMove(theField, playerLetter, move)

            if winGame(theField, playerLetter):
                drawField(theField)
                print('Juhuuu, Du hast das Spiel gewonnen!')
                gameIsPlaying = False
            else:
                if isFieldFull(theField):
                    drawField(theField)
                    print('Das Spiel ist unentschieden.')
                    break
                else:
                    turn = 'Computer'
        else:
            # Computer’s turn.
            move = getComputerMove(theField, computerLetter)
            executeMove(theField, computerLetter, move)
            
            if winGame(theField, computerLetter):
                drawField(theField)
                print('Der Computer hat gewonnen! Du hast leider verloren.')
                gameIsPlaying = False
            else:
                if isFieldFull(theField):
                    drawField(theField)
                    print('Das Spiel ist unentschieden.')
                    break
                else:
                    turn = 'Spieler'

if not playAgain():
    break