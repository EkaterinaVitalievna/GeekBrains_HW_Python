# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задайте последовательность чисел. Напишите программу,
# которая будет выводить список неповторяющихся элементов исходной последовательности

from random import randint

sequence_length = int(input('Введите длинну последовательности: '))

length_value = []
for i in range(sequence_length):
    length_value.append(randint(0,10))
print(f'Длинна последовательности: {sequence_length}')
print(length_value)
print()

length_value_unique = []
for elem in length_value:
    if length_value.count(elem) == 1:
        #length_value_unique.append(elem)
        print(elem, end=", ")



length_value_unique = [elem for elem in length_value if length_value.count(elem) == 1]
print (length_value_unique)