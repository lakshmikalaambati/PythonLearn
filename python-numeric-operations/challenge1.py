print('What is the temperature in fahrenheit?')
fahrenheit=input()
if not fahrenheit.isnumeric():
    print("Enter valid number")
    exit()

fahrenheit=float(fahrenheit)
celsius = (fahrenheit - 32) * 5/9
print(round(celsius))


