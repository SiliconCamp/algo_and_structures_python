"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

АЛГОРИТМ:

Запрашиваем входные данные

Объявляем счетчик
ЦИКЛ пока не пройдем все числа
    Берем очередное число
    ЦИКЛ пока не разберем все число до нуля
        Если последняя цифра равна искомой, то инкремент счетчика
        Отщипываем последнюю цифру

Выводим результат
"""

n = int(input("Nums will be entered: "))
d = int(input("Digit to be tracked: "))

count = 0
for i in range(1, n + 1):
    m = int(input())

    while m > 0:
        if m % 10 == d:
            count += 1
        m = m // 10

print("We tracked", d, "and count it:", count, "time(s)")
