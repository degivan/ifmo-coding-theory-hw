from chapter4.task2 import count_p


def find_probability(left, right, eps, probability):
    mid = (left + right) / 2
    if (right - left) < eps:
        return mid
    value = count_p(mid)
    if probability > value:
        return find_probability(left, mid, eps, probability)
    else:
        return find_probability(mid, right, eps, probability)


if __name__ == '__main__':
    print find_probability(0.6, 10.0, 10 ** (-7), 10 ** (-5))
