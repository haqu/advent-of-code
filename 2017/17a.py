#!/usr/bin/env python
puzzle_input=345

# test
#puzzle_input=3

buffer=[0]
buflen=1
i=0

for it in range(2017):
    i=(i+puzzle_input)%buflen
    v=it+1
    buffer=buffer[:i+1]+[v]+buffer[i+1:]
    buflen+=1
    i+=1

i=(i+1)%buflen
print(buffer[i])

