import itertools
from pathlib import Path
import re


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p08.txt').read_text().splitlines()

    instructions = input_data[0]

    node_map = {}
    for line in input_data[2:]:
        if match := re.match(R'(...) = \((...), (...)\)', line):
            node_map[match.group(1)] = (match.group(2), match.group(3))

    steps = 0
    current_node = 'AAA'
    cycler = itertools.cycle(instructions)
    while True:
        if current_node == 'ZZZ':
            break
        steps += 1
        choices = node_map[current_node]
        tuple_idx = 0 if next(cycler) == 'L' else 1
        current_node = choices[tuple_idx]

    print('Steps taken to go from AAA -> ZZZ:', steps)


if __name__ == '__main__':
    main()
