'''
Для примера был взята Задача 4 из Урока 3.

Я взял этот пример потому, что тут можно оптимизировать и сам алгоритм (уменьшить сложность с О(n2) до O(n2/2), так
и оптимизировать собственно время исполнения за счет рационального использования встроенных функций.

Вот исходный код:
import random
N = 20
arr = [random.randint(1, 20) for _ in range(N)]

print(arr)

num = arr[0]
max_freq = 1
for i in range(N):
    freq = 0
    for k in range(N):
        if arr[i] == arr[k]:
            freq += 1
    if freq > max_freq:
        max_freq = freq
        num = arr[i]

if max_freq > 1:
    print("Element %d we can find %d times" % (num, max_freq))
else:
    print('Unique elements only')

Фактически, при увеличении размеров массива, время исполнения возрастает квадратично О(n2)
Чтобы этого избежать, можно пробегать не каждый раз весь массив, а только от i-го элемента до конца, так как ранее
встретившиеся вхождения уже были подсчитаны. Для задач тестирования принимаем массив размером 10 000 элементов.
Каждый раз будем делать три пробы.

Результаты до оптимизации алгоритма (сек): 10.760, 10.530, 10.520
Результаты после (сек): 5.423, 5.291, 5.429

Уже довольно достойно. Теперь удвоим количество элементов 20 000. Результаты 42.042 и 21.587 соответственно.

Теперь попробуем оптимизировать использование функции random при том же количестве элементов.
Получаем 42.651 и 21.104. Некоторое улучшение есть, но незначительное. Делал большое количество проб, результат
укладывался в пределах 500 мс. Возможно картина будет иной при увеличении диапазона элементов (randint(1, 20000))

В конце файла - репорты cProfile для оптимизированного генератора массива, но с различной реализацияей алгоритма.
'''
# import random  # До оптимизации генератора массива
from random import random  # После оптимизации генератора массива
import cProfile


def arr_generate(n):
    # arr = [random.randint(1, 20) for _ in range(n)]  # До оптимизации генератора массива
    arr = [int(random()*20) for _ in range(n)]  # После оптимизации генератора массива
    print(arr)
    return arr


def main():
    N = 20000
    arr = arr_generate(N)

    num = arr[0]
    max_freq = 1
    for i in range(N):
        freq = 0
        for k in range(N):
            if arr[i] == arr[k]:
                freq += 1
        if freq > max_freq:
            max_freq = freq
            num = arr[i]

    if max_freq > 1:
        print("Element %d we can find %d times" % (num, max_freq))
    else:
        print('Unique elements only')

cProfile.run("main()")

'''
До оптимизации алгоритма:
20008 function calls in 43.388 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   43.388   43.388 <string>:1(<module>)
        1    0.000    0.000    0.015    0.015 Complexity_analysis.py:50(arr_generate)
        1    0.005    0.005    0.007    0.007 Complexity_analysis.py:52(<listcomp>)
        1   43.372   43.372   43.388   43.388 Complexity_analysis.py:57(main)
        1    0.000    0.000   43.388   43.388 {built-in method builtins.exec}
        2    0.009    0.004    0.009    0.004 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    20000    0.001    0.000    0.001    0.000 {method 'random' of '_random.Random' objects}





После оптимизации алгоритма:
20008 function calls in 23.248 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   23.248   23.248 <string>:1(<module>)
        1    0.000    0.000    0.013    0.013 Complexity_analysis.py:50(arr_generate)
        1    0.006    0.006    0.007    0.007 Complexity_analysis.py:52(<listcomp>)
        1   23.235   23.235   23.248   23.248 Complexity_analysis.py:57(main)
        1    0.000    0.000   23.248   23.248 {built-in method builtins.exec}
        2    0.006    0.003    0.006    0.003 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    20000    0.001    0.000    0.001    0.000 {method 'random' of '_random.Random' objects}
'''