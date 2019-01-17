"""
7.	В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

Сначала можно найти минимальный элемент массива. После этого искать второй минимум, исключив их поиска первый
с помощью if. Данный способ рассматривается здесь по отношению к двум наибольшим элементам.

Сложнее задачу решить, используя один цикл перебора.

Предположим, что двумя наименьшими элементами массива являются первый и второй элемент. Присвоим их индексы переменным
m1 и m2. При этом, если первый элемент меньше второго, то его индекс присвоим m1, иначе m1 получит значение второго
элемента, а m2 первого.

Начнем перебирать массив в цикле, начиная с третьего элемента. Если он меньше элемента, чей индекс хранится в m1, то
присвоим индекс текущего элемента m1. Иначе (если значение по индексу m1 меньше, чем по индексу i) будем проверять,
не меньше ли значение по индексу i, того что по индексу m2.

Есть один не очевидный нюанс. Допустим, в m1 указывало на значение 5, а m2 - на 10. Очередной элемент равен 3.
Мы меняем m1, и забываем о числе 5. Однако оно может оказаться как раз вторым минимумом массива.

Поэтому в программе при изменении значения m1 надо предусмотреть проверку, не меньше ли теряемое значение, чем то,
что хранится по индексу m2.
"""

from random import random

N = 10
a = []
for i in range(N):
    a.append(int(random() * 100))
    print("%3d" % a[i], end='')
print()

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, N):
    if a[i] < a[min1]:
        b = min1
        min1 = i
        if a[b] < a[min2]:
            min2 = b
    elif a[i] < a[min2]:
        min2 = i

print("№%3d:%3d" % (min1 + 1, a[min1]))
print("№%3d:%3d" % (min2 + 1, a[min2]))
