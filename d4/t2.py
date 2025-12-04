import numpy as np

def read_file(p: str):
    with open(p, 'r') as f:
        lines = [[int(j) for j in i.strip().replace('.', '0').replace('@', '1')] for i in f.readlines()]
        h = len(lines)
        w = len(lines[0])
        padded_lines = [[0] + i + [0] for i in lines]
        padded_lines = [[0] * (w + 2)] + padded_lines + [[0] * (w + 2)]
        return padded_lines, (h, w)

def removing_rolls(matrix: list[list[int]], h: int, w: int):
    res = 0
    for h in range(1, h+1):
        for w in range(1, w+1):
            if matrix[h][w] == 1:
                dirs = [
                    matrix[h][w - 1],
                    matrix[h][w + 1],
                    matrix[h - 1][w],
                    matrix[h + 1][w],
                    matrix[h - 1][w - 1],
                    matrix[h - 1][w + 1],
                    matrix[h + 1][w - 1],
                    matrix[h + 1][w + 1],
                ]
                if sum(dirs) < 4:
                    res += 1
                    matrix[h][w] = True
    for list_ in matrix:
        for i, val in enumerate(list_):
            if val is True:
                list_[i] = 0
    return matrix, res

def main():
    lines, shape = read_file('input.txt')
    res = 0
    iter_res = -1
    while iter_res != 0:
        lines, iter_res = removing_rolls(lines, shape[0], shape[1])
        res += iter_res
    return res
            


if __name__ == "__main__":
    print(main())