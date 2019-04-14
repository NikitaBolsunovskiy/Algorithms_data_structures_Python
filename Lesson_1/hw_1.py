""" 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

a = int(input("Введите трёхзначной число: "))

first_dig = a // 100
second_dig = (a % 100) // 10
third_dig = a % 10

print("Сумма цифр числа: " + str(first_dig + second_dig + third_dig))
print("Произведение цифр числа: " + str(first_dig * second_dig * third_dig))
