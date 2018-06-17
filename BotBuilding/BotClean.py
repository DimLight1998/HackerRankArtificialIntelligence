if __name__ == '__main__':
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    inf_distance = None
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                distance = abs(i - pos[0]) + abs(j - pos[1])
                if inf_distance is None or inf_distance > distance:
                    inf_distance = distance
                    target = (i, j)
    y_off = target[0] - pos[0]
    x_off = target[1] - pos[1]
    if x_off > 0:
        print('RIGHT')
    elif x_off < 0:
        print('LEFT')
    elif y_off > 0:
        print('DOWN')
    elif y_off < 0:
        print('UP')
    else:
        print('CLEAN')
