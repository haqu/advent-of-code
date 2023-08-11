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

towers_above={}
weights={}

for line in lines:
    line=line.replace(',','')
    parts=line.split(' ')
    name=parts[0]
    weight=int(parts[1][1:-1])
    weights[name]=weight
    if len(parts)>2:
        for n in parts[3:]:
            arr=towers_above.get(name,[])
            arr.append(n)
            towers_above[name]=arr

def get_total_weight(name):
    w=weights[name]
    for n in towers_above.get(name,[]):
        w+=get_total_weight(n)
    return w

for name in towers_above:
    wa=[]
    arr=towers_above[name]
    for n in arr:
        wa.append(get_total_weight(n))
    if len(set(wa))>1:
        if wa[1]==wa[2]:
            index=0
            delta=wa[1]-wa[0]
        elif wa[0]==wa[2]:
            index=1
            delta=wa[2]-wa[1]
        else:
            index=2
            delta=wa[0]-wa[2]
        change=weights[arr[index]]+delta
        print(change)
        exit()

