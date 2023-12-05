from pathlib import Path
import re


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p04.txt').read_text().splitlines()

    # number of copies of each card stored in array
    card_copies = [1] * len(input_data)

    for card_idx, card in enumerate(input_data):
        _, winning_nums, have_nums = re.split(R':|\|', card)
        # the #s are unique within a group even before turning into set
        winning_nums = set(int(n) for n in winning_nums.split())
        have_nums = set(int(n) for n in have_nums.split())

        matches = winning_nums.intersection(have_nums)
        for idx_match in range(len(matches)):
            try:
                # the next len(matches) cards get N copies added to them where N
                # is the # of copies of the current card
                card_copies[card_idx + 1 + idx_match] += card_copies[card_idx]
            except IndexError:
                pass

    print('Total # of scratchcards', sum(card_copies))


if __name__ == '__main__':
    main()
