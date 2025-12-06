def read_file(p: str):
    with open(p, 'r') as f:
        lines = f.readlines()
    avl_ing = False
    fresh_ranges = []
    all_avl = set()
    for line in lines:
        line = line.strip()
        if line == '':
            avl_ing = True
            continue
        if not avl_ing:
            x1, x2 = line.split('-')
            rang = [int(x1), int(x2) + 1]
            fresh_ranges.append(rang)
        else:
            all_avl.add(int(line))
    return fresh_ranges, all_avl

def main():
    fresh, available = read_file('input.txt')
    res = set()
    for avl_ing in available:
        for fresh_range in fresh:
            min_ = fresh_range[0]
            max_ = fresh_range[1]
            if min_ <= avl_ing <= max_:
                res.add(avl_ing)
    return len(res)
            


if __name__ == "__main__":
    print(main())