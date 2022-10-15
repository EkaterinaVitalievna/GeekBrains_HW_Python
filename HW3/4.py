# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10

def double (num, d):
    if num//2 == 0:
        d = str(num%2) + d
        return d
    else:
        d = str(num%2) + d
        d = str(double(num//2, d))
        return d
        

number = int(input('Введите число : '))
str1 = ''
print(f'{number} = {double(number, str1)}')