p:int=0

while p<50:
    c=int(input(f'please input the coin \n we need {50 - p}\n >>'))
    if c==5:
        p=p+c
    elif c==10 :
        p=p+c 
    elif c==25 :
        p=p+c 
    else:
        print('enter the right coin ')    
r=p-50
print(f'you have {r} as Change')