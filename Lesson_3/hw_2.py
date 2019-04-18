"""  2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""


import random


N = int(input('Введите количество элементов первого массива: '))
a = []
b = []

for i in range(N):
    a.append(random.randint(0, 99))
    if a[i] % 2 == 0:
        b.append(i)

print(a)
print(b)
