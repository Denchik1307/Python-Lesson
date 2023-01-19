from texttable import Texttable


class Menu:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def print(self):
        table = Texttable()
        for x, y, _ in self.elements:
            table.add_row([x, y])
        print(table.draw())
        # create_table(, ["номер для ввода", "операция"])

    def run(self, msg=': '):
        while True:
            self.print()
            user_choice = input(msg)
            for (mark, _, run_method) in self.elements:
                if user_choice == mark:
                    run_method()
                    break
