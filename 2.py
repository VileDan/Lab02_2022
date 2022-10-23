"""
Вычислить сумму знакопеременного ряда -(|х(2n+1)|)/(2n+1)!,
где х-матрица ранга к (к и матрица задаются случайным образом),
n - номер слагаемого. Сумма считается вычисленной,
если точность вычислений будет не меньше t знаков после запятой.
У алгоритма д.б. линейная сложность. Операция умножения –поэлементная.
"""



import numpy as np
from numpy import linalg

print("Добро пожаловать в лабораторную №2 студента ИСТбд - 22\nВерясова Владислава")
matrix = int(input('Введите размерность квадратной матрицы больше 1 и меньше 16:'))
while (matrix < 1) or (matrix > 16):
    matrix = int(input("Введите указанные числа"))
size = np.random.randint(5, size=(matrix, matrix))
print("Матрица:\n", size)

sign = int(input('Кол-во знаков после запятой:'))
sign = 0.1 ** sign
n = 1
factorial = 1
summ = 0
fg = 0
out = 1
while abs(out) > sign:
    fg += summ
    summ += -(np.linalg.det(linalg.matrix_power(size, 2 * n + 1))) / factorial
    n += 1
    factorial = factorial * (4*n - 1) * 2*n + 1
    out = abs(fg-summ)
    fg = 0
    print(n-1, ':', summ, ' ', out)
print('Сумма знакопеременного ряда:', summ)
