# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# Импортируем работы с аргументами и именами частей файла
from os.path import dirname, join
from sys import argv

# Получаем из командной строки путь к файлу, выработку в часах, ставку за час, премию
try:
    name, input_file = argv
    print(f'input : {input_file}')

    path = dirname(name)
    output_file = join(path, 'Lesson-05-Task-04-output_data.txt')
    print(f'output: {output_file}')

except ValueError:
    # в случае если аргументов мало - сообщаем
    exit("Необходимо указать имя входного файла как первый параметр строки запуска скрипта")

try:

    # Открываем файл на чтение
    input_file_obg = open(input_file, 'r', encoding='utf-8')
    output_file_obg = open(output_file, 'w', encoding='utf-8')

    # обходим все строки в файле
    for file_line in input_file_obg:

        # делаем замены
        new_line = ''
        if 'One' in file_line:
            new_line = file_line.replace('One', 'Один')
        elif 'Two' in file_line:
            new_line = file_line.replace('Two', 'Два')
        elif 'Three' in file_line:
            new_line = file_line.replace('Three', 'Три')
        elif 'Four' in file_line:
            new_line = file_line.replace('Four', 'Четыре')

        # Ничего не нашли - просто перезапишем строку в новый файл
        if new_line == '':
            new_line = file_line

        # записываем данные в файл получатель
        output_file_obg.write(new_line)

except IOError:
    # в случае ошибки ввода вывода - сообщаем
    print("Ошибка ввода-вывода в файл")

finally:
    # не забываем закрывать файл
    input_file_obg.close()
    output_file_obg.close()
