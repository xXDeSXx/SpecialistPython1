# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

side_a = int(input("Insert first side of triangle>>"))
side_b = int(input("Insert second side of triangle>>"))
side_c = int(input("Insert third side of triangle>>"))
if side_a == side_b or side_a == side_c or side_b == side_c:
    print("Triangle with side A=", side_a, ",side B=", side_b, ",side C=", side_c,"is isosceles")
else:
    print("Triangle with side A=", side_a, ",side B=", side_b, ",side C=", side_c, "isn't isosceles")
