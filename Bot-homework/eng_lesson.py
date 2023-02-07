import random


def get_world_random():
    def _get_dict():
        with open(file="ENRUS.TXT", mode="r") as file:
            text = file.read()
            lib = {}
            while "  " in file:
                text.replace("  ", " ")
            tmp = text.replace("\t", " ").split("\n")
            for i in range(0, len(tmp) - 1, 2):
                lib[tmp[i]] = tmp[i + 1]
        return lib

    lib = _get_dict()
    keys = []
    for key in lib.keys():
        keys.append(key)
    # print(keys)
    rand_key = random.choice(keys)
    # print(rand_key)
    return f"{rand_key}\n{lib[rand_key]}"
