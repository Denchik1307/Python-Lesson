import random

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
is_first = True


def first_move():
    global matrix, is_first
    is_first = False
    matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show_matrix():
    global matrix
    return f'{matrix[0]} | {matrix[1]} | {matrix[2]}' \
           f'\n—  —  —' \
           f'\n{matrix[3]} | {matrix[4]} | {matrix[5]}' \
           f'\n—  —  —' \
           f'\n{matrix[6]} | {matrix[7]} | {matrix[8]}'


def check_win():
    global matrix
    if matrix[0] == matrix[1] == matrix[2] or matrix[0] == matrix[3] == matrix[6]:
        return f'Winner {matrix[0]}\n'
    elif matrix[0] == matrix[4] == matrix[8] \
            or matrix[1] == matrix[4] == matrix[7] \
            or matrix[2] == matrix[4] == matrix[6] \
            or matrix[3] == matrix[4] == matrix[5]:
        return f'Winner {matrix[8]}\n'
    elif matrix[6] == matrix[7] == matrix[8]:
        return f'Winner {matrix[8]}\n'
    else:
        return -1


def player(number):
    global matrix
    # print(matrix, " user before")
    index = int(number) - 1
    if (matrix[index] != 'X') and (matrix[index] != 'O'):
        matrix[index] = 'X'
        # print(matrix, " user after")
        return 1
    else:
        return 0


def comp():
    global matrix
    # print(matrix, " bot before")
    index = 0
    # for i in range(0, len(input_matrix)):
    while True:
        index += 1
        if (matrix[index] != 'X') and (matrix[index] != 'O'):
            matrix[index] = 'O'
            # print(matrix, " bot after")
            if index >= len(matrix):
                return ""
            return f"\nI move to {index + 1}\n"


def check_end_game():
    global matrix
    for i in matrix:
        if i != "X" or i != "O":
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
    if (win := check_win()) != -1:
        temp = win
        is_first = True
        temp += show_matrix()
        first_move()
        temp += "\n\nNew game\n"
    temp += show_matrix()
    return temp
    # if is_wrong == 0:
    #     return show_matrix() + "\nYou cant take this cell"
    # response_bot = comp()
    # return response_bot + show_matrix() + "\nYour move"

# print(show_matrix())
# while True:
#     print(player(int(input("><")))+1)
#     print(show_matrix())
#     if check_win() == 1:
#         break
#     print(comp())
#     print(show_matrix())
#     if check_win() == 1:
#         break
