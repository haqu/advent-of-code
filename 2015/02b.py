#!/usr/bin/env python
with open('02.txt','r') as f:
    data=f.read().split('\n')
#data=['2x3x4']
#data=['1x1x10']
total=0
for entry in data:
    if not len(entry):
        continue
    l,w,h,*rest=[int(v) for v in entry.split('x')]
    pers=[2*(l+w),2*(w+h),2*(h+l)]
    min_per=min(pers)
    vol=w*l*h
    ribbon_len=min_per+vol
    total+=ribbon_len
print(total)

