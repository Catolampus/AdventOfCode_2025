def read_file(p: str):
    with open(p, 'r') as f:
        lines = f.read().split(',')
        return lines


def main():
    digits = read_file('input.txt')
    res = 0
    for r in digits:
        start, end = r.strip().split('-')
        for d in range(int(start), int(end)+1):
            d_s = str(d)
            idxes = tuple(range(1   , len(d_s) // 2 + 1))[::-1]
            print(d_s, idxes)
            for idx in idxes:
                n_seq = d_s.count(d_s[:idx])
                if n_seq > 1:
                    res += d
    return res
            


if __name__ == "__main__":
    print(main())