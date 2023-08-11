#!/usr/bin/env python
with open('15.txt','r') as f:
    lines=f.read().strip().split('\n')

a=int(lines[0].split(' ')[4])
b=int(lines[1].split(' ')[4])
rounds=5000000

# test
#a=65
#b=8921
#rounds=5

a_factor=16807
b_factor=48271

divider=2147483647

matches=0
for _ in range(rounds):
    while True:
        a=(a*a_factor)%divider
        if a%4==0:
            break
    while True:
        b=(b*b_factor)%divider
        if b%8==0:
            break
    if a&0xffff==b&0xffff:
        matches+=1

print(matches)
