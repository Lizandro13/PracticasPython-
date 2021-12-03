'''Funciones: srirven para realizar una tarea determinada'''
'''
def sum(x,y):
    return x+y
    #return: lo que te ntrega la función
'''

def max(a,b):
    return a>b
    '''if a>b:
        return True
    else:
        return False'''
x=int(input('Type a number: '))

y=int(input('Type another number: '))

if max(x,y):
    print(f'The first number {x} is bigger than the second {y}')
else:
    print(f'The second number {y} is bigger than the firt one {x}')

#recursividad: llamar la función dentro de la misma función 



