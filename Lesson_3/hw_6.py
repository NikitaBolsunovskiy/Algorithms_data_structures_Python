""" 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
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

b = a[min_index:max_index + 1] if min_index < max_index else a[max_index:min_index + 1]
el_sum = 0
for i in range(len(b)):
    if i != 0 and i != (len(b) - 1):
        el_sum += b[i]
print(b)
print(f'Сумма элементов между минимальным и максимальным: {el_sum}')

