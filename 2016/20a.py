#!/usr/bin/env python
with open('20.txt','r') as f:
    lines=f.read().strip().split('\n')

ranges=[]
min_ip=0
#max_ip=4294967295

for line in lines:
    v1,v2,*_=line.split('-')
    ranges.append([int(v1),int(v2)])

ranges=sorted(ranges,key=lambda p: p[0])
for pair in ranges:
    print(min_ip,pair)
    if min_ip<pair[0]:
        break
    ip=pair[1]+1
    if ip>min_ip:
        min_ip=ip

print(min_ip)
