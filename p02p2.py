from pathlib import Path
import re

# convert ['2 green', '2 blue', '9 red'] into {'red': 9, 'green': 2, 'blue': 2}
# def game_list_to_dict(game_list: list[str]) -> dict[str, int]:
#     return v
# match = re.search(R'Game (\d+): ((\d+ (red|green|blue)) )+', line)


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p02.txt').read_text().splitlines()

    REAL_BAG = {'red': 12, 'green': 13, 'blue': 14}

    valid_game_pow_sum = 0

    for line in input_data:
        min_set = {'red': 0, 'green': 0, 'blue': 0}

        for game_set in re.split(':|;', line)[1:]:
            game_set = game_set.strip().split(', ')
            handfull = {'red': 0, 'green': 0, 'blue': 0}
            for hand in game_set:
                count, color = hand.split()
                handfull[color] = int(count)
            min_set['red'] = max(min_set['red'], handfull['red'])
            min_set['blue'] = max(min_set['blue'], handfull['blue'])
            min_set['green'] = max(min_set['green'], handfull['green'])

        valid_game_pow_sum += min_set['red'] * min_set['blue'] * min_set['green']

    print(valid_game_pow_sum)


if __name__ == '__main__':
    main()
