# https://adventofcode.com/2018/day/1

import sys

def measure_freq_change(filename):
    total = 0
    for change in open(filename, 'r'):
        total += int(change)
    return print(total)

measure_freq_change(sys.argv[1])
