cities = ["Chicago", "London", "Tokyo"]

for city in cities:
  print(city)

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()
print(numbers)

for number in numbers:
  if number > 42:
    break
  print(number)


print('-----------------')
import random
numbers = []

while len(numbers) < 5:
  numbers.append(random.randint(1, 100))

for number in numbers:
  print(number)
  if number >= 90:
    print('Found at least one number greater than 90')
    break
else:
  print('No numbers greater than 90')

print('Complete')


import random

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selected_number = random.choice(numbers)
print(selected_number)

selected_numbers = random.choices(numbers, k=3)
print(selected_numbers)