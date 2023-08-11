#!/usr/bin/env python
with open('19.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#H => HO
#H => OH
#O => HH
#
#HOH
#'''
#lines=data.strip().split('\n')

rep={}

next_line_is_molecule=False
for line in lines:
    if line=='':
        next_line_is_molecule=True
        continue
    if not next_line_is_molecule:
        p1,p2,*_=line.split(' => ')
        a=rep.get(p1,[])
        a.append(p2)
        rep[p1]=a
    else:
        molecule=line

#print(repr(rep))
#print(molecule)

import re

variations=[]
for p1 in rep:
    a=rep[p1]
    for p2 in a:
        for m in re.finditer(p1,molecule):
            var=molecule[:m.start()]
            var+=p2
            var+=molecule[m.end():]
            variations.append(var)

variations=set(variations) # uniq

#for v in variations:
#    print(v)

print(len(variations))

