# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23

# real_number = input('Введите вещественное число: ')
# sum = 0
# for i in real_number:
#     if i.isdigit() == True:
#         sum = sum + int(i)
# print(sum)

real_number = float(input("Введите вещественное число: "))
a = len(str(real_number)) - 2
real_number = int(real_number * 10 ** a)
sum = 0
while real_number > 0:
    sum = int(sum + real_number % 10)
    real_number = real_number / 10
print(sum)