'''
Для начала реализуем алгоритм без применения Решета Эратосфена. Самый тупой - перебором.
Напишем функцию определения, является ли число простым.
В главной функции просто пройдем все натуральные числа одно за другим, проверяя являеется ли очередное - простым.
i-тое по счету простое число - выведем на экран.

Как и следовало ожидать, уже для вычислении 6000-го простого числа потребовалось (три пробы) 45.401, 42.196, 48.164

Сложность возрастает геометрически O(n*m)
1000 = 4.646
2000 = 5.964
3000 = 12.220
4000 = 17.181
5000 = 28.591
6000 = 42.850
7000 = 60.038

Результаты оценки внизу файла
'''
import cProfile


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


cProfile.run("main()")

'''
Enter i=7000
70657
         234175596 function calls in 60.038 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   60.038   60.038 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
    70657    0.087    0.000   57.408    0.001 non_eratosfen.py:22(is_prime)
234034273   35.894    0.000   35.894    0.000 non_eratosfen.py:23(<genexpr>)
        1    0.032    0.032   60.038   60.038 non_eratosfen.py:26(main)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
    70657   21.427    0.000   57.312    0.001 {built-in method builtins.all}
        1    0.000    0.000   60.038   60.038 {built-in method builtins.exec}
        1    2.598    2.598    2.598    2.598 {built-in method builtins.input}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Готово к отправке
'''