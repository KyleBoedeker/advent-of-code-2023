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
    current_nodes = tuple(k for k in node_map if k.endswith('A'))
    cycler = itertools.cycle(instructions)
    while True:
        if all(n.endswith('Z') for n in current_nodes):
            break
        steps += 1
        tuple_idx = 0 if next(cycler) == 'L' else 1
        current_nodes = tuple(node_map[n][tuple_idx] for n in current_nodes)

    print('Steps taken to go from AAA -> ZZZ:', steps)


if __name__ == '__main__':
    main()
