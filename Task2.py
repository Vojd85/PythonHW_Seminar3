# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
def pow_pare_list(list):
    res_list = []
    for i in range(len(list)//2):
        res = list[i]*list[-1 -i]
        res_list.append(res)
    if len(list)%2 != 0:
        res = list[len(list)//2]**2
        res_list.append(res)
    print(res_list)


pow_pare_list(list1)
pow_pare_list(list2)