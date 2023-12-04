from pathlib import Path
import re


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p02.txt').read_text().splitlines()

    REAL_BAG = {'red': 12, 'green': 13, 'blue': 14}

    valid_game_idx_sum = 0

    for line in input_data:
        game_idx = int(re.split(' |:', line)[1])
        game_is_valid = True

        for game_set in re.split(':|;', line)[1:]:
            game_set = game_set.strip().split(', ')
            handfull = {'red': 0, 'green': 0, 'blue': 0}
            for hand in game_set:
                count, color = hand.split()
                handfull[color] = int(count)
            if handfull['red'] > REAL_BAG['red'] or handfull['green'] > REAL_BAG['green'] or handfull['blue'] > REAL_BAG['blue']:
                game_is_valid = False
                break
        if game_is_valid:
            valid_game_idx_sum += game_idx

    print(valid_game_idx_sum)


if __name__ == '__main__':
    main()
