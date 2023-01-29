# Создать информационную систему позволяющую работать с учениками школы# функции
# Добавление нового студента (Поля - имя, фамилия)
# Добавление предмета (добавляется всем ученикам сразу)
# Добавление оценки ученику по предмету (выбираем ученика(из существующих), выбираем предмет(из сущ.),пишем оценку )
# Показ списка учеников (имена фамилия)
# Показ листа оценок конкретного ученика
# Выход из программы
# Достаточно хранить данные в переменной

import view

#main dct = {"FI":{"MATH":[3,4,5], "PHISC": [2,3,2]}, "FI":}
main_dct = {}
student_name = []
lessons = []

def start():
    while True:
        op = view.get_op()  # вывод меню
        if op == 1:
            student = view.input_student() # ввод студента
            if student not in student_name:         # проверка на повторы
                student_name.append(student) 
                main_dct[student] = {}
                if lessons:
                    for less in lessons:
                        main_dct[student][less]=[]  # добавление предмета в словарь        
        elif op == 2:
            less = view.input_less()
            lessons.append(less)  # добавление предмета кот. ввели
            for name in student_name:
                main_dct[name][less] = []
        elif op == 3:
            name, less, mark = view.input_mark()
            main_dct[name][less].append(mark)
        elif op == 4:
            print(main_dct)
        elif op == 5:
            name = view.get_name_to_show()
            print(f"Оценки {name} - {main_dct[name]}")
        elif op == 6:
            break
     


