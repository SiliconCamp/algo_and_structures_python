"""
2.	Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив 
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), 
т.к. именно в этих позициях первого массива стоят четные числа.

АЛГОРИТМ:
Генерируем массив, объявляем переменные и т.д.
ЦИКЛ проходим весь массив
    Если элемент четны, то добавляем его позицию в список результатов
Выводим сам массив и позиции четных элементов
"""

import random
N = 20
arr = [random.randint(1, 99) for _ in range(N)]
even = []

for i in range(N):
    if arr[i] % 2 == 0:
        even.append(i)

print("Array:", arr)
print('\"Even\" positions: ', even)

