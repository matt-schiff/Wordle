import WordSelector as Word
import WordleSolver as WS
import WordleRefactored as WR
import temp, statistics

def tree(wordlist, word, i):
    options = temp.options()
    vals = []
    valsC = []
    for option in options:
        x = WS.pruneList(wordlist, word, option)
        if len(x) > 1:
            y = Word.enhancedBestLetters(x)
            x = WS.pruneList(wordlist, word, option)
            #print(i, word, option, ': ', x, y)
            t = tree(x,y,i + 1)
            for val in t:
                if type(val) == type(vals):
                    if val in vals:
                        valsP[vals.index(val[0])] = val[1]
                    else:
                        valsC.append(val[1])
                        vals.append(val[0])
        elif len(x) == 1:
            #print(i, word, option, ': ', x)
            return [[x[0],i],]
    return valsC
           
        
    
            
if __name__ == '__main__':
    vals = []
    a = tree(WR.generateGuesses(), 'salet', 1)
    print(a)
    print(sum(a)/len(a))
    print(tree(WR.generateGuesses(), 'irate', 1))
    print(tree(WR.generateGuesses(), 'steal', 1))
    print(tree(WR.generateGuesses(), 'tales', 1))
