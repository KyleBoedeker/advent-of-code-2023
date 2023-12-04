from pathlib import Path
import re


# Need to find both numbers in the event of a line like:
# 'oneight' --(perform replacements)-> 'o1e8t' --(extract numeric)-> '18'
# Using first letter should be sufficient since the overlap isn't much between number's names
REPLACEMENTS = {'one': 'o1e', 'two': 't2o', 'three': 't3e',
                'four': 'f4r', 'five': 'f5e', 'six': 's6x',
                'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
                }


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p01.txt').read_text().splitlines()

    total_sum = 0

    for line in input_data:
        # perform replacements to allow overlapping numbers and simplify digit extraction
        for k, v in REPLACEMENTS.items():
            line = line.replace(k, v)

        digits = re.findall('(\\d)', line)

        line_tot = int(digits[0] + digits[-1])
        total_sum += line_tot

    print('Sum of all calibration values is:', total_sum)


if __name__ == '__main__':
    main()
