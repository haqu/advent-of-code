#!/usr/bin/env python
with open('02.txt','r') as f:
    data=f.read().split('\n')
#data=['2x3x4']
total=0
for entry in data:
    if not len(entry):
        continue
    l,w,h,*rest=[int(v) for v in entry.split('x')]
    areas=[l*w,w*h,h*l]
    parts=[2*a for a in areas]
    wrapping_area=sum(parts)+min(areas)
    total+=wrapping_area
print(total)

