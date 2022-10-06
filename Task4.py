# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
dec_number = int(input('Введите десятичное число: '))

def dec_to_bin_int(num):
    list = []
    while num > 0:
        bin_digit = num%2
        list.insert(0, bin_digit)
        num //=2
    print(list)

def dec_to_bin_str(number):
    bin_num = ""
    while number > 0:
        bin_num = str(number%2) + bin_num
        number //=2
    print(bin_num)

dec_to_bin_str(dec_number)
dec_to_bin_int(dec_number)
