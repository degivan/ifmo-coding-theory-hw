from utils.f2_matrix import F2Matrix


class Order(object):
    def __init__(self, comm):
        params = comm.split()
        self.command = params[0]
        if len(params) > 1:
            self.first = int(params[1])
            self.second = int(params[2])


if __name__ == '__main__':
    matrix = F2Matrix([
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1]
    ])

    while True:
        print matrix
        order = Order(raw_input('Enter command:'))
        if order.command == 'exit':
            break
        elif order.command == 'swap_c':
            matrix.swap_columns(order.first, order.second)
        elif order.command == 'swap_r':
            matrix.swap_rows(order.first, order.second)
        elif order.command == 'subtr_r':
            matrix.subtract_row(order.first, order.second)
        else:
            raise Exception("Bad command")
