def calculator(mess):
    if len(mess) > 1:
        try:
            result = str(eval(mess))
        except Exception as err:
            print(err)
            res = "Error input!"
    else:
        res = "0"
    return result
