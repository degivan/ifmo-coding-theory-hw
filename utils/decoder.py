import numpy as np


def generate_sequences(n):
    result = []
    formatter = ('{0:0' + str(n) + 'b}')
    for i in range(2 ** n):
        result.append([[int(j)] for j in formatter.format(i)])
    return np.array(result)


def np_to_str(array):
    return ''.join([str(j) for j in array])


class Decoder(object):
    def __init__(self, p, matrix):
        self.p = p
        self.matrix = np.array(matrix)
        self.codewords = {}
        for i in generate_sequences(len(matrix)):
            codeword = np.mod(np.sum(np.multiply(i, self.matrix), axis=0), 2)
            self.codewords[np_to_str(codeword)] = np_to_str([l[0] for l in i])

    def decode(self, y):
        codeword = max(self.codewords.keys(), key=lambda cw: self.count_p(y, cw))
        return self.codewords[codeword]

    def count_p(self, y, cw):
        probability = 1.0
        for a, b in zip(y, cw):
            probability *= 1 - self.p if a == b else self.p
        return probability
