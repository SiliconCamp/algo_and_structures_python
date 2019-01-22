'''
В данном случае мы сгенерируем Решето Эратосфена сразу "с запасом".
На текущем оборудовании мы без проблем можем сгенерировать список простых чисел в диапазоне 1 ... 1 100 000, что
позволяет вычислять значения i вплоть до 85714-того простого числа за (три пробы): 35.543, 35.168, 35.007

Для сравнения с предыдущим алгоритмом, 7000-ое простое число вычисляется в Решете диапазона 1 ... 80000 за 2,5 секунды!

Линейная сложность в пределах заданного (достаточно широкого) диапазона O(1).
Опицонально можно подключить простенький прогресс-бар, чтобы было веселее (но дольше) ждать генерации Решета.
Результаты оценки - внизу файла
'''

import cProfile
from math import sqrt


def make_eratosfen(limit):
    lst = range(2, limit)
    print(int(sqrt(limit)//100), end=":")  # Прогресс-бар для больших диапазонов (снижает производительность!)
    for i in range(2, int(sqrt(limit)) + 1):
        lst = list(filter(lambda x: x == i or x % i, lst))
        if i % 100 == 0: print(i//100, end=".")  # Прогресс-бар для больших диапазонов (снижает производительность!)
    return lst


def main():
    num = int(input("Enter i="))

    arr = make_eratosfen(2000000)
    print()
    print(arr[num], len(arr))


cProfile.run("main()")

'''
Без прогресс-бара:
Enter i=85000

1090381
         109143379 function calls in 35.007 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.002    0.002   35.007   35.007 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        1   15.542   15.542   31.724   31.724 eratosfen.py:11(make_eratosfen)
109143366   16.182    0.000   16.182    0.000 eratosfen.py:14(<lambda>)
        1    0.000    0.000   35.005   35.005 eratosfen.py:19(main)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000   35.007   35.007 {built-in method builtins.exec}
        1    3.281    3.281    3.281    3.281 {built-in method builtins.input}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



С прогресс-баром, диапазон 1 ... 2000000 (до 148933-его простого числа) = 82.853 sec

Enter i=90000
14:1.2.3.4.5.6.7.8.9.10.11.12.13.14.
1159531
         253645000 function calls in 82.853 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.004    0.004   82.853   82.853 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        1   36.898   36.898   74.949   74.949 eratosfen.py:17(make_eratosfen)
253644971   38.050    0.000   38.050    0.000 eratosfen.py:21(<lambda>)
        1    0.000    0.000   82.849   82.849 eratosfen.py:26(main)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000   82.853   82.853 {built-in method builtins.exec}
        1    7.900    7.900    7.901    7.901 {built-in method builtins.input}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       17    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        2    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Готово к отправке
'''