#index
#list=[1,2,3,4]
#print(list.index(1)) '''Te regresa la posición en la que se encuentra ese valor. Para este caso regersa 0'''

alphabet=['a', 'b', 'c', ' ','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', ' ','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar (selection,shift_number,start_word):
    
    end_word =''
    if selection == 'decode':
        shift_number*=-1

    for char in start_word:
        if char in alphabet:
           position = alphabet.index(char)
           new_position = position + shift_number
           end_word = end_word + alphabet[new_position]

    return end_word

should_end=False

while not should_end:
    selection = input("Type 'encode' to encrypt or 'decode' to decrypt ").lower()
    shift_number = int(input("Type a shift number "))
    start_word =input("Type your message: ")
    print(caesar(selection,shift_number,start_word))

    repit=input('Do you want do it again? y/n: ').lower()
    if repit == 'y':
        should_end=False
    elif repit == 'n':
        should_end=True 
print('Bye, see you latter')

