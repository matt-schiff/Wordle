import WordleSolver as WS
import WordleRefactored as WR
import WordSelector as Word

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
print('Wordle Solver: Make a guess on the wordle site (https://www.nytimes.com/games/wordle/index.html), then enter the information to this program')
print('Key:')
print('\u001b[48;2;18;227;74m\u001b[38;2;0;0;0mGREEN:\u001b[0m 1 or g.')
print('\u001b[48;2;255;255;28m\u001b[38;2;0;0;0mYELLOW:\u001b[0m 2 or y')
print('\u001b[48;2;115;115;115mGREY:\u001b[0m anything else')

answers = WR.generateAnswers()
answers = WS.preprocessList(answers)
while True:
    guess = input('Guess > ')
    guess = list(guess)
    answerKey = input('Key > ')
    key = []
    for letter in answerKey:
        if letter == '1' or letter == 'g':
            key.append(1)
        elif letter == '2' or letter == 'y':
            key.append(2)
        else:
            key.append(0)
    if key == [1,1,1,1,1]:
        break
    answers = WS.pruneList(answers, guess, key)
    rAnswers = WS.postprocessList(answers)
    suggestedAnswerR = Word.randomWord(rAnswers)
    suggestedAnswerB = Word.bestLetter(rAnswers)
    suggestedAnswerBs = Word.bestLetters(rAnswers)
    print('Remaining Answers: ' + str(rAnswers))
    print('Random Suggestion: ' + suggestedAnswerR)
    print('Best Letter Suggestion: ' + suggestedAnswerB)
    print('Best Letters Suggestion: ' + suggestedAnswerBs)
        
    
    
    
