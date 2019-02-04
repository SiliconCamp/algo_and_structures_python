'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
используйте метод сортировки, который не рассматривался на уроках
---

Сначала делаем функцию генерации массива. Массив у нас нечетный, следовательно медианой у нас будет элемент с
индексом "m" в отсортированном массиве. Для самопроверки и сравнения решений задачи - напишем такую функцию.
sorted_median()


Теперь попробуем найти медиану в несортированном массиве, а вычислеямое ранее значение используем для проверки.
Для нахождения за среднее время O(n) воспользуемся алгоритмом Quickselect (https://en.wikipedia.org/wiki/Quickselect)
Данное решение чем-то навеяно сортировкой методом слияний - та же рекурсивность, обеспечивающая скорость.
Этот алгоритм был предложен Тони Хоаром (Sir Charles Antony Richard Hoare), который в 1960-х был студентом по обмену
в МГУ работал под руководством Колмогорова А.Н. (компьютерный перевод, теория вероятностей)

Суть алгоритма в следующем:
Выбираем опорный элемент (pivot) любым способом (например, random.choice)
Теперь выбираем из массива индексы всех элементов меньше опорного (lows), больше опорного (highs) и раныее ему (pivots)
Здесь удобно воспользоваться генераторами списков Python

Мы знаем, что одна из этих групп содержит медиану. Предположим, что мы ищем k-тый элемент:
    1. Если в списке меньших элементов содержится k или больше эл-тов, рекурсивно обходим список меньших эл-тов
    в поисках k-того элемента.
    2. Если в списке меньших элементов содержится меньше, чем k элементтов, рекурсивно обходим список бОльших элементов.
    Вместо поиска k мы ищем: k минус количество меньших эл-тов.

Безусловно наш алгоритм не обогнал встроенную функцию сортировки ("Ах, кот бы сомневался ..."), но показывает вполне
пристойный результат для массива из 10 миллионов натуральных чисел в диапазоне (-20, 300).
Отчет приложен в конце файла.
'''

import random
import time

M = 10000  # Константа для расчета длины массива (2m + 1)


def gen_array(min_value, max_value):
    n = 2 * M + 1
    a = [0] * n
    for i in range(n):
        a[i] = random.randint(min_value, max_value)
    return a


def sorted_median(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[M]


def quickselect(our_lst, k):

    pivot = random.choice(our_lst)  # Случайным образом выберем элемент из массива как опорный

    # Генерируем списки меньших, больших и опорных
    lows = [el for el in our_lst if el < pivot]
    highs = [el for el in our_lst if el > pivot]
    pivots = [el for el in our_lst if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]  # Найдена медиана
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


def main():
    array = gen_array(-20, 300)

    cur_time = time.time()
    print("--- Sorted Method Test ---")
    print(array)
    print("Median (sorted method) =", sorted_median(array))
    print("Time(ms) =", int((time.time()-cur_time)*1000))

    array = gen_array(-20, 300)

    cur_time = time.time()
    print("--- QuickSelect Method Test ---")
    print(array)
    print("Median (QuickSelect method) =", quickselect(array, M))
    print("Time(ms) =", int((time.time() - cur_time) * 1000))


if __name__ == '__main__':
    main()

'''
Результат для массива из 10 миллионов натуральных чисел в диапазоне (-20, 300).
--- Sorted Method Test ---
Median (sorted method) = 140
Time(ms) = 2620
--- QuickSelect Method Test ---
Median (QuickSelect method) = 140
Time(ms) = 9010
'''