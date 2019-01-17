#3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

'''
В принципе можно было бы решить задачу средствами Python и выделить min()/max() и извлечь их индексы методом .index()
Но курс у нас про алгоритмы, поэтому пойдем длинным путем ...

АЛГОРИТМ:
Генерируем рандомный список (одномерный массив)
Выводим его

Объявляем переменные для индексов минимума и максимума
ЦИКЛ по всем элементам массива
    Если очередной элемент меньше чем минимальный из ранее найденных, то переопределяем индекс минимального.
    Иначе если элемент больше чем максимальный, то переопределяем индекс максимального
Выводим найденные минимум/максимум, и их индексы
Обмениваемся значениями минимума и максимума через 3-ю переменную
Выводим измененный массив
'''

import random
N = 20
arr = [random.randint(1, 99) for _ in range(N)]

print(arr)

min_index = 0
max_index = 0
for i in range(N):
    if arr[i] < arr[min_index]:
        min_index = i
    elif arr[i] > arr[min_index]:
        max_index = i
print('Element %d = %d (min), element %d = %d (max)' % (min_index+1, arr[min_index], max_index+1, arr[max_index]))
buff = arr[min_index]
arr[min_index] = arr[max_index]
arr[max_index] = buff

print(arr)
