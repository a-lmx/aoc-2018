
import sys

def find_checksum(filename):
    ids = list(open(filename))
    print(f'Num ids: {len(ids)}')

    twice_set = set()
    thrice_set = set()

    for box_id in ids:
        letter_counts = {}
        for letter in box_id:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        for _, count in letter_counts.items():
            if count == 2:
                twice_set.add(box_id)
            if count == 3:
                thrice_set.add(box_id)
    
    checksum = len(twice_set) * len(thrice_set)
    print(f'There are {len(twice_set)} ids in which a letter appears exactly twice.')
    print(f'There are {len(thrice_set)} ids in which a letter appears exactly thrice.')
    print(f'The checksum is {checksum}.')

find_checksum(sys.argv[1])
