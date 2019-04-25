"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
"""


import collections


enterprise_list = collections.defaultdict(list)
counter = collections.Counter()

n = int(input('Введите количество предприятий: '))

for i in range(n):
    name = input(f'Введите наименование предприятия №{i + 1}: ')
    enterprise_list[i].append(name)

for enterprise_el in enterprise_list:
    for i in range(4):
        profit = int(input(f'Введите прибыль за квартал №{i + 1} для предприятия {enterprise_list[enterprise_el]}: '))
        counter[enterprise_el] += profit

avg_profit = sum(counter.values()) / n
print()
print(f'Средняя прибыль за год всех предприятий: {avg_profit}')
print()
for enterprise_el in enterprise_list:
    profit = counter[enterprise_el]
    if profit >= avg_profit:
        print(f'Прибыль предприятия {enterprise_list[enterprise_el]} выше среднего, а именно: {profit}')
print()
for enterprise_el in enterprise_list:
    profit = counter[enterprise_el]
    if profit < avg_profit:
        print(f'Прибыль предприятия {enterprise_list[enterprise_el]} ниже среднего, а именно: {profit}')