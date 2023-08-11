#!/usr/bin/env python
with open('05.txt','r') as f:
    lines=f.read().strip().split('\n')
#test
#lines=[
#'ugknbfddgicrmopn',
#'aaa',
#'jchzalrnumimnmhp',
#'haegwjzuvuyypxyu',
#'dvszwmarrgswjxmb'
#]
vowels='aeiou'
def check_if_nice(line):
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        return False
    i=0
    n_vowels=0
    linelen=len(line)
    twice=False
    while i<linelen:
        if line[i] in vowels:
            n_vowels+=1
        if not twice and i<linelen-1 and line[i]==line[i+1]:
            twice=True
        i+=1
    return (twice and n_vowels>=3)

n=0
for line in lines:
    if check_if_nice(line):
        n+=1

print(n)

