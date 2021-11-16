#if statement 

num1 = (input("Type a number: "))
if int(num1) % 2 == 0:
    num1 = int(num1)
    print(num1, 'is even number')
    if num1 == 10:
        print("num1 = 10")
    elif num1 == 6:
        print("num1 = 6")
    else:
        print("num1 != 10 and num1 != 6 ")
elif int(num1) % 2 !=0:
    print(num1, 'is odd number')
    if(int(num1) == 3):
        print("num1 = 3")
    elif int(num1) == 5:
        print("num1 = 5")
else:
    print("Invalid data")
