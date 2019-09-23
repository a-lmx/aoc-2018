# https://adventofcode.com/2018/day/1

def measure_freq_change(filename):
    change_file = open(filename, 'r')
    total = 0
    for change in change_file:
        total += int(change)
    return print(total)

measure_freq_change("day1_1_input.txt")
