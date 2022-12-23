import os
from random import randint
# import emojize
os.system('cls' if os.name == 'nt' else 'clear')


def GetNumericFromConsole(text=""):
    res = -1
    while res < 0:
        try:
            res = int(input(text))
            if res<0:
                print("need number >= 0")
            else:
                break
        except ValueError:
            print("Numbers only please!")
    return res


def Gryadka():
    pcs = GetNumericFromConsole("Input pcs: ")
    bushes = [randint(50, 200) for x in range(pcs)]
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
    print(res, "berries on bushs №", index-1, index, index+1)


def Money():
    sizeOne = GetNumericFromConsole("Input pcs: ")
    sizeTwo = GetNumericFromConsole("Input pcs: ")
    arr1 = [randint(0,50) for x in range(sizeOne)]
    arr2 = [randint(0,50) for x in range(sizeTwo)]
    print(sorted(arr1))
    print(sorted(arr2))
    res = []
    for item in set(arr2):
        if item in set(arr1):
            res.append(item)
    if len(res)==0:
        res.append("nothing")
    print(res)


def ExserciseSelect():
    while True:
        num = GetNumericFromConsole(
            "input number exercise (22 or 24) or 0 to exit: ")
        if num == 22:
            Money()
        elif num == 24:
            Gryadka()
        elif num == 0:
            break
        else:
            print("input error")


ExserciseSelect()
