"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

В качестве программы для теста взял ДЗ к 3-ему уроку:
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться.

ОС Windows 10 64 bit
Python 3.7.3
"""


from pympler import asizeof
import random


def my_func():
    n = int(input('Введите количество элементов первого массива: '))
    a = []

    for i in range(n):
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

    print()
    print('Анализируем использованную память.')
    print('Переменные, которые используются в программе:')
    print('N - int, a - массив int, min_el - int, min_index - int')
    print(f'Размер N: {asizeof.asizeof(n)}')
    print(f'Размер a: {asizeof.asizeof(a)}')
    print(f'Размер min_el: {asizeof.asizeof(min_el)}')
    print(f'Размер min_index: {asizeof.asizeof(min_index)}')


if __name__ == '__main__':
    my_func()
