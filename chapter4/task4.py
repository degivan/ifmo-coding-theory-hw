import numpy as np

if __name__ == '__main__':
    matrix = np.array([[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                       [0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 1, 0, 0, 1, 1]]
                      )
    spans = []
    for row in matrix:
        size = len(row)
        min_ind, max_ind, ind = size, 0, 0
        while ind < size:
            if row[ind] == 1:
                max_ind = ind - 1
                if min_ind == size:
                    min_ind = ind
            ind += 1
        spans.append((min_ind, max_ind))
    print spans
