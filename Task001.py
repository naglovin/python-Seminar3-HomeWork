# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

from random import sample
def find_num(q):                                 
    arr = sample(range(1, q * 2), q)   # sample выбирает из обьекта(кортеж, список и т.д) буковка q выбирает цифру от одного до q*2 т.е в два раза больше, 
    print(arr)
    s = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            s += arr[i]         
    return s 
print("сумма нечетных элементов", find_num(5))
