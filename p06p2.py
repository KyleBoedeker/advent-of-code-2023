from pathlib import Path
import re


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p06.txt').read_text().splitlines()

    # times on first line, distances on the second
    race_time = int(''.join(re.findall(R'(\d)', input_data[0])))
    record_dist = int(''.join(re.findall(R'(\d+)', input_data[1])))

    ways_to_win = 0
    for hold_time in range(1, race_time):
        if hold_time * (race_time - hold_time) > record_dist:
            ways_to_win += 1

    print('Ways to win the race:', ways_to_win)


if __name__ == '__main__':
    main()
