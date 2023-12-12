from __future__ import annotations
import enum

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

# lower index in this string is less valueable
CARD_RANK = '23456789TJQKA'


class HandType(enum.IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def rank_hand(hand: str) -> HandType:
    counter = Counter(hand).most_common()
    # grab the card count of the n'th element in the list of most common cards
    def card_cnt(idx): return counter[idx][1]

    if card_cnt(0) == 5:
        return HandType.FIVE_OF_A_KIND
    elif card_cnt(0) == 4:
        return HandType.FOUR_OF_A_KIND
    elif card_cnt(0) == 3 and card_cnt(1) == 2:
        return HandType.FULL_HOUSE
    elif card_cnt(0) == 3:
        return HandType.THREE_OF_A_KIND
    elif card_cnt(0) == 2 and card_cnt(1) == 2:
        return HandType.TWO_PAIR
    elif card_cnt(0) == 2:
        return HandType.ONE_PAIR
    elif card_cnt(0) == 1:
        return HandType.HIGH_CARD
    raise RuntimeError("Invalid hand provided!")


@dataclass
class CardHand:

    hand: str
    wager: int

    def __lt__(self, other: CardHand) -> bool:
        # clear winner between the hands based on type
        if rank_hand(self.hand) != rank_hand(other.hand):
            return rank_hand(self.hand) < rank_hand(other.hand)

        for self_face, other_face in zip(self.hand, other.hand):
            self_rank = CARD_RANK.index(self_face)
            other_rank = CARD_RANK.index(other_face)
            if self_rank != other_rank:
                return self_rank < other_rank

        raise RuntimeError("Two cards of same exact rank???")


def test_cardhand():
    assert CardHand('33332', 0) > CardHand('2AAAA', 0)
    assert CardHand('77888', 0) > CardHand('77788', 0)
    assert CardHand('JJJJJ', 0) > CardHand('JJJJA', 0)

    # Full house is better than 3 of a kind
    assert CardHand('23332', 0) > CardHand('TTT98', 0)
    # ... and worse than 4 of a kind
    assert CardHand('AA8AA', 0) > CardHand('23332', 0)


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p07.txt').read_text().splitlines()

    hands = []
    # times on first line, distances on the second
    for line in input_data:
        if match := re.match(R'(.....) (\d+)', line):
            cardhand = CardHand(match.group(1), int(match.group(2)))
            hands.append(cardhand)

    hands.sort()

    # winnings = bid * rank (rank is one indexed)
    total_winnings = sum(h.wager * (1 + idx) for idx, h in enumerate(hands))

    print('Total winnings are:', total_winnings)


if __name__ == '__main__':
    main()
