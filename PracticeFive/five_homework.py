def get_positive_num_from_console(text=""):
    res = -1
    while res < 0:
        try:
            res = int(input(text))
            if res < 0:
                print("need number >= 0")
            else:
                break
        except ValueError:
            print("Numbers only please!")
    return res


def exercise_26():
    first_num = get_positive_num_from_console("Input number: ")
    second_num = get_positive_num_from_console("Input pow: ")

    def my_pow(a: int, b: int):
        if b == 0:
            return 1
        if b == 1:
            return a
        else:
            return a * my_pow(a, b - 1)

    print(my_pow(first_num, second_num))


def exercise_28():
    first_num = get_positive_num_from_console("Input first number: ")
    second_num = get_positive_num_from_console("Input second number: ")

    def my_summa(a: int, b: int):

        if b == 0:
            return a
        else:
            # b -= 1
            # a += 1
            return my_summa(a + 1, b - 1)

    print(my_summa(first_num, second_num))


def exercise_select():
    while True:
        num = get_positive_num_from_console(
            "input number exercise (26 or 28) or 0 to exit: ")
        if num == 26:
            exercise_26()
        elif num == 28:
            exercise_28()
        elif num == 0:
            break
        else:
            print("input error")


exercise_select()
