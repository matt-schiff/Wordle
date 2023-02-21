import random
import WordleRefactored as WR
import WordleSolver as WS


class InvalidWordException(Exception):
    pass
    
    
def alphabetList():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return list(alphabet)


'''
Input: broken down words
Output: Total counts of each letters as a list
'''
def letterFrequencies(words):
    letters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for word in words:
        for letter in word:
            val = ord(letter[0]) - 97
            letters[val] = letters[val] + 1
    return letters
    
'''
Input:
    frequencies: a list of frequencies of letters for each position in the word
    level: the level of the order to be checked (4,3,2,1,0)
    order: list of the order in which the frequencies should be checked
    word: the current list of letters in the form ['1', '2', '3', '4', '5']
    words: a list of valid words in the form ['1', '2', '3', '4', '5']
Output: a single word that is the first to resolve
'''
def recursiveWordFinder(frequencies, level, order, word, words):
    frequencyChart = frequencies[order[level]]
    maxVal = max(frequencyChart)
    if level == 0:
        for i in range(maxVal, 0, -1):
            for j in range(26):
                if frequencyChart[j] == i:
                    word[order[level]] = str(chr(97 + j))
                    if word in words:
                        return word
        return None
    else:
        for i in range(maxVal, 0, -1):
            for j in range(26):
                if frequencyChart[j] == i:
                    word[order[level]] = str(chr(97 + j))
                    result = recursiveWordFinder(frequencies, level - 1, order, word, words)
                    if result:
                        return result
    

'''
Input: list of words
Output: 5 lists of letter frequency (one for each letter position) in a list
'''
def letterPosFrequency(words):
    letterPos = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for word in words:
        for i in range(5):
            val = ord(word[i]) - 97
            letterPos[i][val] = letterPos[i][val] + 1
    return letterPos

'''
Input: A list of words
Output: A random word from the list to use
'''
def randomWord(words):
    return random.choice(words)

'''
Input: A list of words
Output: The first word that features the most commonly used letter as defined by both position and frequency
    prioritizes the first letter alphabetically and in the word (ie [algae, after, older] will return algae)
'''
def bestLetter(words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    brokenWords = []
    for word in words:
        brokeWord = list(word)
        brokenWords.append(brokeWord)
    maxLetters = []
    maxCounts = []
    for i in range(5):
        maxLetter = ''
        maxCount = 0
        for letter in alphabet:
            letterCount = 0
            for word in brokenWords:
                if word[i] == letter:
                    letterCount += 1
            if letterCount > maxCount:
                maxCount = letterCount
                maxLetter = letter
        maxLetters.append(maxLetter)
        maxCounts.append(maxCount)
    maxVal = max(maxCounts)
    idx = maxCounts.index(maxVal)
    letter = maxLetters[idx]
    for word in words:
        if word[idx] == letter:
            return word
            
'''
Input: a list of words
Output: a word from the list that contains the most most frequent letters from all the words
    prioritizes the earliest letter in the alphabet, and most frequent letter and position overall (ie list will return older [totalVal: 8 (1+2+1+2+2)].
'''
def bestLetters(words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    brokenWords = []
    for word in words:
        brokeWord = list(word)
        brokenWords.append(brokeWord)
    frequencies = letterPosFrequency(words)
    maxes = []
    letters = []
    for i in range(5):
        maxes.append(max(frequencies[i]))
        letters.append(str(chr(frequencies[i].index(max(frequencies[i]))+97)))
    
    maxOMax = max(maxes)
    order = []
    for i in range(maxOMax, 0, -1):
        for j in range(5):
            if maxes[j] == i:
                order.append(j)
    finalWord = recursiveWordFinder(frequencies, 4, order, letters, brokenWords)
    if finalWord == None:
        return 'Error calculating best word'
    return words[brokenWords.index(finalWord)]
    
'''
Input: A list of the reamining valid words
Output: A word that comes from the list of all words that contains the best letters possible
'''
def enhancedBestLetters(words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    brokenWords = []
    frequencies = letterPosFrequency(words)
    additionalWords = WR.generateGuesses()
    for word in words:
        brokeWord = list(word)
        brokenWords.append(brokeWord)
    for word in additionalWords:
        words.append(word)
    maxes = []
    letters = []
    for i in range(5):
        maxes.append(max(frequencies[i]))
        letters.append(str(chr(frequencies[i].index(max(frequencies[i]))+97)))
    
    maxOMax = max(maxes)
    order = []
    for i in range(maxOMax, 0, -1):
        for j in range(5):
            if maxes[j] == i:
                order.append(j)
    finalWord = recursiveWordFinder(frequencies, 4, order, letters, brokenWords)
    if finalWord == None:
        return 'Error calculating best word'
    return words[brokenWords.index(finalWord)]
    
'''
Input: a list of previous guesses and their scores
Output: a list of each letter and its possible and guaranteed positions (ex: ['a', (0,3), (1,)], ['b', (), ()])
'''
def generateAlphabet(guesses):
    uncheckedLetter = (0,1,2,3,4)
    invalidLetter = ()
    letters = []
    validLetters = []
    for guess in guesses:
        for i in range(5):
            if guess[1][i] == '0':
                if guess[0][i] in letters:
                    pos = letters.index(guess[0][i])
                    letterList = validLetters[pos]
                    newPos = []
                    for k in letterList[1]:
                        if i != k:
                            newPos.append(k)
                    newPos.sort()
                    letterList[1] = tuple(newPos)
                else:
                    letters.append(guess[0][i])
                    letterList = [guess[0][i], invalidLetter, invalidLetter]
                    validLetters.append(letterList)
            elif guess[1][i] == '1':
                if guess[0][i] in letters:
                    pos = letters.index(guess[0][i])
                    letterList = validLetters[pos]
                    if not i in letterList[2]:
                        newPos = [i]
                        for k in letterList[2]:
                            newPos.append(k)
                        newPos.sort()
                        letterList[2] = tuple(newPos)
                        newPos = []
                        for k in letterList[1]:
                            if k != i:
                                newPos.append(k)
                        newPos.sort()
                        letterList[1] = tuple(newPos)
                else:
                    letters.append(guess[0][i])
                    posList = []
                    for j in range(5):
                        if i != j:
                            posList.append(j)
                    posList = tuple(posList)
                    letterList = [guess[0][i], posList, (i,)]
                    validLetters.append(letterList)
            elif guess[1][i] == '2':
                if guess[0][i] in letters:
                    pos = letters.index(guess[0][i])
                    letterList = validLetters[pos]
                    pos = []
                    for j in letterList[1]:
                        if i != j:
                            pos.append(j)
                    pos.sort()
                    letterList[1] = tuple(pos)
                else:
                    letters.append(guess[0][i])
                    pos = []
                    for j in range(5):
                        if i != j:
                            pos.append(j)
                    pos.sort()
                    pos = tuple(pos)
                    letterList = [guess[0][i], pos, invalidLetter]
                    validLetters.append(letterList)
    alphabet = alphabetList()
    for letter in alphabet:
        if not letter in letters:
            validLetters.append([letter, uncheckedLetter, invalidLetter])
    validLetters.sort()
    return validLetters
    
    

    
    
    
                
