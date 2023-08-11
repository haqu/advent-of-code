#!/usr/bin/env python
import re

with open('16.txt', 'r') as f:
    lines = f.read().strip().split('\n')

target = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

# Sue 1: goldfish: 6, trees: 9, akitas: 0

for line in lines:
    aunt, rp = re.match(r'Sue (\S+): (.+)$', line).groups()
    pairs = rp.split(', ')
    is_valid = True
    for pair in pairs:
        k, v, *_ = pair.split(': ')
        if target[k] != int(v):
            is_valid = False
            break
    if is_valid:
        print(aunt)
        exit()
