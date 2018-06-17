#!/usr/bin/python


def displayPathtoPrincess(n, grid):
    src_col = -1
    src_row = -1
    dest_col = -1
    dest_row = -1
    for row, line in enumerate(grid):
        if src_col == -1:
            src_col = line.find('m')
            src_row = row
        if dest_col == -1:
            dest_col = line.find('p')
            dest_row = row
    for _ in range(src_col - dest_col):
        print('LEFT')
    for _ in range(dest_col - src_col):
        print('RIGHT')
    for _ in range(src_row - dest_row):
        print('UP')
    for _ in range(dest_row - src_row):
        print('DOWN')


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m, grid)
