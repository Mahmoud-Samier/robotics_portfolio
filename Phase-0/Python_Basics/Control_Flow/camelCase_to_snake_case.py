sen=input('enter the sentence')
for i in sen :
    if i.isupper():
        print(i.replace(i,f'_{i.lower()}') ,end='')
    else :
        print(i,end='')