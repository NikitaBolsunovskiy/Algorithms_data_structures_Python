""" 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

"""

a = int(input("Введите год (в формате YYYY): "))
if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
    leap_year = 0
else:
    leap_year = 1

if leap_year == 0:
    print("Не високосный год.")
else:
    print("Високосный год.")
