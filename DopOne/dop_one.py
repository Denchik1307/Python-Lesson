import os
import math
import re
from random import randint

def Clear() -> None: os.system('cls')

def EndExercise() -> None:
    input("\npress enter to continue")
    Clear()

def GetPositiveNumericFromConsole(text="") -> int:
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

def GetNumericFromConsole(text="") -> int:
    while True:
        try:
            res = int(input(text))
            break
        except ValueError:
            Clear()
            print("Numbers only please!")
    return res

def CreateRandomList(min: int, max: int, size: int):
    return [randint(min, max + 1) for x in range(size)]

def IsPrime(num) -> bool:
    for i in range(2, num >> 1):
        if num % i == 0:
            return False
    return True

def Exercise101() -> None:
    num = 0.001
    pi = math.pi
    tmp = str(num).split(".")
    print(round(pi, len(tmp[1])))
    EndExercise()

def WriteFile(file: str, text: str) -> None:
    with open(file, "w") as file:
        file.write(text)

def Exercise102() -> None:
    n = GetNumericFromConsole("Insert number: ")
    print([num for num in range(1, n + 1) if n % num == 0], "все целые")
    print([num for num in range(1, n + 1) if n %
          num == 0 and IsPrime(num)], "простые")
    EndExercise()

def Exercise103() -> None:
    def MakeFormula(coeff: int) -> str:
        listNum = CreateRandomList(0, 100, coeff)
        sizeList = len(listNum)-1
        result = ''
        for i in listNum:
            tmp = str(i) if 1 != i != 0 else ""
            if sizeList > 1:
                result += f"{tmp}x**{sizeList} + "
            elif sizeList == 1:
                result += f"{tmp}x + "
            elif sizeList == 0:
                if i == 0:
                    result = result[:-3]
                    break
                else:
                    result += tmp
            sizeList -= 1
        result += " = 0"
        return result

    coeffOne = GetPositiveNumericFromConsole(
        "Input coefficient for file one: ")
    coeffTwo = GetPositiveNumericFromConsole(
        "Input coefficient for file two: ")

    WriteFile("104_file1.txt", MakeFormula(coeffOne))
    WriteFile("104_file2.txt", MakeFormula(coeffTwo))
    print("File created")
    EndExercise()

def Exercise104() -> None:

    def FunToDict(file: str) -> dict:
        with open(file, 'r') as file:
            poly = file.readline()
            polyReplased = poly.replace(" ", "").replace(
                "=0", "").replace("\n", "").split("+")

        resDict = {}
        for i in polyReplased:
            if "x**" in i:
                resDict[i[i.find("x")+3]] = i[:i.find("*")-1]
            elif "x" in i:
                resDict[1] = i[:i.find("x")]
            elif "x" not in i:
                resDict[0] = i
        return resDict

    dicOne = FunToDict('104_file1.txt')
    dicTwo = FunToDict('104_file2.txt')
    res = ""
    tmp = ""
    for key in dicOne:
        try:
            tmp = dicTwo[key]
        except:
            tmp = "0"

        sum = int(dicOne[key]) - int(tmp)
        deg = f"x**{key}" if int(key) >= 2 else "x" if int(key) == 1 else ""
        znak = " + " if sum >= 0 else " - "
        sum = sum if sum > 0 else sum * -1
        res += f"{znak}{sum}{deg}"

    res += " = 0"
    WriteFile("104_result.txt",res)
    print("File created")
    EndExercise()

def Exercise105() -> None:
    print([res for res in input(
        """\"\"\"Напишите программу, удаляющую из текста все слова,
содержащие "абв" \"\"\"
введите слова разделяя пробелом: """).split() if "абв" not in res])
    EndExercise()

def Exercise106() -> None:
    maxTakeCandys = 28
    candys: int = 2021
    print(f"There {candys} candys")
    isPlayerOne = True
    selectPlayer = input("Input 1 or Yes for play with BOT: ").lower()
    isBot = True if (selectPlayer == "yes" or selectPlayer == "1") else False
    if isBot:
        while True:
            level = GetPositiveNumericFromConsole("Select level (low - hard -> 0 -> 3: ")
            if 0 <= level <= 3:
                break
            else:
                print("only number 0-3")
        level *= 3
    playerOne = input("Input name first player: ")
    playerTwo = "BOT" if isBot else input("Input name second player: ")

    def GetCandys(player: str) -> int:
        candy = -1
        while (True):
            print(msg := "You need to take from 1 to 28 pcs")
            candy = GetPositiveNumericFromConsole(f"Take candys ({player}): ")
            if 28 >= candy >= 1:
                break
        return candy

    def Play(candys: int, takePCS: int) -> int:
        candys = candys - takePCS
        return candys

    while (True):
        message = f"Player {playerOne}" if isPlayerOne else f"Player {playerTwo}"
        if candys > maxTakeCandys:
            print()
            if isBot and not isPlayerOne:
                rand = candys%maxTakeCandys + level + randint(0, level)
                candys = Play(candys, rand)
                Clear()
                print(f"BOT takes {rand} candys")
            else:
                candys = Play(candys, GetCandys(message))
            print(f"there are {candys} candies left")
        else:
            print(message, "WIN")
            break
        isPlayerOne = not isPlayerOne
    EndExercise()

def Exercise107() -> None:
    print(107)
    EndExercise()

def Exercise108() -> None:
    print(108)
    EndExercise()

def ExserciseSelect() -> None:
    while True:
        num = GetPositiveNumericFromConsole(
            "input number exercise (101, 102, 103, 104, 105, 106, 107 or 108) or 0 to exit: ")
        Clear()
        if num == 101:
            Exercise101()
        elif num == 102:
            Exercise102()
        elif num == 103:
            Exercise103()
        elif num == 104:
            Exercise104()
        elif num == 105:
            Exercise105()
        elif num == 106:
            Exercise106()
        elif num == 107:
            Exercise107()
        elif num == 108:
            Exercise108()
        elif num == 0:
            break
        else:
            print("input error")
    Clear()

ExserciseSelect()
