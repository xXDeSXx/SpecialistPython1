# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random
length = 9
cnt = 0
numbers = []
while cnt < length:
    numbers.append(random.randint(-100, 100))
    cnt = cnt + 1
print(numbers)
