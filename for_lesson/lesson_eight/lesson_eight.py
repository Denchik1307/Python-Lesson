def calculate(a, b, sign):
    a = float(a)
    b = float(b)
    res = ""
    match sign:
        case "+":
            res = str(a + b)
        case "-":
            res = str(a - b)
        case "*":
            res = str(a * b)
        case "/":
            res = str(a / b)
    return res


def preparation(example_input):
    list_example = []
    tmp = ""
    for i in example_input:
        if i.isdigit():
            tmp += i
        else:
            list_example.append(tmp)
            tmp = ""
        if i in "()+-/*":
            list_example.append(i)
    list_example.append(tmp)
    while "" in list_example:
        list_example.remove("")
    return list_example


def get_res(input_list):
    if input_list[0] == "-":
        input_list[1] = str(-int(input_list[1]))
        input_list.pop(0)
    while "*" in input_list or "/" in input_list:
        for i in range(0, len(input_list) - 2, 2):
            if len(input_list)-2 <= i: break
            if input_list[i + 1] in "*/":
                input_list[i] = str(calculate(input_list[i], input_list[i + 2], input_list[i + 1]))
                input_list.pop(i + 1)
                input_list.pop(i + 1)
    while "+" in input_list or "-" in input_list:
        input_list[0] = str(calculate(input_list[0], input_list[2], input_list[1]))
        input_list.pop(1)
        input_list.pop(1)

    return input_list


def remove_other(input_for_remove):
    while "(" in input_for_remove:
        first = len(input_for_remove) - 1 - input_for_remove[::-1].index("(")
        second = input_for_remove[first:].index(")") + first
        start = input_for_remove[: first]
        end = input_for_remove[second + 1:]
        tmp = input_for_remove[first + 1: second]
        if tmp[0] == "-":
            tmp[1] = str(-int(tmp[1]))
            tmp.pop(0)
        xxx = get_res(tmp)

        input_for_remove.clear()
        input_for_remove.extend(start)
        input_for_remove.extend(xxx)
        input_for_remove.extend(end)

    return get_res(input_for_remove)


n = "-22+300-((-14-5)*5)/2 +5"
example = n.replace(" ", "")
prepare = preparation(example)
print(remove_other(prepare))
