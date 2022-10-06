# Задайте список из n чисел последовательности 〖(1+1/n)〗^n
# и выведите на экран их сумму.

while True:
    num = input('Задайте количество чисел в последовательности: ')
    try:
        num = int(num)
        if num > 0:
            break
        else: print('Количество чисел не может быть отрицательным')
    except ValueError:
        print('Ошибка. Необходимо ввести целое положительное число')

list = []
for i in range(1, num + 1):
    elem = round(((1+1/i)**i), 2)
    list.append(elem)
print(list)
print(f'Сумма последовательности равна: {sum(list)}')