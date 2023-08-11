#!/usr/bin/env python
with open('03.txt','r') as f:
    data=f.read()
#data='^v'
#data='^>v<'
#data='^v^v^v^v^v'
x1,y1=0,0
x2,y2=0,0 #robo
mem={'0,0':True}
total=1
is_robo=False
for d in data:
    if not is_robo:
        if d=='<':
            x1-=1
        elif d=='>':
            x1+=1
        elif d=='^':
            y1-=1
        elif d=='v':
            y1+=1
        coord=f'{x1},{y1}'
    else:
        if d=='<':
            x2-=1
        elif d=='>':
            x2+=1
        elif d=='^':
            y2-=1
        elif d=='v':
            y2+=1
        coord=f'{x2},{y2}'
    if not mem.get(coord):
        mem[coord]=True
        total+=1
    is_robo=not is_robo
print(total)

