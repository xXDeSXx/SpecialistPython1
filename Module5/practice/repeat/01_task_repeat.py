# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.
import random


def gen_list(size, of, to):
    cnt = 0
    my_list = []
    while cnt < size:
        my_list.append(random.randint(of, to))
        cnt = cnt + 1
    return my_list


print(gen_list(5, 10, 1000))
