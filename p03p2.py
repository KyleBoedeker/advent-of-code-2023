from pathlib import Path


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p03.txt').read_text().splitlines()

    # 'gears' is of the form below where the tuple is the row/col offset
    # to the '*' and the value is a list of all numbers touching it.
    # For the example in the question this will become:
    # gears = {(1, 3): [467, 35], (4, 3): [617], (8, 5): [755, 598]}
    gears = {}

    for line_idx, line in enumerate(input_data):
        num_acc = ''
        # set of star positions {(row, col)} to avoid duplication
        star_pos = set()
        for ch_idx, ch in enumerate(line):
            if ch.isnumeric():
                num_acc += ch
                # symbol locater:
                for ch_offset in (-1, 0, 1):
                    for line_offset in (-1, 0, 1):
                        # avoid wrapping around for first row of shematic
                        if line_idx == 0 and line_offset == -1:
                            continue
                        # check around the digit for a symbol
                        try:
                            row = line_idx + line_offset
                            col = ch_idx + ch_offset
                            sym = input_data[row][col]
                            if sym == '*':
                                star_pos.add((row, col))
                        except IndexError:
                            pass
            elif num_acc:
                # non-numeric char encountered terminating number
                for pos in star_pos:
                    gears.setdefault(pos, []).append(int(num_acc))

                num_acc = ''
                star_pos = set()

        # handle end-of-line numbers
        if num_acc and star_pos:
            for pos in star_pos:
                gears.setdefault(pos, []).append(int(num_acc))

    # count 'real' gears (those stars with only 2 nearby numbers)
    sum_of_gear_ratios = 0
    for g in gears.values():
        if len(g) == 2:
            sum_of_gear_ratios += g[0] * g[1]

    print(gears)
    print('Sum of all gear ratios in engine:', sum_of_gear_ratios)


if __name__ == '__main__':
    main()
