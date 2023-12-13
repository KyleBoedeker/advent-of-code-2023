import itertools
import math
from pathlib import Path
import re

"""
I had to cheat via the subreddit and read the term "LCM" after getting bored
of waiting for my brute-force approach to work. Just that term alone made
me realize this was some clever math-major stuff based on cleverly designed
input data. Sigh... not the fun kind of puzzle I was hoping for.
"""


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p08.txt').read_text().splitlines()

    instructions = input_data[0]

    node_map = {}
    for line in input_data[2:]:
        if match := re.match(R'(...) = \((...), (...)\)', line):
            node_map[match.group(1)] = (match.group(2), match.group(3))

    path_lengths = []
    for current_node in (n for n in node_map if n.endswith('A')):
        steps = 0
        cycler = itertools.cycle(instructions)
        while True:
            if current_node.endswith('Z'):
                break
            steps += 1
            choices = node_map[current_node]
            tuple_idx = 0 if next(cycler) == 'L' else 1
            current_node = choices[tuple_idx]
        path_lengths.append(steps)

    print('Steps taken to go from all ??A -> to all ??Z:', math.lcm(*path_lengths))


if __name__ == '__main__':
    main()
