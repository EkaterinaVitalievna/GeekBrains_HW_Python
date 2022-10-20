# 34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю.
# Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12

from math import degree
from math import numpy as np

some_str = ''
number1 = int(input('введите степень первого многочлена: '))
number2 = int(input('введите степень второго многочлена: '))
# print(degree.form_funk(number, some_str)+ ' = 0')

# Запись многочленов в файлы
f = open('5_1_file.txt','w')
f.write(degree.form_funk(number1, some_str))
f.close()
f = open('5_2_file.txt','w')
f.write(degree.form_funk(number2, some_str))
f.close()

# сложение многочленов
with open ('5_1_file.txt', 'r') as f1:
    n1 = [x for x in f1.read().split('+')]
    m1=[]
    for i in range(len(n1)):
        m1.append (int(''.join(map(str, n1[i].split('x')[:1]))))
with open ('5_2_file.txt', 'r') as f2:
    n2 = [x for x in f2.read().split('+')]
    m2=[]
    for i in range(len(n2)):
        m2.append (int(''.join(map(str, n2[i].split('x')[:1]))))
with open ('5_3_file.txt', 'w') as f3:
    f3.write(str(np.poly1d(np.polyadd(m1, m2))))
p = np.poly1d(np.polyadd(m1, m2))
print(p)