# 22. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
sum_odd_position = 0
for i in range(1, len(list), 2):
    sum_odd_position += list[i]
print(f'{list} - сумма элементов на нечетных позициях равна: {sum_odd_position}')

exit()
control_list = [int(input('введите элемент списка: '))
for _ in range(int(input('Введите кол-во элементов: ')))]
print \
    (f'Сумма элементов {[control_list[i] for i in range(len(control_list)) if i%2 == 1]} ,\
    стоящих на нечетных позициях = {sum([control_list[i] for i in range(len(control_list)) if i%2 == 1])}')