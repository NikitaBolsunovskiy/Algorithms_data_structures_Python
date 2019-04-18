""" 4. Определить, какое число в массиве встречается чаще всего.
"""


import random


N = int(input('Введите количество элементов первого массива: '))
a = []

for i in range(N):
    a.append(random.randint(0, 5))

print(a)

count = 0
element = -1

for i in range(len(a)):

    count_new = a.count(a[i])
    if count_new > count:
        element = a[i]
        count = count_new

print(f'Этот элемент встречается чаще всего: {element}, а именно {count} раз')


