def get_op():
    op = int(input(" 1 - добавить студента\n 2 - добавить предмет\n 3 - добавить оценку\n 4 - показать список\n 5 - показать конкретный список\n 6 - выход\n"))
    return op

def input_student():
      name = input("Введите имя и фамилию: ")  
      return name

def input_less():
    less = input("Ввведите предмет: ")
    return less

def input_mark():
    name = input("Введите имя и фамилию: ")
    less = input("Введи предмет:")
    mark = input("Введи оценку: ")
    return name, less, mark

def get_name_to_show():
    name = input("Введи имя и фамилию для просмотра оценок: ")
    return name
