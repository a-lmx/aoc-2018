# https://adventofcode.com/2018/day/3

import sys

def create_fabric(side_length):
    return [[[] for i in range(side_length)] for j in range(side_length)]

def parse_claim(claim_string):
    # ex: #123 @ 3,2: 5x4
    claim = {}
    split_claim = claim_string.split()
    claim['id'] = split_claim[0][1:]
    left, top = split_claim[2].split(',')
    claim['left'], claim['top'] = int(left), int(top[:-1])
    width, height = split_claim[3].split('x')
    claim['width'], claim['height'] = int(width), int(height)

    return claim

def track_claims(fabric, claim):
    # ex: left is 3, top is 2, width is 5, height is 4
    for i in range(claim['height']):
        for j in range(claim['width']):
            fabric[claim['top']+i][claim['left'] + j].append(claim['id'])

def count_clashing_claims(fabric):
    clashing_claims = 0
    for row in fabric:
        for inch in row:
            if len(inch) > 1:
                clashing_claims += 1

    return clashing_claims

def process_claims(filename, fabric_size):
    claims = open(filename).readlines()

    fabric = create_fabric(fabric_size)

    for claim in claims:
        parsed_claim = parse_claim(claim)
        track_claims(fabric, parsed_claim)

    num_clashing_claims = count_clashing_claims(fabric)
    print(f'Number of squares with clashing claims: {num_clashing_claims}')

process_claims(sys.argv[1], int(sys.argv[2]))
