import random


def get_cipher():
    n = int(input('>> '))
    res = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                res += str(i)
                res += str(j)

    print(res)


get_cipher()
