import os
os.system('cls' if os.name == 'nt' else 'clear')

def Distance():
    n = 700
    m = 701
    result = (m + n - 1) // n
    print(result)

Distance()

def CountTable():
    classA = int(input("Кол-во учеников класса A"))
    classB = int(input("Кол-во учеников класса Б"))
    classC = int(input("Кол-во учеников класса B"))
    result = (classA + classB + classC + 1) // 2
    print(result)

CountTable()

def Locomotive():
    i = int(input("порядковый номер вагона: "))
    j = int(input("номер на вагоне: "))
    result = i + j - 1
    print(result, "вагонов")

Locomotive()

def IsHighYear():
    i = int(input("Введите год: "))
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print('YES')
    else:
        print('NO')

IsHighYear()

