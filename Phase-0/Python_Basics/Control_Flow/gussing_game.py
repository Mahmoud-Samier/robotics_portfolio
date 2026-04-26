import random
y=random.randint(1,20)
x=int(input('enter number from 1 to 20'))
while True :
    
    if x == y :
        print('you are right')
        break
    elif x<y :
        print('enter bigger number')
    elif x>y:
        print ('enter smaller number')
    x=int(input('again , enter number from 1 to 20'))