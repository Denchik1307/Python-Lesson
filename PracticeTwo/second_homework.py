import os
from random import randint
os.system('cls' if os.name == 'nt' else 'clear')


def getNumericFromConsole(text=""):
    while True:
        try:
            res = int(input(text))
            break
        except ValueError:
            print("Numbers only please!")
    return res


def GuessTheNumber():
    summ = getNumericFromConsole("enter the sum of the hidden numbers: ")
    mult = getNumericFromConsole(
        "enter the multiplication of the hidden numbers: ")
    ran = range(0, 1001)
    list = []
    isFind = False

    for i in ran:
        if isFind:
            break
        for j in ran:
            if i*j == mult and i+j == summ:
                list.append(i)
                list.append(j)
                isFind = True
                break

    if len(list) < 1:
        list.append("something's wrong")

    print(list)


def Degrees():
    num = getNumericFromConsole("enter a number: ")
    res = []
    tmp = 2

    while tmp < num:
        res.append(tmp)
        tmp <<= 1
    print(res)


def Money():
    n = 0
    while n < 1:
        n = getNumericFromConsole("enter the number of coins on the table: ")
        if n < 2:
            print("need <0")

    list = []

    for i in range(0, n):
        list.append("head" if randint(0, 1) == 1 else "tail")

    print(list)
    count = 0

    for item in list:
        if item == "head":
            count += 1

    if len(list) == 1 or count == len(list) or count == 0:
        print("turn nothing")
    elif count > n >> 1:
        print("turn tail")
    elif count < n+1 >> 1:
        print("turn heads")
    else:
        print("turn any (tails or heads)")
    print(count, len(list))


def ExserciseSelect():
    while True:
        num = getNumericFromConsole(
            "input number exercise (10, 12 or 14) or 0 to exit: ")
        if num == 10:
            Money()
        elif num == 12:
            GuessTheNumber()
        elif num == 14:
            Degrees()
        elif num == 0:
            break
        else:
            print("input error")


ExserciseSelect()
