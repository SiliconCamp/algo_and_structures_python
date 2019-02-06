"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Смог решить только вторую задачу. Для решения решил:
1. Написать все в виде классов для Листочков и Узлов с методом
2. Использовать структуры данных для наглядности, например именованные кортежи

Для начала создадим основную логику в виде main():

  -- Блок кодирования --
Запрашиваем строку у пользователя
Формируем словарь
Генерируем закодированную строку
  -- Блок демонстрации --
Показываем размер словаря, размер закодированного сообщения
Показываем сам словарь
Выводим закодированную строку (для трех слов она будет небольшая)
  -- Блок декодирования --
Декодируем строку и показываем что получилось

Для всего этого нам понадобится как минимум две функции: кодирования (принимает строку - возвращает словарь) и
декодирования (принимает зашифрованную строку и словарь - возвращает расшифрованную).
Также надо будет сделать два класса - Узел и Листочек. У Узла есть левая и правая ножка, у Листочка - значение.

При кодировании:
Формируем частотный словарь
Раскидываем символы по дереву
Собираем словарь с кодами и возвращаем его в виде кортежа

При декодировании:
Поочередно проходимся по всем символам закодированной строки
Формируем список символов, эквивалентным закодированным последовательностям
Выводим его (раскодированный список) в склеенном виде.

Пример работы:
Your string >>Карл у Клары украл кораллы
---
Dict size: 9
Encoded size (bit): 80
---
Dictionary:
' ' = 110
'К' = 0111
'а' = 100
'к' = 010
'л' = 00
'о' = 0110
'р' = 101
'у' = 1110
'ы' = 1111
01111001010011011101100111001001011111110111001010110000110010011010110000001111
Карл у Клары украл кораллы
"""

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)


def main():
    s = input("Your string >>")
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)

    print("---\nDict size: %d\nEncoded size (bit): %d\n---\nDictionary:" % (len(code), len(encoded)))
    for ch in sorted(code):
        print("'{}' = {}".format(ch, code[ch]))
    print(encoded)
    print(huffman_decode(encoded, code))


if __name__ == '__main__':
    main()
