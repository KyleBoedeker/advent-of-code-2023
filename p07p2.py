from __future__ import annotations

import enum
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

# lower index in this string is less valueable
CARD_RANK = 'J23456789TQKA'


class HandType(enum.IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def rank_hand(hand: str) -> HandType:
    jokers = hand.count('J')
    if jokers == 5:
        return HandType.FIVE_OF_A_KIND

    counter = Counter(hand.replace('J', '')).most_common()

    (_, cc0) = counter[0]
    if cc0 + jokers == 5:
        return HandType.FIVE_OF_A_KIND
    if cc0 + jokers == 4:
        return HandType.FOUR_OF_A_KIND
    # must be at least one other type of card by this point
    (cf1, cc1) = counter[1]
    if (cc0 + jokers == 3 and cc1 == 2) or (cc0 == 3 and cc1 + jokers == 2):
        return HandType.FULL_HOUSE
    if cc0 + jokers == 3:
        return HandType.THREE_OF_A_KIND
    if (cc0 + jokers == 2 and cc1 == 2) or (cc0 == 2 and cc1 + jokers == 2):
        return HandType.TWO_PAIR
    if cc0 + jokers == 2:
        return HandType.ONE_PAIR
    if cc0 + jokers == 1:
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
    assert CardHand('QQQQ2', 0) > CardHand('JKKK2', 0)
    assert CardHand('KTJJT', 0) > CardHand('QQQJA', 0)
    assert rank_hand('AAAAA') == HandType.FIVE_OF_A_KIND
    assert rank_hand('JJJJJ') == HandType.FIVE_OF_A_KIND
    assert rank_hand('AAAAJ') == HandType.FIVE_OF_A_KIND
    assert rank_hand('JAAQQ') == HandType.FULL_HOUSE
    assert rank_hand('JAAQK') == HandType.THREE_OF_A_KIND
    assert rank_hand('AAAQK') == HandType.THREE_OF_A_KIND
    assert rank_hand('22AQQ') == HandType.TWO_PAIR
    assert rank_hand('J2AQK') == HandType.ONE_PAIR
    assert CardHand('AAAAA', 0) > CardHand('22222', 0) > CardHand('JJJJJ', 0)


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
