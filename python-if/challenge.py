print('Would you like to continue?')
resp=str.upper(input())
if(resp=='Y' or resp=='YES' ):
    print('Continuing ...')
    print('Complete!')
elif(resp=='NO' or resp=='N'):
    print('Exiting')
else:
    print('Please try again and respond with yes or no')