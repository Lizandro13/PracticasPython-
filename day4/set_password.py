#This is a program that construct a password with 'x'
# number of characters
import random 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('welcome to the PyPassword generator')
nr_letters=int(input('How many characters do you want in your password?'))
nr_numbers=int(input('How many numbers do you want in your password?'))
nr_symbols=int(input('How many symbols do you want in your password?'))

'''#easy way
password_string=""
for _ in range(1,nr_letters + 1):
    #password_string= password_string + random.choice(letters)
    password+=random.choice(letters)
#_ representa una variable, pero se pone _ porque no utilizo la variable
for _ in range(1,nr_numbers+1):
    password_string+=random.choice(numbers)
for _ in range(1,nr_symbols+1):
    password_string+=random.choice(symbols)

print(f"Your Password is: {password}")
'''

#hard way
password_list=[]
for _ in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
for _ in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))
for _ in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)

string_list_password=""
for element in password_list:
    string_list_password=string_list_password + element
print(string_list_password)