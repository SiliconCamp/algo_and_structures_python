'''
Возьмем для примера задачи Урока 4.
Посмотрим, насколько лучше у нас будет использоваться память при оптимизации работы с рандомом (оптимизация генератора
массива). По факту видим экономию на 0.1 MiB

Оптимизация алгоритма в данном случае вообще не дает эффекта по использванию памяти, что вполне логично, так как мы
лишь уменьшили колчество проходов цикла, а не задействовали дополнительных переменных.

В конца файла - отчеты.
'''

import random  # До оптимизации генератора массива
# from random import random  # После оптимизации генератора массива
import memory_profiler


@memory_profiler.profile()


def arr_generate(n):
    arr = [random.randint(1, 20) for _ in range(n)]  # До оптимизации генератора массива
    # arr = [int(random()*20) for _ in range(n)]  # После оптимизации генератора массива
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


main()

'''
До оптимизации генератора массива
Line #    Mem usage    Increment   Line Contents
================================================
     9     13.9 MiB     13.9 MiB   @memory_profiler.profile()
    10                             
    11                             
    12                             def arr_generate(n):
    13     14.1 MiB      0.1 MiB       arr = [random.randint(1, 20) for _ in range(n)]  # До оптимизации генератора массива
    14                                 # arr = [int(random()*20) for _ in range(n)]  # После оптимизации генератора массива
    15     14.0 MiB      0.0 MiB       print(arr)
    16     14.0 MiB      0.0 MiB       return arr


После оптимизации генератора массива
Line #    Mem usage    Increment   Line Contents
================================================
     9     13.8 MiB     13.8 MiB   @memory_profiler.profile()
    10                             
    11                             
    12                             def arr_generate(n):
    13                                 # arr = [random.randint(1, 20) for _ in range(n)]  # До оптимизации генератора массива
    14     14.0 MiB      0.1 MiB       arr = [int(random()*20) for _ in range(n)]  # После оптимизации генератора массива
    15     13.9 MiB      0.0 MiB       print(arr)
    16     13.9 MiB      0.0 MiB       return arr

'''