# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplication (num):
    if num <= 1:
        return 1
    else:
        return (num * multiplication (num-1))
number = int(input('Введите число: '))
for i in range(1, number):
    print(multiplication(i), end= ', ')
print(multiplication(number))

free_number = int(input("Введите число: "))
m = 1
a = 1
for i in range (free_number):  
    print(m * a, end=", ")
    m = m * a
    a += 1