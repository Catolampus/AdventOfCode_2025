def read_file(p: str):
    with open(p, 'r') as f:
        lines = f.readlines()
        return lines


def main():
    lines = read_file('input.txt')
    res = 0
    for line in lines:
        line = line.strip()
        
        sub_line = line[:-1]
        frst_max_digit = str(max([int(i) for i in set(sub_line)]))
        max_id = line.index(str(frst_max_digit))
        sec_max_dig = str(max([int(i) for i in set(line[max_id+1:])]))
        val = int(f"{frst_max_digit}{sec_max_dig}")
        res += val
    return res
            


if __name__ == "__main__":
    print(main())