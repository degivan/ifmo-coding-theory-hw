from random import random

from scipy.stats import norm

from utils.decoder import Decoder, generate_sequences, np_to_str
import numpy as np
import matplotlib.pyplot as plt

N = 10 ** 3


def spoil_codeword(codeword, p):
    result = []
    for i in codeword:
        if random() < p:
            result.append((i + 1) % 2)
        else:
            result.append(i)
    return result


def difference(a, b):
    count = 0
    for x, y in zip(a, b):
        count += (x != y)
    return count


def bit_error_probability(p, matrix):
    decoder = Decoder(p, matrix)
    diff = 0
    k = len(matrix)
    for i in range(N):
        sequences = generate_sequences(k)
        for sequence in sequences:
            codeword = np.mod(np.sum(np.multiply(matrix, sequence), axis=0), 2)
            received = np_to_str(spoil_codeword(codeword, p))
            diff += difference(sequence.tolist(), [[int(j)] for j in decoder.decode(received)])
    return diff / float((N * k * (2 ** k)))


if __name__ == '__main__':
    matrix = np.array([[0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
              [1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
              [0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 1, 0, 0, 0, 1]])
    X = []
    Y = []
    for val in [0.1 * (i + 2) for i in range(70)]:
        p = 1 - norm.cdf(np.sqrt(2 * val))
        X.append(10 * np.log10(val))
        Y.append(bit_error_probability(p, matrix))
    print X
    print Y
    plt.plot(X, Y)
    plt.show()
