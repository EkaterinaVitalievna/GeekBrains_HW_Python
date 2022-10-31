sequence = [1, 2, 3, 4, 7, 8, 9]

# 1 вариант
for id in range (len (sequence)):
    print('Индекс элемента: ', id, 'элемент', sequence[id], 'из списка sequence')

print ()

# 2 вариант
for id, el in enumerate (sequence):
    print('Индекс элемента: ', id, 'элемент', el, 'из списка sequence')