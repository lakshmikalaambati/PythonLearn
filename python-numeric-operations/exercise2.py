numeric_value = '7'
print(numeric_value.isnumeric())


string_value = 'Bob'
print(string_value.isnumeric())
print('--------------')
print('Enter number1')
number1=input()
if(number1.isnumeric() == False):
    print('Not valid number')
    exit()


print('enter number2')
number2=input()

if(number2.isnumeric() == False):
    print('Not valid number')
    exit()

sum=float(number1)+float(number2)

print('Sum: '+str(sum))