import WordleRefactored as WR, os

previousGuesses = []
legalGuesses = WR.generateGuesses()
requiredLetters = []
requiredPlaces = []
badLetters = []

def additionalRules():
    print('''
Additional Rules for ANTIWORDLE:
    
    - The goal of the game is to survive as long as possible
    - If a letter is green: for all remaining guesses, that letter must remain in that position
    - If a letter is yellow: for all remaining guesses, that letter must remain in the word
    - If a letter is grey: for all remaining guesses, that letter must not be used again
    - No repeat words will be allowed.
    
Good Luck!''')

def validateGuess(guess, word):
    for letter in requiredLetters:
        if not letter in guess:
            return False
    for place in requiredPlaces:
        if guess[place] != word[place]:
            return False
    for letter in badLetters:
        if letter in guess:
            return False
    return not guess in previousGuesses and guess in legalGuesses
    
    
    
if __name__ == '__main__':
    os.system('clear')
    WR.openingSequence()   
    additionalRules() 
    words = WR.generateAnswers()
    word = WR.selectWord(words)
    print(word)
    while True:
        guess = input('> ')
        if validateGuess(guess, word):
            print('Good Guess')
            previousGuesses.append(guess)
            if guess == word:
                break
        else:
            print("Try Again")
        
