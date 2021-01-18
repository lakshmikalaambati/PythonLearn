print('Simple calculator!')
print('First number?')
number1=input()
if not number1.isnumeric():
    print("Not valid number")
    exit()

print('enter operation')
oper1 = input()
# if('oper1' not in ['+','-','*','/','%','**']):
#     print("not valid operator")
#     exit()

print('Second number?')
number2=input()
if not number2.isnumeric():
    print("Not valid number")
    exit()

if(oper1=='+'):
    result=int(number1)+int(number2)
    print('Sum :'+str(result))
elif(oper1=='-'):
    result=int(number1)-int(number2)
    print('Diff  :'+str(result))
elif(oper1=='*'):
    result=int(number1)*int(number2)
    print('Product :'+str(result))
elif(oper1=='/'):
    result=int(number1)/int(number2)
    print('Division :'+str(result))
elif(oper1=='%'):
    result=int(number1)%int(number2)
    print('Modulus :'+str(result))
elif(oper1=='**'):
    result=int(number1)**int(number2)
    print('Expoent :'+str(result))
else:
    print("Not valid operator")