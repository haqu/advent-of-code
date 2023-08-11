#!/usr/bin/env python
with open('13.txt','r') as f:
    lines=f.read().strip().split('\n')

#data='''
#Alice would gain 54 happiness units by sitting next to Bob.
#Alice would lose 79 happiness units by sitting next to Carol.
#Alice would lose 2 happiness units by sitting next to David.
#Bob would gain 83 happiness units by sitting next to Alice.
#Bob would lose 7 happiness units by sitting next to Carol.
#Bob would lose 63 happiness units by sitting next to David.
#Carol would lose 62 happiness units by sitting next to Alice.
#Carol would gain 60 happiness units by sitting next to Bob.
#Carol would gain 55 happiness units by sitting next to David.
#David would gain 46 happiness units by sitting next to Alice.
#David would lose 7 happiness units by sitting next to Bob.
#David would gain 41 happiness units by sitting next to Carol.
#'''
#lines=data.strip().split('\n')

happiness={}
guests=[]

for line in lines:
    line=line.replace('would ','')
    line=line.replace('gain ','')
    line=line.replace('lose ','-')
    line=line.replace('happiness units by sitting next to ','')
    line=line.replace('.','')
    g1,h,g2,*_=line.split(' ')
    if not g1 in guests:
        guests.append(g1)
    if not g2 in guests:
        guests.append(g2)
    a=happiness.get(g1,[])
    a.append([g2,int(h)])
    happiness[g1]=a

n_guests=len(guests)

import itertools
perms=list(itertools.permutations(guests))

def get_happiness(g1,g2):
    a=happiness[g1]
    for pair in a:
        if pair[0]==g2:
            return pair[1]
    print(f'could not get happiness for {g1}, {g2}')
    exit()

max_total=0
for perm in perms:
    total=0
    for i in range(n_guests):
        if i>0:
            gL=perm[i-1]
        else:
            gL=perm[n_guests-1]
        g=perm[i]
        if i<n_guests-1:
            gR=perm[i+1]
        else:
            gR=perm[0]
        total+=get_happiness(g,gL)
        total+=get_happiness(g,gR)
    if total>max_total:
        max_total=total

print(max_total)

