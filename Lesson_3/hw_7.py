""" 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться.
"""

import random


N = int(input('Введите количество элементов первого массива: '))
a = []

for i in range(N):
    a.append(random.randint(0, 99))

print(a)

min_el = a[0]
min_index = 0

for i in range(len(a)):
    if i > 0:
        if a[i] < min_el:
            min_el = a[i]
            min_index = i

print(f'Индекс минимального: {min_index}')

a.pop(min_index)

print(a)

min_el = a[0]
min_index = 0

for i in range(len(a)):
    if i > 0:
        if a[i] < min_el:
            min_el = a[i]
            min_index = i

print(f'Индекс минимального: {min_index}')

a.pop(min_index)

print(a)