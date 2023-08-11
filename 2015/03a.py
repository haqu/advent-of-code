#!/usr/bin/env python
with open('03.txt','r') as f:
    data=f.read()
#data='>'
#data='^>v<'
#data='^v^v^v^v^v'
x,y=0,0
mem={'0,0':True}
total=1
for d in data:
    if d=='<':
        x-=1
    elif d=='>':
        x+=1
    elif d=='^':
        y-=1
    elif d=='v':
        y+=1
    coord=f'{x},{y}'
    if mem.get(coord):
        continue
    mem[coord]=True
    total+=1
print(total)

