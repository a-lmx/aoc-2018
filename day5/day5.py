# https://adventofcode.com/2018/day/5

import sys

def reactive(unit_a, unit_b):
    if abs(ord(unit_a) - ord(unit_b)) == 32:
        return True
    return False

def process_polymer(polymer, num_eliminated):
    if num_eliminated == 0:
        print(f'The resulting polymer {polymer} is {len(polymer)} units long.')
        return polymer
    output = []
    eliminated = [0 for i in range(len(polymer))]
    i = 0
    while i < (len(polymer) - 1):
        if reactive(polymer[i], polymer[i+1]):
            eliminated[i] = 1
            eliminated[i+1] = 1
            i += 2
        else:
            i += 1
    for i in range(len(polymer)):
        if eliminated[i] == 0:
            output.append(polymer[i])
    
    output_polymer = ''.join(output)
    sum_eliminated = sum(eliminated)
    process_polymer(output_polymer, sum_eliminated)
    
def main(filename):
    polymer = open(filename).readline().rstrip('\n')
    process_polymer(polymer, -1)

main(sys.argv[1])
