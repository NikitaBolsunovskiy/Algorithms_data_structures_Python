""" 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""



import random


N = int(input('Введите количество элементов первого массива: '))
a = []

for i in range(N):
    a.append(random.randint(0, 7) - 5)

print(a)

first = True
max_el_below_zero = 0

for i in range(len(a)):
    if first and a[i] < 0:
        max_el_below_zero = a[i]
        first = False
    elif max_el_below_zero < a[i] < 0:
        max_el_below_zero = a[i]

print(f'Максимальный отрицательный Элемент: {max_el_below_zero}')
