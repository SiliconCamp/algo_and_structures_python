'''
Берем алгоритм Эратосфена и смотрим его "жручесть на память". Собственно, как и следовало ожидать - ест и не давится.
(смотрим отчет внизу).
'''

from math import sqrt
import memory_profiler


@memory_profiler.profile()

def make_eratosfen(limit):
    lst = range(2, limit)
    print(int(sqrt(limit)//100), end=":")  # Прогресс-бар для больших диапазонов (снижает производительность!)
    for i in range(2, int(sqrt(limit)) + 1):
        lst = list(filter(lambda x: x == i or x % i, lst))
        if i % 100 == 0: print(i//100, end=".")  # Прогресс-бар для больших диапазонов (снижает производительность!)
    return lst


def main():
    num = int(input("Enter i="))

    arr = make_eratosfen(100000)
    print()
    print(arr[num], len(arr))


main()

'''
Эратосфен для 900000
Line #    Mem usage    Increment   Line Contents
================================================
     9     13.1 MiB     13.1 MiB   @memory_profiler.profile()
    10                             
    11                             def make_eratosfen(limit):
    12     13.1 MiB      0.0 MiB       lst = range(2, limit)
    13     13.1 MiB      0.0 MiB       print(int(sqrt(limit)//100), end=":")  # Прогресс-бар для больших диапазонов (снижает производительность!)
    14     22.3 MiB      0.0 MiB       for i in range(2, int(sqrt(limit)) + 1):
    15     23.7 MiB      0.5 MiB           lst = list(filter(lambda x: x == i or x % i, lst))
    16     22.3 MiB      0.0 MiB           if i % 100 == 0: print(i//100, end=".")  # Прогресс-бар для больших диапазонов (снижает производительность!)
    17     20.5 MiB      0.0 MiB       return lst

Эратосфен для 100000
Line #    Mem usage    Increment   Line Contents
================================================
     9     13.1 MiB     13.1 MiB   @memory_profiler.profile()
    10                             
    11                             def make_eratosfen(limit):
    12     13.1 MiB      0.0 MiB       lst = range(2, limit)
    13     13.1 MiB      0.0 MiB       print(int(sqrt(limit)//100), end=":")  # Прогресс-бар для больших диапазонов (снижает производительность!)
    14     14.2 MiB      0.0 MiB       for i in range(2, int(sqrt(limit)) + 1):
    15     14.2 MiB      0.1 MiB           lst = list(filter(lambda x: x == i or x % i, lst))
    16     14.2 MiB      0.0 MiB           if i % 100 == 0: print(i//100, end=".")  # Прогресс-бар для больших диапазонов (снижает производительность!)
    17     14.0 MiB      0.0 MiB       return lst
'''