# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]


from random import sample
from typing import List
def find_num(q):                                 
    arr = sample(range(1, q * 2), q)   # sample выбирает из обьекта(кортеж, список и т.д) буковка q выбирает цифру от одного до q*2 т.е в два раза больше, 
    print(arr)
list = []
for i in range(len(arr)):
    list.append(i[0] * i[-1], i[1] * i[2])
    return list 
print(find_num(5), List)