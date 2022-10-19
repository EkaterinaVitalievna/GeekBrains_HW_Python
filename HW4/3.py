# 32). Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def unique_numbers(numbers):
    return [i for i in numbers if numbers.count(i) == 1]


user_numbers = [1, 2, 2, 2, 4, 4, 5]

print(unique_numbers(user_numbers))