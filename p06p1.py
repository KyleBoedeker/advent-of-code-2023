from pathlib import Path
import re
from math import prod


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p06.txt').read_text().splitlines()

    # times on first line, distances on the second
    race_times = map(int, re.findall(R'(\d+)', input_data[0]))
    record_dists = map(int, re.findall(R'(\d+)', input_data[1]))

    ways_to_win_per_race = []
    for race_time, record_dist in zip(race_times, record_dists):
        ways_to_win = 0
        for hold_time in range(1, race_time):
            if hold_time * (race_time - hold_time) > record_dist:
                ways_to_win += 1

        ways_to_win_per_race.append(ways_to_win)

    print(ways_to_win_per_race)
    print('Product of ways to win by race:', prod(ways_to_win_per_race))


if __name__ == '__main__':
    main()
