from pathlib import Path


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p03.txt').read_text().splitlines()

    sum_of_pns = 0
    for line_idx, line in enumerate(input_data):
        num_acc = ''
        num_valid = False
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
                            sym = input_data[line_idx +
                                             line_offset][ch_idx + ch_offset]
                            is_symbol = not sym.isnumeric() and sym != '.'
                            num_valid = num_valid or is_symbol
                        except IndexError:
                            pass
            elif num_acc:
                # non-numeric char encountered terminating number
                if num_valid:
                    sum_of_pns += int(num_acc)
                num_acc = ''
                num_valid = False

        # handle end-of-line numbers
        if num_acc and num_valid:
            sum_of_pns += int(num_acc)

    print('Sum of all PNs in engine schematic', sum_of_pns)


if __name__ == '__main__':
    main()
