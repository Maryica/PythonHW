# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_arr = [0, 24, -1, 32, 5, -22, -3, 15, 1, 16]
min_num = int(input('Введите минимальный элемент диапазона: '))
max_num = int(input('Введите максимальный элемент диапазона: '))
list_new = []
for i in range(len(list_arr)):
    if min_num <= list_arr[i] <= max_num:
        list_new.append(i)
print('Индексы элементов массива в заданном диапазоне:  ', *list_new)