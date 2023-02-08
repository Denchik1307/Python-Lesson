import random

from texttable import Texttable

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
is_first = True

_x_cell = "x"
_o_cell = "o"


def first_move():
    global matrix, is_first
    is_first = False
    matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_matrix():
    global matrix
    place = Texttable()
    place.add_row([matrix[0], matrix[1], matrix[2]])
    place.add_row([matrix[3], matrix[4], matrix[5]])
    place.add_row([matrix[6], matrix[7], matrix[8]])
    return place.draw()


def check_win():
    global matrix
    if matrix[0] == matrix[1] == matrix[2] or matrix[0] == matrix[3] == matrix[6]:
        return f'Winner "{matrix[0]}"\n'
    elif matrix[0] == matrix[4] == matrix[8] \
            or matrix[1] == matrix[4] == matrix[7] \
            or matrix[2] == matrix[4] == matrix[6] \
            or matrix[3] == matrix[4] == matrix[5]:
        return f'Winner "{matrix[4]}"\n'
    elif matrix[6] == matrix[7] == matrix[8] or matrix[3] == matrix[5] == matrix[8]:
        return f'Winner "{matrix[8]}"\n'
    else:
        return -1


def player(number):
    global matrix
    index = int(number) - 1
    if (matrix[index] != _x_cell) or (matrix[index] != _o_cell):
        matrix[index] = _x_cell
        return 1
    else:
        return 0


def comp():
    global matrix
    dog_watch = 0
    while True:
        index = random.randint(0, 8)
        if dog_watch > 30:
            return "I can`t move\n"
        if (matrix[index] != _x_cell) or (matrix[index] != _o_cell):
            matrix[index] = _o_cell
            return f"\nI move to {index + 1}\n"
        dog_watch += 1


def check_end_game():
    global matrix
    for i in matrix:
        if i != _x_cell or i != _o_cell:
            return -1
        else:
            return 1


def start_game(msg):
    global is_first
    temp = ""
    if is_first:
        first_move()
    if 9 >= int(msg) >= 1:
        if player(msg) != 0:
            temp += comp()
        else:
            temp = "Wrong cell\n"
    else:
        temp = "Wrong input\n"
    if (win := check_win()) != -1:
        temp = win
        is_first = True
        temp += show_matrix()
        first_move()
        temp += "\n\nNew game\n"
    temp += show_matrix()
    return temp

