#!/usr/bin/env python
with open('05.txt','r') as f:
    lines=f.read().strip().split('\n')

#test
#lines=[
#'qjhvhtzxzqqjkmpb',
#'xxyxx',
#'uurcxstgmygtbstg',
#'ieodomkazucvgmuy',
#]

def check_if_nice(line):
    i=0
    linelen=len(line)
    found=False
    for i in range(linelen-1):
        ss=line[i:i+2]
        if line.count(ss)>=2:
            found=True
            break
    if not found:
        return False
    found=False
    for i in range(linelen-2):
        if line[i]==line[i+2]:
            found=True
            break
    if not found:
        return False
    return True

n=0
for line in lines:
    if check_if_nice(line):
        n+=1

print(n)

