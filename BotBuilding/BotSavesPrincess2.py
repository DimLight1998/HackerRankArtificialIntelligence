#!/bin/python


def nextMove(n, r, c, grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                p_pos = (i, j)
                break
    x_off = c - p_pos[1]
    y_off = r - p_pos[0]
    if abs(x_off) < abs(y_off):
        if y_off < 0:
            return 'DOWN'
        else:
            return 'UP'
    else:
        if x_off < 0:
            return 'RIGHT'
        else:
            return 'LEFT'


n = input()
r, c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n, r, c, grid)
