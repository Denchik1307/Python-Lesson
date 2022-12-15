import os

os.system('cls' if os.name == 'nt' else 'clear')


def Factorial(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


# print(Factorial(5))

# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
def Fibonacci(n):
    # 0 1 1 2 3 5 8
    # 1 2 3 4 5 6 7
    if n==0: return 1
    if n ==1: return 2,3
    number0 = 0
    number1 = 1
    count = 2
    while n >= number1:
        if n == number1: return count
        temp = number1
        number1 += number0
        number0 = temp
        count += 1
    return -1

# print(Fibonacci(5))

# Задача №13
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за 
# всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики 
# за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, 
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2
from random import randint

def Sinoptic(n):
    list = []

    for item in range(0,n):
        list.append(randint(-40,50))

    count = 0
    max = 0

    for item in list:
        if item > 0:
            count += 1
        if count > max:
            max = count
        if item < 0:
            count = 0
    return max


# print(Sinoptic(100))

def ArbuzLine(n):
    arbuzes=[]
    for _ in range(n):
        arbuzes.append(randint(5000,30000))
    arbuzes.sort()
    print(arbuzes)
    
    min=max=arbuzes[0]
    for item in arbuzes:
        if min>item: min = item
        elif max < item: max = item
    
    return min, max

print(ArbuzLine(10))

def ArbuzLineTwo(n):
    arbuzes=[]
    for _ in range(n):
        arbuzes.append(randint(5000,30000))
    arbuzes.sort()
    print(arbuzes)
    
    return arbuzes[0],arbuzes[-1]

    
print(ArbuzLineTwo(10))