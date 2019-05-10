"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде
функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def init_array(n):

    a = []
    for i in range(0, n):
        a.append(random.randint(-100, 100))
    return a


def buble_sort(a):
    counter = 0
    m = 1
    while m < len(a):
        for i in range(len(a) - m):
            counter += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        m += 1
    print(f'Количество операций внутренних: {counter}')
    return a


def buble_sort_opt(a):
    counter = 0
    m = 1
    was_moved = True
    while m < len(a) and was_moved:
        was_moved = False
        for i in range(len(a) - m):
            counter += 1
            if a[i] > a[i + 1]:
                was_moved = True
                a[i], a[i + 1] = a[i + 1], a[i]
        m += 1
    print(f'Количество операций внутренних: {counter}')
    return a


n = int(input('Введите размер массива: '))
a = init_array(n)

# a = [0, 9, 1, 2, 3, 4, 5, 6, 7, 8]

b = a.copy()
print(f'Рандомный массив размера {n}:')
print(a)

a = buble_sort(a)
print('Отсортированный массив (пузырьком):')
print(a)

b = buble_sort_opt(b)
print('Отсортированный массив (пузырьком оптимизированным):')
print(b)
