import os
from random import randint


def EndExercise():
    input("\npress enter to continue")
    os.system('cls')


def GetNumericFromConsole(text=""):
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


def CreateRandomList(min, max, size):
    return [randint(min, max+1) for x in range(size)]


def GardenBed():
    pcs = GetNumericFromConsole("Input pcs: ")
    bushes = CreateRandomList(20, 50, pcs)
    print(bushes)
    res = 0
    index = 0
    for i in range(3, len(bushes)+3):
        if len(bushes) < 3:
            print("not enough bushes ")
            break
        bushes = bushes[1:] + bushes[:1]
        tmp = bushes[0] + bushes[1] + bushes[2]
        if tmp > res:
            res = tmp
            index = i
    print("Maximum", res, "berries on bushs №", index-1, index, index+1)
    EndExercise()


def GetDublicatesInLists():
    sizeOne = GetNumericFromConsole("Input pcs: ")
    sizeTwo = GetNumericFromConsole("Input pcs: ")
    arr1: list[int] = CreateRandomList(0, 50, sizeOne)
    arr2: list[int] = CreateRandomList(0, 50, sizeTwo)
    print(sorted(arr1))
    print(sorted(arr2))
    res = []
    for item in set(arr2):
        if item in set(arr1):
            res.append(item)
    if len(res) == 0:
        res.append("nothing")
    print("Dubicates numbers -> ", res)
    EndExercise()


def ExserciseSelect():
    while True:
        num = GetNumericFromConsole(
            "input number exercise (22 or 24) or 0 to exit: ")
        if num == 22:
            GetDublicatesInLists()
        elif num == 24:
            GardenBed()
        elif num == 0:
            break
        else:
            print("input error")


ExserciseSelect()
