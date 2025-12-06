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
            rang = (int(x1), int(x2))
            fresh_ranges.append(rang)
        else:
            pass
    fresh_ranges.sort(key=lambda x: x[0])
    return fresh_ranges, all_avl

def main():
    fresh_intervals, _ = read_file('input.txt')
    merged_intervals = []
    curr_start, curr_end = fresh_intervals[0]
    for start, end in fresh_intervals[1:]:
        if start <= curr_end +1:
            curr_end = max(curr_end, end)
        else:
            merged_intervals.append((curr_start, curr_end))
            curr_start, curr_end = start, end
    merged_intervals.append((curr_start, curr_end))
    return sum(end - start + 1 for start, end in merged_intervals)
            


if __name__ == "__main__":
    print(main())