import itertools

def id(line):
    char_map = {'B': '1', 'F': '0', 'L': '0', 'R': '1'}
    bin = ''.join(char_map[char] for char in line)
    return int(bin, 2)

def puzzle1(data):
    return max(id(line) for line in data)

def puzzle2(data):
    present = {id(line) for line in data}
    for seat_num in itertools.count(min(present)):
        if seat_num not in present:
            return seat_num

if __name__ == '__main__':
    with open('input.py') as in_file:
        data = in_file.read().strip().splitlines()
    print(puzzle1(data))
    print(puzzle2(data))
