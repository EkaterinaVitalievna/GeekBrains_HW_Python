# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23

real_number = input('Введите вещественное число: ')
sum = 0
for i in real_number:
    if i.isdigit() == True:
        sum = sum + int(i)
print(sum)