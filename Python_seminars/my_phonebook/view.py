def get_op():           # ввод меню пользователя
    op = int(input(" 1 - добавить пользователя\n 2 - вывести таблицу\n 3 - вывести только имя и фамилию\n 4 - отсортировать по именам\n 5 - отсортировать по id\n 6 - выход\n"))
    return op


def add_worker():                       # добавление пользователя
    id = input("Введите id: ")
    name = input("Введите имя: ")
    lastname = input("Введите фамилию: ")
    number = input("Введите номер телефона: ")
    comments = input("Введите комментарий: ")
    line = f"{id}, {name}, {lastname}, {number}, {comments}\n"
    with open("worker_list.txt", 'a', encoding="utf-8") as file:
        file.write(line)
    print("сохранено!")


def print_table():
    with open("worker_list.txt", "r", encoding="utf-8")as file:
        for line in file.readlines():                  # проход по строкам файла
            print(line, end="")


def print_only_name():                                  # вывод фамилии и имени
    with open("worker_list.txt", 'a', encoding="utf-8") as file:
        lst = file.readlines()
        print(lst)
        for line in lst:
            a = line.split(",")
            print(f"Имя - {a[1]}, Фамилия - {a[2]}")
