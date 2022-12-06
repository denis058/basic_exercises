# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
names = [student['first_name'] for student in students]

for name in set(names):
    print(f'{name}: {names.count(name)}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = [student['first_name'] for student in students]

for name in set(names):
    if names.count(name) > 1:
        print(f'Самое частое имя среди учеников: {name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
school_students_one = school_students[0]
names = [student['first_name'] for student in school_students_one]

for name in set(names):
    if names.count(name) > 1:
        print(f'Самое частое имя в классе 1: {name}')

school_students_one = school_students[1]
names = [student['first_name'] for student in school_students_one]

for name in set(names):
    if names.count(name) > 1:
        print(f'Самое частое имя в классе 2: {name}')       
  
school_students_one = school_students[2]
names = [student['first_name'] for student in school_students_one]

for name in set(names):
    if names.count(name) > 1:
        print(f'Самое частое имя в классе 3: {name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
count_male = 0
count_female = 0
for students in school:
    for student in students['students']:
        if is_male[student['first_name']]:
            count_male += 1
        else:
            count_female += 1
    print(f'Класс {students["class"]}: девочки {count_female}, мальчики {count_male}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
count_male = 0
count_female = 0
for students in school:
    if count_male < count_female:
        print(f'Больше всего мальчиков в классе {students["class"]}')
    else:
        print(f'Больше всего девочек в классе {students["class"]}')
    for student in students['students']:
        if is_male[student['first_name']]:
            count_male += 1
        else:
            count_female += 1

