import math
import click
import os
from random import randint


def clear() -> None: os.system('cls')


def end_exercise() -> None:
    input("\npress enter to continue")
    clear()


def get_positive_numeric_from_console(text="") -> int:
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


def get_numeric_from_console(text="") -> int:
    while True:
        try:
            res = int(input(text))
            break
        except ValueError:
            clear()
            print("Numbers only please!")
    return res


def create_random_list(minimal: int, maximal: int, size: int) -> list[int]:
    return [randint(minimal, maximal + 1) for _ in range(size)]


def is_prime(num) -> bool:
    for i in range(2, num >> 1):
        if num % i == 0:
            return False
    return True


def exercise101() -> None:
    num = 0.001
    pi = math.pi
    tmp = str(num).split(".")
    print(round(pi, len(tmp[1])))
    end_exercise()


def write_file(file: str, text: str) -> None:
    with open(file, "w") as file:
        file.write(text)


def exercise102() -> None:
    n = get_numeric_from_console("Insert number: ")
    print([num for num in range(1, n + 1) if n % num == 0], "all digit")
    print([num for num in range(1, n + 1) if n %
           num == 0 and is_prime(num)], "simple")
    end_exercise()


def exercise103() -> None:
    def make_formula(coefficient: int) -> str:
        list_num = create_random_list(0, 100, coefficient)
        size_list = len(list_num) - 1
        result = ''
        for i in list_num:
            tmp = str(i) if 1 != i != 0 else ""
            if size_list > 1:
                result += f"{tmp}x**{size_list} + "
            elif size_list == 1:
                result += f"{tmp}x + "
            elif size_list == 0:
                if i == 0:
                    result = result[:-3]
                    break
                else:
                    result += tmp
            size_list -= 1
        result += " = 0"
        return result

    coefficient_one = get_positive_numeric_from_console(
        "Input coefficient for file one: ")
    coefficient_two = get_positive_numeric_from_console(
        "Input coefficient for file two: ")

    write_file("104_file1.txt", make_formula(coefficient_one))
    write_file("104_file2.txt", make_formula(coefficient_two))
    print("File created")
    end_exercise()


def exercise104() -> None:
    def fun_to_dict(file: str) -> dict:
        with open(file, 'r') as file:
            poly = file.readline()
            poly_replaced = poly.replace(" ", "").replace(
                "=0", "").replace("\n", "").split("+")

        res_dict = {}
        for i in poly_replaced:
            if "x**" in i:
                res_dict[i[i.find("x") + 3]] = i[:i.find("*") - 1]
            elif "x" in i:
                res_dict[1] = i[:i.find("x")]
            elif "x" not in i:
                res_dict[0] = i
        return res_dict

    dic_one = fun_to_dict('104_file1.txt')
    dic_two = fun_to_dict('104_file2.txt')
    res = ""
    for key in dic_one:
        try:
            tmp = dic_two[key]
        except IndexError as e:
            print(e)
            tmp = "0"

        summa = int(dic_one[key]) - int(tmp)
        deg = f"x**{key}" if int(key) >= 2 else "x" if int(key) == 1 else ""
        plus_or_minus = " + " if summa >= 0 else " - "
        summa = summa if summa > 0 else summa * -1
        res += f"{plus_or_minus}{summa}{deg}"

    res += " = 0"
    write_file("104_result.txt", res)
    print("File created")
    end_exercise()


def exercise105() -> None:
    print([res for res in input("Input letters separate with space: ")
          .split() if "абв" not in res])
    end_exercise()


def exercise106() -> None:
    max_take_candy = 28
    candy: int = 2021
    print(f"There {candy} candies")
    is_player_one = True
    level = 0
    select_player = input("Input 1 or Yes for play with BOT: ").lower()
    is_bot = True if (select_player == "yes" or select_player == "1") else False
    if is_bot:
        while True:
            level = get_positive_numeric_from_console("Select level (low - hard -> 0 -> 3: ")
            if 0 <= level <= 3:
                break
            else:
                print("only number 0-3")
        level *= 3
    player_one = input("Input name first player: ")
    player_two = "BOT" if is_bot else input("Input name second player: ")

    def get_candy(player: str) -> int:
        while True:
            print("You need to take from 1 to 28 pcs")
            pcs_candies = get_positive_numeric_from_console(f"Take candies ({player}): ")
            if 28 >= pcs_candies >= 1:
                break
        return pcs_candies

    def play(pcs: int, take_pcs: int) -> int:
        pcs = pcs - take_pcs
        return pcs

    while True:
        message = f"Player {player_one}" if is_player_one else f"Player {player_two}"
        if candy > max_take_candy:
            print()
            if is_bot and not is_player_one:
                rand = candy % max_take_candy + level + randint(0, level)
                candies = play(candy, rand)
                clear()
                print(f"BOT takes {rand} candies")
            else:
                candies = play(candy, get_candy(message))
            print(f"there are {candies} candies left")
        else:
            print(message, "WIN")
            break
        is_player_one = not is_player_one
    end_exercise()


def exercise107() -> None:
    print(107)
    end_exercise()


def exercise108() -> None:
    print(108)
    end_exercise()


def exercise_select() -> None:
    while True:
        num = get_positive_numeric_from_console(
            "input number exercise (101, 102, 103, 104, 105, 106, 107 or 108) or 0 to exit: ")
        clear()
        if num == 101:
            exercise101()
        elif num == 102:
            exercise102()
        elif num == 103:
            exercise103()
        elif num == 104:
            exercise104()
        elif num == 105:
            exercise105()
        elif num == 106:
            exercise106()
        elif num == 107:
            exercise107()
        elif num == 108:
            exercise108()
        elif num == 0:
            break
        else:
            print("input error")
    clear()


exercise_select()
