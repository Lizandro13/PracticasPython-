import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game=[rock,paper,scissors]
computer=random.randint(0,len(game)-1)
choice= int(input("make a choice 0-rock, 1-paper, 2-scissors"))

if choice==0 and computer ==2:
    print("User WINS")
elif choice==2 and computer ==0:
    print("computer wins")
elif choice==computer:
    print("it is a tie")
elif choice>computer:
    print("User WINS")
elif choice<computer:
    print("Computer wins")


#show game 
print("User's choice")
print(game[choice])
print("Computer's choice")
print(game[computer])

