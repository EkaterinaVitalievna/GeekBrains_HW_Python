# Задайте число N, создайте список: [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции (случайные) хранятся в файле file.txt
# (создаётся во время выполнения кода и зависит от количества элементов в списке)
# в одной строке одно число.
# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

import random

# создание списка
n = int(input('Введите количество элементов: '))
run = range(-n, n, 2)
numbers = list(run)
print(numbers)

#Запись позиций в файл
number = random.randint(2, n)
f = open('4.1.txt','w')
for i in range (number):
    index = random.randint(0,n-1)
    f.write(str(index))
    f.write('\n')
f.close()

multiplicator = 1
#for i in  range (1, number+1):
with open ("4.1.txt", "r") as f:
    for i in f :
        print(i)
        multiplicator = multiplicator * numbers[int(i)]
#f.close()
print(f'Произведение чисел под заданными в файле номерами = {multiplicator}')