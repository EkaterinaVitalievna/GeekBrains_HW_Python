# вариант 1

some_list = 'абв текст текстабв для дляабв тестирования абвтестирования программы программыабв'.split()
for elem in some_list:
    if "абв" in elem:
        print ("?", end=" ")
    else:
        print (elem, end=" ")


print ()
# вариант 2

some_list = 'абв текст текстабв для дляабв тестирования абвтестирования программы программыабв'.split()
new_list = list(filter(lambda i: not 'абв' in i, some_list))
print(' '.join(new_list))