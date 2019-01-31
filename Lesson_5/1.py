"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Изначальная идея состоит в том, что у каждой компании должен быть ID (уникальный ключ), по которому мы храним название
компании (допускается, что оно не уникально ... всякое может случиться). Для хранения воспользуемся структурой
данных defaultdict. Я отказался от использования последовательностей и множеств в пользу отображений Mapping так как
ID может со временем стать чем-то подобен шифру, компании могут удаляться и я не хочу сдвига ID, ну и по многим другим
причинам "потнециального расширения функционала" (объект "Компания" может быть очень многогранным).

Все оформим в виде функций и пока выведем в виде циклов. Среднюю прибыль каждого предприятия храним дополнительным
значением и одним махом выводим и первормеров и андерперформеров.
"""

import collections
import random

company_dict = collections.defaultdict(list)

def gen_of_complist(company_count):
    for i in range(1, company_count+1):
        print("Give me the #%d company name" % i)
        next_name = str(input("Enter="))
        company_dict[i] = [next_name]


def receive_data(company_count):
    for i in range(1, company_count + 1):
        for j in range(1, 5):
            print("Give me the #%d quarter results for company '%s'" % (j, str(company_dict[i][0])))
            next_result = input("Enter=")
            if next_result == '':
                next_result = random.randint(10, 1000)
                print(">> Random generated=", next_result)
            company_dict[i].append(int(next_result))
        print("-------------------------")


def take_data(comp_id, qrt=6):
    if qrt > 5:
        return list(company_dict[comp_id])
    else:
        return company_dict[comp_id][qrt]


def take_average(comp_id):
    sum = 0
    for i in range(1, 5):
        sum += int(take_data(comp_id, i))
    company_dict[comp_id].append(sum/4)
    return company_dict[comp_id][5]


def main():
    company_count = int(input("How many companies? Enter="))
    print("-------------------------")
    gen_of_complist(company_count)
    print("-------------------------")
    receive_data(company_count)

    # Определяем среднюю прибыль
    print("Averages (per enterprise):")
    total_sum = 0
    for comp_id in company_dict.keys():
        next_sum = take_average(comp_id)
        print("%s = %d" % (take_data(comp_id, 0), next_sum))
        total_sum += next_sum
    print("-------------------------")
    industry_avg = int(total_sum/company_count)
    print("Industry Average =", industry_avg)
    print("-------------------------")

    # Выводим наименования предприятий, чья прибыль выше среднего
    print("Performers:")
    for comp_id in company_dict.keys():
        if company_dict[comp_id][5] > industry_avg:
            print(company_dict[comp_id][0])
    print("-------------------------")

    # Выводим наименования предприятий, чья прибыль ниже среднего
    print("Under-performers:")
    for comp_id in company_dict.keys():
        if company_dict[comp_id][5] < industry_avg:
            print(company_dict[comp_id][0])
    print("-------------------------")


if __name__ == '__main__':
    main()