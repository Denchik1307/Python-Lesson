import os
os.system('cls' if os.name == 'nt' else 'clear')


def getNumericFromConsole(text):
    while True:
        try:
            res = int(input(text))
            break
        except ValueError:
            print("Numbers only please!")
    return res


def SummDigitNum():
    result = 0
    num = getNumericFromConsole("input triple number: ")
    num = str(num)
    if len(num) != 3:
        print("wrong input!!!")
    else:
        for item in num:
            result += int(item)
    print("summ digit =", result)


def LuckyTicket():
    firstHalf = 0
    secondHalf = 0
    isLucky = False
    ticket = getNumericFromConsole("input number ticket: ")
    ticket = str(ticket)
    if len(ticket) != 6 and int(ticket):
        print("you made a mistake!!!")
    else:
        for item in ticket[:3]:
            firstHalf += int(item)
        for item in ticket[3:]:
            secondHalf += int(item)
        if secondHalf == firstHalf:
            isLucky = True
    print("Yes" if isLucky else "No")


def Aists():
    allAists = getNumericFromConsole("input all aists: ")
    katy = int((allAists/3)*2)
    petya = int((katy/2)/2)
    sergey = int(petya)
    if allAists % 6 == 0:
        print("\nPetya", petya, "\nKaty", katy, "\nSergey", sergey)
    else:
        print("wrong quantity aists")


def ChokolateCut():
    print("input size chocolate N x M : ")
    n = getNumericFromConsole("inut N: ")
    m = getNumericFromConsole("inut M: ")
    k = getNumericFromConsole("input K: ")
    if k % n or k % m:
        print("Yes")
    else:
        print("No")


def ExserciseSelect(num):
    if num == 2:
        SummDigitNum()
    elif num == 4:
        Aists()
    elif num == 6:
        LuckyTicket()
    elif num == 8:
        ChokolateCut()
    else:
        print("input error")


ExserciseSelect(getNumericFromConsole("input number exercise (2,4,6 or 8)"))
