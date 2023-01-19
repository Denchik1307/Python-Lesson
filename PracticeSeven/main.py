from function import *
from menu import Menu

if __name__ == "__main__":
    menu_items = [
        ("1", "Вывод автобусов", print_bus),
        ("2", "Добавление автобуса", add_bus),
        ("3", "Вывод водителей", print_driver),
        ("4", "Добавление водителя", add_driver),
        ("5", "Вывод маршрутов", print_route),
        ("6", "Добавление маршрута", add_route),
        ("0", "Выход", close_program)]

    menu = Menu(menu_items)
    menu.run("сделайте выбор: ")
