# https://adventofcode.com/2018/day/1#part2

import sys

def first_freq_reached_twice(filename):
    changes = open(filename, 'r').readlines()
    frequency = 0
    freqs = set()
    freqs.add(frequency)
    frequency_repeated = False

    while not frequency_repeated:
        for change in changes:
            frequency += int(change)
            if frequency in freqs:
                print("Frequency reached twice: ", frequency)
                frequency_repeated = True
                break
            else:
                freqs.add(frequency)
    
first_freq_reached_twice(sys.argv[1])
