# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
length = 4
cnt = 0
total = 0
numbers = []
while cnt < length:
    numbers.append(random.randint(-100, 100))
    cnt = cnt + 1
for number in numbers:
    if number % 2 == 0 and number > 0:
        total = total + int(number)
        print(number)
print("Total: ", total)
