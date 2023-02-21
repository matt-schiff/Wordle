import Wordle
import os

def fetchLetters(key, previousGuesses):
    keyVal = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for guess in previousGuesses:
        guessKey = Wordle.makeGuessDict(key, guess)
        for j in range(26):
            if guessKey[alphabet[j]] == 1:
                keyVal[j] = 1
            if guessKey[alphabet[j]] == 2 and keyVal[j] != 1:
                keyVal[j] = 2
            if guessKey[alphabet[j]] == 0 and keyVal[j] != 1 and keyVal[j] != 2:
                keyVal[j] = 0
    return keyVal
                    
                

def printLetters(previousGuesses, key, guessed):
    clearAnswers()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(8):
        print("\x1b[" + str(15 + i) + ';' + str(50) + 'H', end = "")
        print(f'{i+1}: ', end = "")
        if guessed[i] == False:
            keyVal = fetchLetters(key[i], previousGuesses)
            for j in range(26):
                if keyVal[j] == 1:
                    print(f'\u001b[48;2;18;227;74m\u001b[38;2;0;0;0m{alphabet[j]}\u001b[0m', end = '')
                elif keyVal[j] == 2:
                    print(f'\u001b[48;2;255;255;28m\u001b[38;2;0;0;0m{alphabet[j]}\u001b[0m', end = '')
                elif keyVal[j] == 3:
                    print(alphabet[j], end='')
                else:
                    print(' ', end = '')
        else:
            print(' ' * 26, end = '')
    printGuesses(previousGuesses, key)
    
def printGuesses(previousGuesses, key):
    clearAnswers()
    guessOutput = ''
    for i in range(guessesTaken):
        for j in range(8):
            if i < guessed[j] or guessed[j] == False:
                (answerKey, printVal) = Wordle.makeGuessMultiWord(key[j], previousGuesses[i])
                guessOutput += printVal
            else:
                guessOutput += '_____'
            guessOutput += ' '
        guessOutput += '\n'
    print(guessOutput)
    
def clearAnswers():
    print("\033[%d;%dH" % (14, 0))
    for i in range(13):
        print('_____ _____ _____ _____ _____ _____ _____ _____')
    print("\033[%d;%dH" % (14, 0))
    
def clearGuess():
    print("\033[%d;%dH" % (12, 0))
    print('               ')
    print("\033[%d;%dH" % (11, 0))                                                                                         


def printInstructions():
    print('''
 _______  _______ _________ _______  _______  ______   _        _______ 
|  ___  ||  ____ \\\\__   __/|  ___  ||  ____ ||  __  \\ | \\      |  ____ \\
| |   | || |    \\/   | |   | |   | || |    ||| |  \\  || |      | |    \\/
| |   | || |         | |   | |   | || |____||| |   | || |      | |__    
| |   | || |         | |   | |   | ||     __|| |   | || |      |  __|   
| |   | || |         | |   | |   | || |\\ |   | |   | || |      | |      
| |___| || |____/\\   | |   | |___| || | \\ \\__| |__/  || |____/\\| |____/\\
|_______||_______/   |_|   |_______||/   \\__/|______/ |_______/|_______/''')
    print('\nWelcome to Octordle! This game is just like normal Wordle, just with 8 words to guess. Good Luck!')

def generateKey():
    words = Wordle.generateAnswers()
    key = []
    for i in range(8):
        word = Wordle.selectWord(words)
        while word in key:
            word = Wordle.selectWord(words)
        key.append(word)
    return key

os.system('clear')
printInstructions()
key = generateKey()
guessed = [False, False, False, False, False, False, False, False]
guessesRemaining = 13
guessesTaken = 0
previousGuesses = []
while guessesRemaining > 0:
    printLetters(previousGuesses, key, guessed)
    clearGuess()
    guess = Wordle.formatGuess(input('Your guess:    \n> '))
    while not Wordle.checkWord(guess, Wordle.generateGuesses()):
        clearGuess()
        guess = Wordle.formatGuess(input('Invalid guess:\n> '))
    guessesRemaining -= 1
    guessesTaken += 1
    guessOutput=''
    previousGuesses.append(guess)
    for i in range(8):
        if Wordle.makeGuessHeadless(key[i], guess) == [1,1,1,1,1]:
            guessed[i] = 13-guessesRemaining
    printGuesses(previousGuesses, key)
    allGuessed = True
    printLetters(previousGuesses, key, guessed)
    for i in range(8):
        if guessed[i] == False:
            allGuessed = False
    if allGuessed:
        break
    elif guessesRemaining != 0:
        clearGuess()
if not allGuessed:
    print('The Answers were:')
    words = ''
    for word in key:
        words += f'{word} '
    print(words)
else:
    print("\x1b[" + str(25 + i) + ';' + str(0) + 'H', end = "")
    print('You Win!')

        
        


