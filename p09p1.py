from pathlib import Path
import re
import numpy as np


class Extrapolater:

    def __init__(self, row: list[int]) -> None:
        self._rows = [row]

        while self._append_diff():
            pass

        self._interpolate_backward()

    def get_val_in_sequence(self) -> int:
        return self._rows[0][-1]

    def _append_diff(self) -> bool:
        """Returns true if row appended was non-zero."""
        diff = np.diff(np.array(self._rows[-1]))
        self._rows.append(diff.tolist())

        return bool(np.any(diff))

    def _interpolate_backward(self):
        # append zero
        self._rows[-1].append(0)

        # iterate over rows skipping the last row
        for row_idx, row in reversed(list(enumerate(self._rows[:-1]))):
            row.append(self._rows[row_idx + 1][-1] + row[-1])


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p09.txt').read_text().splitlines()

    sum_of_next_history_values = 0
    for line in input_data:
        row_data = list(map(int, (re.findall(R'(-?\d+)', line))))

        e = Extrapolater(row_data)
        for r in e._rows:
            print(r)
        print('-----------------')
        sum_of_next_history_values += e.get_val_in_sequence()

    print(sum_of_next_history_values)


if __name__ == '__main__':
    main()
