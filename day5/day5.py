# https://adventofcode.com/2018/day/5

import string
import sys

def reactive(unit_a, unit_b):
    if abs(ord(unit_a) - ord(unit_b)) == 32:
        return True
    return False

# Recursive process_polymer left for sentimentality
def process_polymer(polymer, num_eliminated):
    if num_eliminated == 0:
        return polymer
    else:
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
        
        result_polymer = ''.join(output)
        sum_eliminated = sum(eliminated)
        return process_polymer(result_polymer, sum_eliminated)

def process_polymer_iter(polymer):
    num_eliminated = len(polymer)

    polymer_list = list(polymer)
    finished_processing = False
    while finished_processing == False:
        num_eliminated = 0
        i = 0
        while i < (len(polymer_list) - 1):
            # print(polymer_list)
            if reactive(polymer_list[i], polymer_list[i+1]):
                del polymer_list[i]
                # this would be polymer_list[i+1] before the previous deletion
                del polymer_list[i]
                num_eliminated += 1
            else:
                i += 1
        if num_eliminated == 0:
            finished_processing = True
    result_polymer = ''.join(polymer_list)
    return result_polymer

def preprocess_polymer(polymer, char):
    output = []
    for i in range(len(polymer)):
        letter = polymer[i]
        if letter.lower() == char:
            continue
        else:
            output.append(letter)
    return ''.join(output)

def get_processed_polymer(polymer):
    result = process_polymer_iter(polymer)
    print(f'The resulting polymer {result} is {len(result)} units long.')


def find_shortest_polymer(polymer):
    shortest_letter = None
    len_shortest_polymer = len(polymer)
    for letter in list(string.ascii_lowercase):
        preprocessed_polymer = preprocess_polymer(polymer, letter)
        
        result_polymer = process_polymer_iter(preprocessed_polymer)
        if len(result_polymer) < len_shortest_polymer:
            shortest_letter = letter
            len_shortest_polymer = len(result_polymer)
    print(f'The length of the shortest polymer (after removing {shortest_letter}) is {len_shortest_polymer}.')
    
def main(filename):
    polymer = open(filename).readline().rstrip('\n')
    find_shortest_polymer(polymer)

main(sys.argv[1])
