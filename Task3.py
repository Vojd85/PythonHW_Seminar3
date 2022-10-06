# Задача 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1 = [1.1, 1.2, 3.35, 5.03, 10.05]

def ne_znat_kak_nazvat(list):
    res = 0
    max_double = round(list[0]%1, 3)
    min_double = round(list[0]%1, 3)
    for i in range(len(list)):
        if round(list[i]%1, 3) > max_double:
            max_double = round(list[i]%1, 3)
        if round(list[i]%1, 3) < min_double:
            min_double = round(list[i]%1, 3)
    res = max_double - min_double
    print("{:.3f}".format(res)) # round что-то не очень работает с числами меньше 1, не нашел как сделать лучше


ne_znat_kak_nazvat(list1)