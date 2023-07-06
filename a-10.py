import random

saikoro = [1, 2, 3, 4, 5, 6]

# print(dice(saikoro))

# 下記も可能
# def dice():
#    return random.choice(saikoro)


def dice():
    return random.randint(1, 6)

print(dice())
