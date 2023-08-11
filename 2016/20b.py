#!/usr/bin/env python
with open('20.txt','r') as f:
    lines=f.read().strip().split('\n')

ranges=[]
max_ip=4294967295
n_ips=max_ip+1

for line in lines:
    v1,v2,*_=line.split('-')
    ranges.append([int(v1),int(v2)])

merged_ranges=[]
merged_range=[-2,-2]
ranges=sorted(ranges,key=lambda p: p[0])
for pair in ranges:
    p0=pair[0]
    p1=pair[1]
    if p0<=merged_range[1]+1 and p1>=merged_range[0]-1:
        merged_range[0]=min(merged_range[0],p0)
        merged_range[1]=max(merged_range[1],p1)
    else:
        merged_ranges.append(merged_range)
        merged_range=[p0,p1]
merged_ranges.append(merged_range)

for r in merged_ranges:
    if r[0]<0:
        continue
    v=r[1]-r[0]+1
    n_ips-=v

print(n_ips)

