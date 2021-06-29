# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

sentence = "На лугу пасется "
cows_number = int(input("Введите кол-во коров>>"))
if (cows_number >= 11) and (cows_number <= 14):
    print(sentence + str(cows_number) + " коров")
elif cows_number % 10 == 0 or cows_number % 10 >= 5 and cows_number % 10 <= 9:
    print(sentence + str(cows_number) + " коров")
elif cows_number % 10 == 1:
    print(sentence + str(cows_number) + " корова")
elif cows_number%10>=2 and cows_number%10 <=4:
    print(sentence + str(cows_number) + " коровы")
