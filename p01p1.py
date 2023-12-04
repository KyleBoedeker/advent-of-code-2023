from pathlib import Path
import re


def main():
    input_data = (Path(__file__).parent / 'inputs' /
                  'p01.txt').read_text().splitlines()

    total_sum = 0

    for line in input_data:
        nums = re.findall('\\d', line)
        line_tot = int(nums[0] + nums[-1])
        total_sum += line_tot

    print('Sum of all calibration values is:', total_sum)


if __name__ == '__main__':
    main()
