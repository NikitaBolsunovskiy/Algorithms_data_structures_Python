""" 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

num = input('Введите число: ')
count_even = 0
count_not_even = 0
for i in num:
    if int(i) % 2 == 0:
        count_even += 1
    else:
        count_not_even += 1

print(f'Чётных цифр: {count_even}, Нечётных цифр: {count_not_even}')