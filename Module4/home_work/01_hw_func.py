# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    num = str(ticket_number)
    list1 = int(num[:1]) + int(num[1:2])
    list2 = int(num[-1]) + int(num[-2])
    if list1 == list2:
        return True
    else:
        return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
