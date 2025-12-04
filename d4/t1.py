import numpy as np

def read_file(p: str):
    with open(p, 'r') as f:
        lines = [[int(j) for j in i.strip().replace('.', '0').replace('@', '1')] for i in f.readlines()]
        h = len(lines)
        w = len(lines[0])
        padded_lines = [[0] + i + [0] for i in lines]
        padded_lines = [[0] * (w + 2)] + padded_lines + [[0] * (w + 2)]
        return padded_lines, (h, w)

def main():
    lines, shape = read_file('input.txt')
    res = 0
    for h in range(1, shape[0]+1):
        for w in range(1, shape[1]+1):
            if lines[h][w] == 1:
                dirs = [
                    lines[h][w - 1],
                    lines[h][w + 1],
                    lines[h - 1][w],
                    lines[h + 1][w],
                    lines[h - 1][w - 1],
                    lines[h - 1][w + 1],
                    lines[h + 1][w - 1],
                    lines[h + 1][w + 1],
                ]
                if sum(dirs) < 4:
                    res += 1
    return res
            


if __name__ == "__main__":
    print(main())