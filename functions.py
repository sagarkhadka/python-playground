def higher(num1, num2):
  if (num1 > num2):
    print (num1, 'is greater')
  
  else:
    print (num2, 'is greater')

def lower(num1, num2):
  if (num1 < num2):
    print(num1, 'is smaller')

  else:
    print(num2, 'is smaller')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print('1. for higher \n2. for lower' )
option = int(input('Choose your option: '))

match option:
  case 1:
    higher(num1, num2)
  case 2:
    lower(num1, num2)
  case _:
    print('Invalid option')