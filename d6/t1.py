from math import prod
import re

def read_file(p: str):
    with open(p, 'r') as f:
        lines = [re.sub(r'\s+', ',', i.strip()) for i in f.readlines()]
    digits = []
    signs = None
    for line in lines:
        line = line.split(',')
        try:
            line = [int(i) for i in line]
            digits.append(line)
        except ValueError as e:
            signs = line
    return digits, signs

def main():
    digits, signs = read_file('input.txt')
    total_lines = len(digits)
    res = 0
    for idx, sign in enumerate(signs):
        vals = []
        for pos in range(total_lines):
            vals.append(digits[pos][idx])
        if sign == '+':
            res += sum(vals)
        elif sign == '*':
            res += prod(vals)
    return res



if __name__ == "__main__":
    print(main())