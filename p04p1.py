from pathlib import Path
import re


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p04.txt').read_text().splitlines()

    points_in_card_pile = 0
    for card in input_data:
        _, winning_nums, have_nums = re.split(R':|\|', card)
        # the #s are unique within a group even before turning into set
        winning_nums = set(int(n) for n in winning_nums.split())
        have_nums = set(int(n) for n in have_nums.split())

        matches = winning_nums.intersection(have_nums)
        if matches:
            points = 2 ** (len(matches) - 1)
            points_in_card_pile += points

    print('Total # of points in card pile', points_in_card_pile)


if __name__ == '__main__':
    main()
