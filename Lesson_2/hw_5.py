"""5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def print_ascii_symbols(a, b):
    sequence = range(a,b+1)
    string = ''
    count = 0
    for i in sequence:
        string = string + str(f'{i}-"{chr(i)}" ')
        count += 1
        if count == 10:
            print(string)
            count = 0
            string = ''


print_ascii_symbols(32, 127)
