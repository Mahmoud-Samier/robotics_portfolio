n1 =int (input('1st number is'))
n2 =int (input('2st number is '))
s=input('sign is ')
if s=='+':
   sum= n1 +n2
   print(f'the result is {sum}')
if s=='-':
   sum= n1 - n2
   print(f'the result is {sum}')
if s=='*':
   sum= n1 * n2
   print(f'the result is {sum}')
if s=='/':
   sum:float=n1/n2
   if n2==0 :
      print('error')
   else:
      print(f'the result is {sum}')