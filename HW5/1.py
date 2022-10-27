# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

some_list = 'абв текст текстабв для дляабв тестирования абвтестирования программы программыабв'.split()
new_list = list(filter(lambda i: not 'абв' in i, some_list))
print(' '.join(new_list))

exit()

my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'


def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)


my_text = del_some_words(my_text)
print(my_text)
