from pathlib import Path
import re


class RangeTranslatorGroup:

    def __init__(self) -> None:
        self._tri_vals: list[tuple[int, int, int]] = []

    def add(self, tri_val: tuple[int, int, int]) -> None:
        self._tri_vals.append(tri_val)

    def lookup(self, val: int, rev=False) -> int:
        """Lookup src->dest or inverse if optional parameter rev is True."""
        for dst_start, src_start, rlen in self._tri_vals:
            if not rev and val in range(src_start, src_start + rlen):
                return val - src_start + dst_start
            if rev and val in range(dst_start, dst_start + rlen):
                return val - dst_start + src_start
        # any src nums not mapped, are returned un-changed
        return val


# use `python -m pytest p05p1.py` to test, I used it to root out a bug
def test_range_translator_group():
    rt = RangeTranslatorGroup()
    rt.add((50, 98, 2))
    rt.add((52, 50, 48))

    # default lookup
    assert rt.lookup(79) == 81
    assert rt.lookup(14) == 14
    assert rt.lookup(55) == 57
    assert rt.lookup(13) == 13

    # reverse
    assert rt.lookup(81, rev=True) == 79
    assert rt.lookup(14, rev=True) == 14
    assert rt.lookup(57, rev=True) == 55
    assert rt.lookup(13, rev=True) == 13


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p05.txt').read_text().splitlines()

    starting_seeds = tuple(int(v) for v in re.findall(R'(\d+)', input_data[0]))
    # starting_seeds = (79, 14, 55, 13)
    # catalog = { ('seeds', 'soil'): RangeTranslatorGroup(...), ...}
    catalog = {}

    current_catalog_key = ''
    # skip seed line
    for line in input_data[1:]:
        # skip empty lines
        if not line:
            pass
        # switch catalog over to a new mapping
        elif 'map' in line:
            # for example: splits = ['seed', 'to', 'soil', 'map:']
            splits = re.split(R'-|\s', line)
            # this converts 'seed' to 'soil'
            key, val = splits[0], splits[2]
            current_catalog_key = (key, val)
        # numeric lines (ranges)
        else:
            nums = tuple(int(v) for v in re.findall(R'(\d+)', line))
            # add the numbers to the RangeTranslatorGroup for the current catalog
            catalog.setdefault(
                current_catalog_key, RangeTranslatorGroup()).add(nums)

    conversion_vals = starting_seeds
    conversion_state = 'seed'

    # go until our current state is what we desire ('location' for the first part)
    while conversion_state != 'location':
        # catalog_key should become ('seed', 'soil') for the first iteration
        catalog_key = next((k, v)
                           for k, v in catalog.keys() if k == conversion_state)
        range_grp = catalog[catalog_key]
        conversion_vals = tuple(range_grp.lookup(v) for v in conversion_vals)
        # don't forget we've converted to the next type, so change our current state
        conversion_state = catalog_key[1]

    print('The min location corresponding to a seeed is:', min(conversion_vals))


if __name__ == '__main__':
    main()
