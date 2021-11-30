import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=['hangman','computer','travel','airplane']
chosen_word=random.choice(word_list)
lenght_word=len(chosen_word)

display=[]
for _ in range(lenght_word):
    display.append(' _ ')
print(display)
lives=6
end_of_game=True

while  end_of_game:    
    guess=input('Guess a letter: ').lower()
    #pido una letra y la hago minúscula 
    for position in range(lenght_word):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    
    if guess not in chosen_word:
        lives-=1
        print(stages[lives])
        if lives==0:
            end_of_game=False
            final_word=''
            for element in chosen_word:
                final_word=final_word+element
            print("YOU LOSE ")
            print(f"The secret word is: {final_word}")

    
    if ' _ ' not in display:
        end_of_game=False
        final_word=''
        for element in display:
            final_word=final_word+element
        print('¡¡¡YOU WIN!!!')
        print(f"The secret word is: {final_word}")