import sys, os, random, time
import WordleRefactored as WR
import WordSelector as WS

def preprocessList(answerKey):
    newKey = []
    for word in answerKey:
        newWord = list(word)
        newKey.append(newWord)
    return newKey
    
def pruneList(possibleAnswers, guess, answerKey):
    validAnswers = []
    for word in possibleAnswers:
        if len(word) == 5:
            validAnswers.append(word)
    possibleAnswers = validAnswers
    for i in range(5):
        validAnswers = []
        if answerKey[i] == 1:
            for word in possibleAnswers:
                if word[i] == guess[i]:
                    validAnswers.append(word)
        if answerKey[i] == 2:
            for word in possibleAnswers:
                if word[i] != guess[i] and guess[i] in word:
                    validAnswers.append(word)
        if answerKey[i] == 0:
            goodRemoval = True
            for j in range(5):
                if ((answerKey[j] == 1 or answerKey[j] == 2) and guess[j] == guess[i]):
                    goodRemoval = False
            if goodRemoval:
                for word in possibleAnswers:
                    if not (guess[i] in word):
                        validAnswers.append(word)
            else:
                for word in possibleAnswers:
                    if word[i] != guess[i]:
                        validAnswers.append(word)
        possibleAnswers = validAnswers
    return possibleAnswers
    
def postprocessList(validAnswers):
    readableAnswers = []
    for word in validAnswers:
        newWord = ''
        for letter in word:
            newWord += letter
        readableAnswers.append(newWord)
    return readableAnswers
    
def mainProgram():
    WR.openingSequence()
    print('Solving Random Wordle...')
    answers = WR.generateAnswers()
    key = WR.selectWord(answers)
    print('Wordle Answer: ' + key)
    print('1> irate')
    answerKey = WR.makeGuess(key, 'irate')
    validAnswers = answers
    validAnswers = preprocessList(validAnswers)
    guess = list('irate')
    validAnswers = pruneList(validAnswers, guess, answerKey)
    readableAnswers = []
    for word in validAnswers:
        newWord = ''
        for letter in word:
            newWord += letter
        readableAnswers.append(newWord)
    print(readableAnswers)
    i = 1
    while answerKey != [1,1,1,1,1]:
        i += 1
        if len(validAnswers) > 1:
            guess = WS.enhancedBestLetters(readableAnswers)
        else:
            guess = readableAnswers[0]
        print(guess)
        print(str(i) + '> ' + guess)
        answerKey = WR.makeGuess(key, guess)
        guessList = list(guess)
        validAnswers = pruneList(validAnswers, guessList, answerKey)
        readableAnswers = postprocessList(validAnswers)
        if answerKey != [1,1,1,1,1]:
            print(readableAnswers)
        else:
            break
    print('Solution took ' + str(i) + ' guesses.')
    
def mainProgramHeadless():
    answers = WR.generateAnswers()
    key = WR.selectWord(answers)
    answerKey = WR.makeGuessHeadless(key, 'irate')
    validAnswers = answers
    validAnswers = preprocessList(validAnswers)
    guess = list('irate')
    validAnswers = pruneList(validAnswers, guess, answerKey)
    readableAnswers = []
    for word in validAnswers:
        newWord = ''
        for letter in word:
            newWord += letter
        readableAnswers.append(newWord)
    i = 1
    while answerKey != [1,1,1,1,1]: 
        guess = WS.enhancedBestLetters(readableAnswers)
        i += 1
        answerKey = WR.makeGuessHeadless(key, guess)
        guessList = list(guess)
        validAnswers = pruneList(validAnswers, guessList, answerKey)
        readableAnswers = postprocessList(validAnswers)
        if answerKey != [1,1,1,1,1]:
            pass
        else:
            break
    return i

if __name__ == '__main__':
    os.system('clear')
    if len(sys.argv) == 1:
        mainProgram()
    else:
        WR.openingSequence()
        maxMoves = 0
        count = 0
        timeA = time.time()
        for i in range(int(sys.argv[1])):
            turns = mainProgramHeadless()
            count += turns
            if turns > maxMoves:
                maxMoves = turns
        timeB = time.time()
        print('Number of solutions: ' + str(sys.argv[1]) + ' in ' + str(timeB-timeA) + ' seconds')
        print('Average length of solution: ' + str(count/int(sys.argv[1])))
        print('Maximum number of turns: ' + str(maxMoves))

