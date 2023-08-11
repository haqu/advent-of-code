#!/usr/bin/env python
with open('06.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#eedadn
#drvtee
#eandsr
#raavrd
#atevrs
#tsrnev
#sdttsa
#rasrtv
#nssdts
#ntnada
#svetve
#tesnvt
#vntsnd
#vrdear
#dvrsen
#enarar
#'''
#lines=data.strip().split('\n')

letters=[]

for line in lines:
    for i in range(len(line)):
        if len(letters)<=i:
            letters.append([])
        letters[i].append(line[i])

import itertools
message=''
for i in range(len(letters)):
    arr=letters[i]
    counts={arr.count(c):c for c in arr}
    keys=sorted(list(counts.items()))
    message+=keys[0][1]

print(message)

