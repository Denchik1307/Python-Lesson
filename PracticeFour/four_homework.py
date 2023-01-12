import os
from random import randint


def end_exercise():
    input("\npress enter to continue")
    os.system('cls')


def get_numeric_from_console(text=""):
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


def create_random_list(min_in_random, max_in_random, size):
    return [randint(min_in_random, max_in_random + 1) for _ in range(size)]


def garden_bed():
    pcs = get_numeric_from_console("Input pcs: ")
    bushes = create_random_list(20, 50, pcs)
    print(bushes)
    res = 0
    index = 0
    for i in range(3, len(bushes) + 3):
        if len(bushes) < 3:
            print("not enough bushes ")
            break
        bushes = bushes[1:] + bushes[:1]
        tmp = bushes[0] + bushes[1] + bushes[2]
        if tmp > res:
            res = tmp
            index = i
    print("Maximum", res, "berries on bush`s №", index - 1, index, index + 1)
    end_exercise()


def get_duplicates_in_lists():
    size_one = get_numeric_from_console("Input size list one (pcs): ")
    size_two = get_numeric_from_console("Input size list two (pcs): ")
    arr1: list[int] = create_random_list(0, 50, size_one)
    arr2: list[int] = create_random_list(0, 50, size_two)
    print(sorted(arr1))
    print(sorted(arr2))
    res = []
    for item in set(arr2):
        if item in set(arr1):
            res.append(item)
    if len(res) == 0:
        res.append("nothing")
    print("Duplicates numbers -> ", sorted(res))
    end_exercise()


def exercise_select():
    while True:
        num = get_numeric_from_console(
            "input number exercise (22 or 24) or 0 to exit: ")
        if num == 22:
            get_duplicates_in_lists()
        elif num == 24:
            garden_bed()
        elif num == 0:
            break
        else:
            print("input error")


exercise_select()
