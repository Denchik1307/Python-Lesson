from texttable import Texttable


def read_data_from_file(file_name: str) -> list[str]:
    with open(file_name, 'r', encoding='utf-8') as datafile:
        result = datafile.read().strip().split("\n")
    return result


def save_data_to_file(file_name: str, data_list: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as datafile:
        datafile.write(data_list.strip(" ") + '\n')


def create_table(items, header) -> None:
    table = Texttable()
    table.add_row([item for item in header])
    for item in items:
        table.add_row(item.split(","))
    print(table.draw())
    input("Нажмите ввод для продолжения")


def print_bus() -> None:
    create_table(read_data_from_file('bus.txt'), ["автобус", "гос. номер"])


def add_bus() -> None:
    save_data_to_file('bus.txt', input("Введите\n(номер автобуса,гос.номер автобуса): "))


def print_driver() -> None:
    create_table(read_data_from_file("driver.txt"), ["водитель", "фамилия"])


def add_driver() -> None:
    save_data_to_file('driver.txt', input("Введите\n(номер водителя,фамилия водителя): "))


def print_route() -> None:
    create_table(read_data_from_file('marshrut.txt'), ["маршрут", "длинна", "автобус", "водитель"])


def add_route() -> None:
    save_data_to_file('route.txt', input("Введите\n(маршрут,длинна,автобус,водитель): "))


def close_program():
    exit()
