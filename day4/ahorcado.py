ahorcado=[ '''
             ___
            |   |
                |
                |
                |
          ______|''','''
          
             ___
            |   |
            O   |
                |
                |
          ______|''','''

             ___
            |   |
            O   |
            |   |
                |
          ______|''','''

             ___
            |   |
            O   |
           /|   |
                |
          ______|''','''

             ___
            |   |
            O   |
           /|\  |
                |
          ______|''','''

             ___
            |   |
            O   |
           /|\  |
           /    |
          ______|''','''

             ___
            |   |
            0   |
           /|\  |
           / \  |
          ______|
          ''']

WordGuess=""
ListWordGue=[]
ListWordShow=[]
Attempts=0
letter=''
run =True

print("HANGMAN")
WordGuess=input('Write the word for the game')
ListWordGue=list(WordGuess)

for item in (ListWordGue):
    ListWordShow.append('_')

while run:
    print(' '.join(ListWordShow))

letter=input('Give me a letter')

for num in range(100):
    print()
fail=False

if letter not in ListWordGue:
    fallo=True
    Attempts+=1
    print(ahorcado[Attempts])
    print('Try again')
else:
    for key,value in enumerate(ListWordGue):
        if value == letter:
            ListWordShow[key]=value
if Attempts>=6:
    run=False
    print('Sorry GAME OVER')
elif ListWordGue == ListWordShow:
    run=False
    print('YOU WIN')