"""
Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только
из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""


import hashlib
import collections

counter = collections.Counter()

s = 'banana'
for len_sub in range(1, len(s)):
    for i in range(0, len(s) - len_sub + 1):
        substring = s[i:i + len_sub]
        # print(substring)
        sub_hash = hashlib.sha1(substring.encode('utf-8')).hexdigest()
        counter[sub_hash] += 1

c = counter.most_common()
print(len(c))
# print(shash)

