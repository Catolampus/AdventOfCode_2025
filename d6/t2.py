import numpy as np
import re

def main():
    with open("input.txt", 'r') as f:
        lines = [list(i.strip()) for i in f.readlines()]
    res = 0
    new_lines = []
    total_len = len(lines[0])
    total_rows = len(lines) -1
    signs = (re.sub(r'\s+',',', ''.join(lines[-1]))).split(',')
    for idx in range(total_len):
        if all([lines[pos][idx]==' ' for pos in range(total_rows)]):
            for pos in range(total_rows):
                lines[pos][idx] = "|"
    for pos in range(total_rows):
        new_lines.append([i if i != ' ' else '0' for i in lines[pos]])
    processed_lines = []
    for line in new_lines:
        processed_lines.append(''.join(line).split('|'))

    for idx in range(len(processed_lines[0])):
        vals = []
        sign = signs[idx]
        for pos in range(len(processed_lines)):
            vals.append([i if i != '0' else None for i in list(processed_lines[pos][idx])])
        matrix = np.array(vals).T
        vals = []
        for row in matrix:
            digits = [x for x in row if isinstance(x, str)]
            vals.append(int(''.join(digits)))
        if sign == '+':
            res += sum(vals)
        elif sign == '*':
            res += np.prod(vals)
    return int(res)
    



if __name__ == "__main__":
    print(main())