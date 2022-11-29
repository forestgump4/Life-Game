# function definitions
import random


def binary(x,y):
    z=random.randint(0,1)
    if z==0:
        return x
    else:
        return y

def slowner(x):
    y=0
    while y<x:
        y +=1

def randfrmlist(x):
    z=int(len(x) +1)
    y=random.randint(0,str(z))
    return x[y]

def ask(statment, x, y):
    z=input(statment)
    z=z.lower()
    if z==x:
        return x
    elif z==y:
        return y
    else:
        return print('can u please answer the question? dont mess with this program that barely works.')

ask("how many people were killed",'yes','no')