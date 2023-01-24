def sort_names():
    with open("worker_list.txt", "r") as file:
        lst = file.readlines()
        lst_with_lst = []
        for line in lst:
            a = line.strip().split(",")
            lst_with_lst.append(a)

        # сортировка по имени - x[1]
        lst_with_lst = sorted(lst_with_lst, key=lambda x: x[1])
        string_ = ""
        for worker in lst_with_lst:             # worker - внутренний список
            # join соединяет все эл-ты списка через "," и формирует строку
            res = ",".join(worker)
            string_ += res + "\n"
    with open("worker_list.txt", "w") as file:
        file.write(string_)


def sort_id():
    with open("worker_list.txt", "r") as file:
        lst = file.readlines()
        lst_with_lst = []
        for line in lst:
            a = line.strip().split(",")
            lst_with_lst.append(a)
        # сортировка по id - x[0]
        lst_with_lst = sorted(lst_with_lst, key=lambda x: x[0])
        string_ = ""
        for worker in lst_with_lst:             # worker - внутренний список
            # join соединяет все эл-ты списка через "," и формирует строку
            res = ",".join(worker)
            string_ += res + "\n"
    with open("worker_list.txt", "w") as file:
        file.write(string_)
