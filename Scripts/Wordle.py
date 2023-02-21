#!/usr/bin/env python3
import random, os

def generateAnswers():
    with open('wordle-answers-alphabetical.txt', 'r') as words:
        words = words.read()
        words = words.split('\n')
        newWords = []
        for word in words:
            if len(word) == 5:
                newWords.append(word)
        return newWords

def generateGuesses():
    with open('wordle-answers-alphabetical.txt', 'r') as words:
        words = words.read()
        answers = words.split('\n')
        with open('wordle-allowed-guesses.txt', 'r') as words:
            words = words.read()
            words = words.split('\n')
            words = words + answers 
            newWords = []
            for word in words:
                if len(word) == 5:
                    newWords.append(word)
            return newWords
            
def generateWrong():
    with open('wordle-answers-alphabetical.txt', 'r') as words:
        words = words.read()
        answers = words.split('\n')
        newWords = []
        for word in words:
            if len(word) == 5:
                newWords.append(word)
        return newWords
        

def selectWord(words):
    return random.choice(words)
    
def checkWord(word, words):
    return word in words

def openingSequence():
    gameName = """ .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
| ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
| |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
| |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
| |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
| |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'"""
    print(gameName)
    print('Guess the word in 6 guesses.\nAfter each guess, the color of the tiles will display to show how close your guess was to the word.')
    print('\u001b[48;2;18;227;74m\u001b[38;2;0;0;0mGREEN\u001b[0m  means the letter is in the word and in the correct place.')
    print('\u001b[48;2;255;255;28m\u001b[38;2;0;0;0mYELLOW\u001b[0m means the letter is in the word but not in the correct place.')
    print('\u001b[48;2;115;115;115mGREY\u001b[0m   means the letter is not in the word in any spot.')
    
def formatGuess(word):
    word = (''.join(e for e in word if (e.isalnum() and not e.isdigit()))).lower()
    return word
    
def validateGuess(word, words):
    return len(word) == 5 and checkWord(word, words)

def makeGuessDict(word, guess):
    letters = list(word)
    guessL = list(guess)
    letterDict = {}
    colorCode = [0,0,0,0,0]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letter in alphabet:
        letterDict[letter] = 3
    for i in range(0,len(guessL)):
        if letters[i] == guessL[i]:
            colorCode[i] = 1
            letterDict[guessL[i]] = 1
        else:
            count = 0
            for j in range(0,len(letters)):
                if letters[j] == guessL[i]:
                    count += 1
                    if letters[j] == guessL[j]:
                        count -= 1
            if count > 0:
                for j in range(0,i):
                    if guessL[j] == guessL[i]:
                        count -= 1
            if count > 0:
                colorCode[i] = 2
    for i in range(5):
        if colorCode[i] == 2 and letterDict[guessL[i]] != 1:
            letterDict[guessL[i]] = 2
        elif colorCode[i] == 0 and letterDict[guessL[i]] > 2:
            letterDict[guessL[i]] = 0
    return letterDict

def makeGuess(word, guess):
    letters = list(word)
    guessL = list(guess)
    colorCode = [0,0,0,0,0]
    for i in range(0,len(guessL)):
        if letters[i] == guessL[i]:
            colorCode[i] = 1
        else:
            count = 0
            for j in range(0,len(letters)):
                if letters[j] == guessL[i]:
                    count += 1
                    if letters[j] == guessL[j]:
                        count -= 1
            if count > 0:
                for j in range(0,i):
                    if guessL[j] == guessL[i]:
                        count -= 1
            if count > 0:
                colorCode[i] = 2
    printVal = ''
    for i in range(0,len(guessL)):
        if colorCode[i] == 0:
            printVal += '\u001b[48;2;115;115;115m' + guessL[i] + '\u001b[0m'
        elif colorCode[i] == 1:
            printVal += '\u001b[48;2;18;227;74m\u001b[38;2;0;0;0m' + guessL[i] + '\u001b[0m'
        else:
            printVal += '\u001b[48;2;255;255;28m\u001b[38;2;0;0;0m' + guessL[i] + '\u001b[0m'
    print(printVal)
    return colorCode
    
def makeGuessMultiWord(word, guess):
    letters = list(word)
    guessL = list(guess)
    colorCode = [0,0,0,0,0]
    for i in range(0,len(guessL)):
        if letters[i] == guessL[i]:
            colorCode[i] = 1
        else:
            count = 0
            for j in range(0,len(letters)):
                if letters[j] == guessL[i]:
                    count += 1
                    if letters[j] == guessL[j]:
                        count -= 1
            if count > 0:
                for j in range(0,i):
                    if guessL[j] == guessL[i]:
                        count -= 1
            if count > 0:
                colorCode[i] = 2
    printVal = ''
    for i in range(0,len(guessL)):
        if colorCode[i] == 0:
            printVal += '\u001b[48;2;115;115;115m' + guessL[i] + '\u001b[0m'
        elif colorCode[i] == 1:
            printVal += '\u001b[48;2;18;227;74m\u001b[38;2;0;0;0m' + guessL[i] + '\u001b[0m'
        else:
            printVal += '\u001b[48;2;255;255;28m\u001b[38;2;0;0;0m' + guessL[i] + '\u001b[0m'

    return (colorCode, printVal)
    
def makeGuessHeadless(word, guess):
    letters = list(word)
    guessL = list(guess)
    colorCode = [0,0,0,0,0]
    for i in range(0,len(guessL)):
        if letters[i] == guessL[i]:
            colorCode[i] = 1
        else:
            count = 0
            for j in range(0,len(letters)):
                if letters[j] == guessL[i]:
                    count += 1
                    if letters[j] == guessL[j]:
                        count -= 1
            if count > 0:
                for j in range(0,i):
                    if guessL[j] == guessL[i]:
                        count -= 1
            if count > 0:
                colorCode[i] = 2
    return colorCode
    
if __name__ == '__main__':
    os.system('clear')
    openingSequence()    
    words = generateAnswers()
    word = selectWord(words)
    words = generateGuesses()
    guesses = 6
    guessed = False
    while guesses > 0:
        guess = None
        while True:
            guess = input('> ')
            guess = formatGuess(guess)
            if not validateGuess(guess, words):
                print('Try Again')
            else:
                break
        makeGuess(word, guess)
        if word == guess:
            print('You Win!')
            guessed = True
            break
        else:
            guesses -= 1
            print(str(guesses) + '/6 Guesses Remaining')
    if not guessed:
        print('You Lose! The word was ' + word)
    
    
    
    
    
    
    
    
