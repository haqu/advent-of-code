#!/usr/bin/env python

with open('15.txt','r') as f:
    lines=f.read().strip().split('\n')

#test='''
#Disc #1 has 5 positions; at time=0, it is at position 4.
#Disc #2 has 2 positions; at time=0, it is at position 1.
#'''
#lines=test.strip().split('\n')

discs=[]

import re
for line in lines:
    m=re.match(r'Disc #\d+ has (\d+) positions; at time=0, it is at position (\d+).',line).groups()
    discs.append([int(m[0]),int(m[1])])

#print(discs)

def check_disc(d,t):
    period=d[0]
    start=d[1]
    #print(f'check_disc, period:{d[0]}, start:{d[1]}, time:{t}')
    return (t+start)%period==0

drop_time=-1
while True:
    drop_time+=1
    #print('-------------------------------------')
    #print(drop_time)
    time=drop_time
    invalid=False
    for d in discs:
        time+=1
        if not check_disc(d,time):
            #print(f'bounced at disc {discs.index(d)}')
            invalid=True
            break
    if invalid:
        continue
    print(drop_time)
    exit()

