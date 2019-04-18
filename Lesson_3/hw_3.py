""" 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


import random


N = int(input('Введите количество элементов первого массива: '))
a = []

for i in range(N):
    a.append(random.randint(0, 99))

print(a)

min_el = a[0]
max_el = a[0]

min_index = 0
max_index = 0

for i in range(len(a)):
    if i > 0:
        if a[i] < min_el:
            min_el = a[i]
            min_index = i
        if a[i] > max_el:
            max_el = a[i]
            max_index = i

print(f'Индекс минимального: {min_index}, индекс максимального: {max_index}')

a[min_index] = max_el
a[max_index] = min_el

print(a)