import os
from random import randint
os.system('cls')


def getNumericFromConsole(text=""):
    while True:
        try:
            res = int(input(text))
            break
        except ValueError:
            print("Numbers only please!")
    return res


def ArrayRandom(n: int, rangeMin: int = 0, rangeMax: int = 100):
    resArr = []
    for i in range(n):
        resArr.append(randint(rangeMin, rangeMax))
    return resArr


def CountNumber():
    arrSize = getNumericFromConsole("Input size arr: ")
    arr = ArrayRandom(arrSize, rangeMin=1, rangeMax=arrSize >> 1)
    arr = sorted(arr)
    num = getNumericFromConsole("input number for count repit digit: ")
    count = 0
    for i in arr:
        if num == i:
            count += 1
        if num < i:
            break
    print(arr)
    print(count)


def Scrabble():
    word = input("Input your word: ")
    lib = \
        {"AEIOULNSTRАВЕИНОРСТ": 1,
         "DGДКЛМПУ": 2,
         "BCMPБГЁЬЯ": 3,
         "FHVWYЙЫ": 4,
         "KЖЗХЦЧ": 5,
         "JXШЭЮ": 8,
         "QZФЩЪ": 10}
    count = 0
    for i in word:
        for val, key in enumerate(lib.keys()):
            if str(i).upper() in key:
                count += lib[key]
    print(count)


def FindNearDigit():
    arrSize = getNumericFromConsole("Input size arr: ")
    arr = ArrayRandom(arrSize, rangeMin=1, rangeMax=arrSize >> 1)
    arr = sorted(arr)
    num = getNumericFromConsole("input number for find near digit: ")
    max = min = 0
    for i in arr:
        if i < num:
            min = i
        if i > num:
            max = i
            break
    print(arr, max-num, num-min)
    print(min if num-min <= max - num or max == 0 else max)


def ExserciseSelect():
    while True:
        num = getNumericFromConsole(
            "16 CountNumber\n18 FindNearDigit\n20 Scrabble\nInput number exercise (16, 18 or 20) or 0 to exit: ")
        if num == 16:
            CountNumber()
        elif num == 18:
            FindNearDigit()
        elif num == 20:
            Scrabble()
        elif num == 0:
            break
        else:
            print("input error")


ExserciseSelect()
