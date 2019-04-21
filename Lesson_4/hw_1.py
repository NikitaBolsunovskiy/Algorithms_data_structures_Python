"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех
уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Взял в качестве тестового алгоритмма задание 5 из домашнего задания урока 3.
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random
import timeit


def generate_array(n, max_random):
    a = []

    for i in range(n):
        a.append(random.randint(0, max_random) - int(max_random / 2))

    return a


def find_maximum_element_below_zero_in_array(a):
    first = True
    max_el_below_zero = 0

    for i in range(len(a)):
        if first and a[i] < 0:
            max_el_below_zero = a[i]
            first = False
        elif max_el_below_zero < a[i] < 0:
            max_el_below_zero = a[i]

    return max_el_below_zero


def find_maximum_element_below_zero_in_array2(a):

    b = []

    for i in range(len(a)):
        if a[i] < 0:
            b.append(a[i])

    b = sorted(b, reverse=True)

    return b[0]


def test_function_main():
    a = generate_array(100, 100)
    find_maximum_element_below_zero_in_array(a)


def test_function_main2():
    a = generate_array(100, 100)
    find_maximum_element_below_zero_in_array2(a)


print('Первый алгоритм (как делал в ДЗ): ')
print(str(timeit.timeit("test_function_main()", setup="from __main__ import test_function_main", number=1))
      + ': \t время выполнения на 1 повторе')
print(str(timeit.timeit("test_function_main()", setup="from __main__ import test_function_main", number=100))
      + ': \t время выполнения на 100 повторах')
print(str(timeit.timeit("test_function_main()", setup="from __main__ import test_function_main", number=10000))
      + ': \t время выполнения на 10000 повторах')
print('Видно, что время +- увеличивается картно количеству повторов. Сложность видимо порядка O(n), где n количество '
      'повторов (пробовал на массиве из 100,1000,10000 элементов)')

print()
print('Второй алгоритм: ')
print(str(timeit.timeit("test_function_main2()", setup="from __main__ import test_function_main2", number=1))
      + ': \t время выполнения на 1 повторе')
print(str(timeit.timeit("test_function_main2()", setup="from __main__ import test_function_main2", number=100))
      + ': \t время выполнения на 100 повторах')
print(str(timeit.timeit("test_function_main2()", setup="from __main__ import test_function_main2", number=10000))
      + ': \t время выполнения на 10000 повторах')
print('Видно, что время +- увеличивается картно количеству повторов. Сложность видимо порядка O(n), где n количество '
      'повторов (пробовал на массиве из 100,1000,10000 элементов)')
