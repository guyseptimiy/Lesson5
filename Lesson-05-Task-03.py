# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

# Импортируем работы с аргументами
from sys import argv

# Получаем из командной строки путь к файлу, выработку в часах, ставку за час, премию
try:
    name, output_file = argv  # в каталоге исходников для урока - Lesson-05-Task-03-data.txt

except ValueError:
    # в случае если аргументов мало - сообщаем
    exit("Необходимо указать имя входного файла как первый параметр строки запуска скрипта")

try:

    # Открываем файл на чтение
    file_obg = open(output_file, 'r', encoding='utf-8')

    employee_totals = 0
    salary_fronter = 20000.00
    salary_totals = 0

    # обходим все строки в файле
    for file_line in file_obg:
        employee_totals += 1

        # Получаем слова из строки деля слова по пробелу
        employee_record = file_line.split()
        initials = employee_record[0]
        salary = float(employee_record[1])

        salary_totals += salary

        if salary < salary_fronter:
            # выводим данные о текущей строке
            print(f'Зарплата сотрудника меноше меньше {salary_fronter} ({initials} - {salary})')

    print(f'Средняя зараотная плата {salary_totals / employee_totals}')

except IOError:
    # в случае ошибки ввода вывода - сообщаем
    print("Ошибка ввода-вывода в файл")

finally:
    # не забываем закрывать файл
    file_obg.close()
