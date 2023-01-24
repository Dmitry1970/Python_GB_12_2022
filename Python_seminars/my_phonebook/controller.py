import view
import sorting


def start():
    while True:
        op = view.get_op()  # просмотр числа пользователя
        if op == 1:
            view.add_worker()
        elif op == 2:
            view.print_table()
        elif op == 3:
            view.print_only_name()
        elif op == 4:
            sorting.sort_names()
        elif op == 5:
            sorting.sort_id()
        elif op == 6:
            break
