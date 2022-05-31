# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from functools import reduce
from os.path import dirname, join
# импортуруем себе работу с генератором случайных чисел
from random import randint
# Импортируем работы с аргументами и именами частей файла
from sys import argv

# Получаем из командной строки путь к файлу, выработку в часах, ставку за час, премию
try:
    path = dirname(argv[0])
    output_file = join(path, 'Lesson-05-Task-05-output_data.txt')
    print(f'output: {output_file}')

except ValueError:
    # в случае если аргументов мало - сообщаем
    exit("Необходимо указать имя входного файла как первый параметр строки запуска скрипта")

# создаем исходный список случайных чисел
rand_list = [randint(0, 100) for i in range(100)]

# считаем сумму
totals = reduce(lambda el, el2: el + el2, rand_list)
print(f'Сумма всех чисел: {totals}')

# формируем исходну строку из списка - преобразовывая все значения к строке
out_str = " ".join([str(el) for el in rand_list])

try:
    # Открываем файл на запись
    output_file_obg = open(output_file, 'w', encoding='utf-8')
    output_file_obg.write(out_str)

except IOError:
    # в случае ошибки ввода вывода - сообщаем
    print("Ошибка ввода-вывода в файл")

finally:
    # не забываем закрывать файл
    output_file_obg.close()
