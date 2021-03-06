# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

# Импортируем работы с аргументами
from sys import argv

# Получаем из командной строки путь к файлу, выработку в часах, ставку за час, премию
try:
    name, output_file = argv

except ValueError:
    # в случае если аргументов мало - сообщаем
    exit("Необходимо указать имя выходного файла как первый параметр строки запуска скрипта")

# всю запись делаем в попытке на случай ошибки работы с файлом
try:
    # открываем файла на запись - при каждом запуске он перезапишется
    file_obg = open(output_file, 'w', encoding='utf-8')

    # делаем бесконечный цикл
    while 1 == 1:

        # вводим очередную строку
        file_string = input('::')

        # если строка пустая - это признак завершения ввода
        if file_string == '':
            break

        # помним, что тут на самом деле теневой file_obg - записываем данные в файл
        file_obg.write(file_string)
        file_obg.write('\n')

    print(f'Сохранен файла {output_file}')

except IOError:
    print("Ошибка ввода-вывода в файл")
finally:
    file_obg.close()
