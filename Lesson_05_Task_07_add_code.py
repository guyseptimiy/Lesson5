# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
# импортируем функции работы с частями имен файлов
from os.path import dirname, join


def process_file(input_file):
    profit_sum = 0
    totals_firm = 0

    dict_profit_by_firm = {}

    try:

        # Открываем файл на чтение
        file_obg = open(input_file, 'r', encoding='utf-8')

        # обходим все строки в файле
        for file_line in file_obg:
            # увеличиваем счетчик фирм на 1
            totals_firm += 1

            # получаем данные по фирме
            firm_data = file_line.split()
            firm_name = firm_data[0].replace('\ufeff', '')
            # считаем прибыль по фирме
            total = float(firm_data[2]) - float(firm_data[3])

            # Если она положительная включаем в сумму для расчета средней
            if total > 0:
                profit_sum += float(firm_data[2])

            # наполняем словарь фирм с прибыллью
            dict_profit_by_firm.update({firm_name: total})

        average_profit = profit_sum / totals_firm

        # формируем словарь со средней прибылью
        dict_average = {'average_profit': average_profit}

        # формируем записываый в файл список
        data_to_write = [dict_profit_by_firm, dict_average]
        print(data_to_write)

    except IOError:
        # в случае ошибки ввода вывода - сообщаем
        print("Ошибка ввода-вывода в файл")

    except ValueError:
        # в случае если аргументов мало - сообщаем
        exit("Файл данных содержит ошибку")

    finally:
        # не забываем закрывать файл
        file_obg.close()

    path = dirname(input_file)
    output_file = join(path, 'Lesson-05-Task-07-output_data.txt')
    print(f'output: {output_file}')

    try:
        file_obg = open(output_file, 'w', encoding='utf-8')
        json.dump(data_to_write, file_obg)

    except IOError:
        # в случае ошибки ввода вывода - сообщаем
        print("Ошибка ввода-вывода в файл")
    finally:
        # не забываем закрывать файл
        file_obg.close()
