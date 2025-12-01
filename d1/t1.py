def read_file(p: str):
    with open(p, 'r') as f:
        lines = [i.strip() for i in f.readlines()]
    return lines

def main() -> None:
    inp = read_file('input.txt')
    curr_item = 50
    res = 0
    for condition in inp:
        direction = 1 if condition[0] == "R" else -1
        turns = int(condition[1:])
        for _ in range(turns):
            if direction > 0:
                curr_item += 1
            else:
                curr_item -= 1
            if curr_item == -1:
                curr_item = 99
            if curr_item == 100:
                curr_item = 0
        if curr_item == 0:
            res +=1
    print(res)

if __name__ == "__main__":
    main()