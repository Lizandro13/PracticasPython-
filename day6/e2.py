'''def factorial_(n):
    factorial=1
    while n>0:
        factorial=factorial * n
        n-=1
    return factorial 
print(factorial_(6))'''

def factorial(n): #con recursion
    if n==0 or n==1:
        result=1
    elif n>1:
        result= n * factorial(n-1) 
    return result

facto=factorial(6)
print(facto)
