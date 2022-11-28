# snake,water,gun-->game 

import random

def gamewin(comp,you):
    if comp == you:
        return None
    if comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return False
        elif you=='g':
            return True
    if comp=='g':
        if you=='w':
            return False
        elif you=='s':
            return True
print("*********************************************")
print("WELCOME TO THE SNAKE , WATER , GUN ---GAME!!!")
print("*********************************************")

you= input("player:snake(s)water(w)or gun(g)??")
randno = random.randint(1,3)

if randno==1:
    comp = 's'

if randno==2:
    comp = 'w'

if randno==3:
    comp = 'g'
#  snake(s) water(w) or gun(g)??
print("computer turn ::",comp)

a = gamewin(comp,you)
if a == None:
    print("The game is a tie")
elif a:
    print("You win!!!!!!!!!:)))")
else:
    print("You Looseee!! :|")
    
