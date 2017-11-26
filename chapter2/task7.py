# coding=utf-8
import numpy as np

from data.f2_matrix import F2Matrix


def multiply(msg, matrix):
    return np.remainder(np.dot(msg, matrix.matrix), 2)


def ones(msg):
    count = 0
    for elem in msg:
        count += elem
    return count


def to_str(v):
    return ''.join([str(i) for i in v])


if __name__ == '__main__':
    matrix = F2Matrix([
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1]
    ])

    matrix = matrix.transpose()
    print matrix

    table = {}
    for i in range(1024):
        msg = [int(j) for j in '{0:010b}'.format(i)]
        syn = to_str(multiply(msg, matrix).tolist())
        if syn not in table:
            table[syn] = msg
        elif ones(table[syn]) > ones(msg):
            table[syn] = msg
    for k, v in sorted(table.items()):
        str_v = to_str(v)
        print "{}           {}".format(k, str_v)
