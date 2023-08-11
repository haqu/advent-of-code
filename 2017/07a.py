#!/usr/bin/env python
with open('07.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#pbga (66)
#xhth (57)
#ebii (61)
#havc (66)
#ktlj (57)
#fwft (72) -> ktlj, cntj, xhth
#qoyq (66)
#padx (45) -> pbga, havc, qoyq
#tknk (41) -> ugml, padx, fwft
#jptl (61)
#ugml (68) -> gyxo, ebii, jptl
#gyxo (61)
#cntj (57)
#'''.strip().split('\n')

towers=[]
excluded=[]

for line in lines:
    line=line.replace(',','')
    parts=line.split(' ')
    name=parts[0]
    towers.append(name)
    if len(parts)>2:
        for n in parts[3:]:
            excluded.append(n)
    else:
        excluded.append(name)

print(set(towers)-set(excluded))

