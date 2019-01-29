'''
Достаем из резерва скрипт, не-Эратосфена. Смотрим использование памяти.
Как и следовало ожидать - стабильные 13.1 MiB
Жертвуем скоростью в пользу экономии памяти. Отчет внизу.
'''
import memory_profiler


@memory_profiler.profile()

def is_prime(a):
    return all(a % i for i in range(2, a))  # Проверяем - все ли нули в сгенерированном списке остатоков


def main():
    num = int(input("Enter i="))
    count = 0
    i = 0
    while count <= num:
        i += 1
        if is_prime(i):
            count += 1
    print(i)


main()

'''

Line #    Mem usage    Increment   Line Contents
================================================
     7     13.1 MiB     13.1 MiB   @memory_profiler.profile()
     8                             
     9                             def is_prime(a):
    10     13.1 MiB      0.0 MiB       return all(a % i for i in range(2, a))  # Проверяем - все ли нули в сгенерированном списке остатоков
    
Line #    Mem usage    Increment   Line Contents
================================================
     7     13.1 MiB     13.1 MiB   @memory_profiler.profile()
     8                             
     9                             def is_prime(a):
    10     13.1 MiB      0.0 MiB       return all(a % i for i in range(2, a))  # Проверяем - все ли нули в сгенерированном списке остатоков
'''