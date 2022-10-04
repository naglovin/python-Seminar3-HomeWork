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

def list_rand_nums(count):                                                # Функция создания списка
    if count < 0:
        print("отрицательное число")
        return[]

    list_nums = sample(range(1, count * 2), count)
    return list_nums

def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):                                        # Длина списка поделена на пополам // Целочисленное деление, (RANGE не работает с дробями)
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])       # -k движение с двух сторон, -1 ставим всегда

    if len_list % 2:                                                      # Сюда мы попадаем когда у нас что то отличное от истины, если кратно, если 0. мы сюда не попадем
        res_list.append(list_nums[len_list // 2])
    return res_list

all_list =  list_rand_nums(int(input("Введите цифру")))
print(all_list)
print(prod_pairs(all_list))


