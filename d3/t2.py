def read_file(p: str):
    with open(p, 'r') as f:
        lines = f.readlines()
        return lines


def main():
    lines = read_file('input.txt')
    steps = list(range(1, 13))[::-1]
    res = 0
    for line in lines:
        line = line.strip() + '0'
        max_id = -1
        totals = []
        for step in steps:
            max_id = max_id+1
            sub_line = line[max_id:-step]
            max_digit = str(max([int(i) for i in set(sub_line)]))
            totals.append(max_digit)
            max_id = line.index(str(max_digit), max_id)
            # print(sub_line, f"{max_id}:-{step}", f"max_dig: {max_digit}, max_id: {max_id}")
        res += int(''.join(totals))
    return res
            


if __name__ == "__main__":
    print(main())