#!/usr/bin/env python

with open('24.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#1
#2
#3
#4
#5
#7
#8
#9
#10
#11
#'''
#lines=data.strip().split('\n')

masses=[int(v) for v in lines]
masses.sort(reverse=True)
n_masses=len(masses)
total_mass=sum(masses)
group_mass=total_mass/4

import itertools
import functools
import operator

def find_groups(arr,max_size):
    groups=[]
    for m in arr:
        if m==group_mass:
            groups.append([m])
            return groups
    if max_size==1:
        return groups
    for n in range(2,max_size+1):
        combinations=list(itertools.combinations(arr,n))
        for group in combinations:
            m=functools.reduce(operator.add,group)
            if m==group_mass:
                groups.append(group)
    return groups

def get_remainder(arr,group):
    rem=arr.copy()
    for m in group:
        rem.remove(m)
    return rem

min_qe=0
n=0
while True:
    n+=1
    groups=find_groups(masses,n)
    if len(groups)==0:
        continue
    print(f'1st group variations: {len(groups)}, size: {n}')
    for g in groups:
        rem=get_remainder(masses,g)
        n2=n_masses-len(g)-4 # optimization (min group size is 4)
        groups2=find_groups(rem,n2)
        if len(groups2)==0:
            continue
        print(f'2nd group variations: {len(groups2)}, size: {n2}')
        for g2 in groups2:
            rem2=get_remainder(rem,g2)
            n3=n_masses-len(g)-len(g2)-4
            groups3=find_groups(rem2,n3)
            if len(groups3)==0:
                continue
            print(f'3nd group variations: {len(groups3)}, size: {n3}')
            for g in groups:
                qe=functools.reduce(operator.mul,g)
                if qe<min_qe or min_qe==0:
                    min_qe=qe
                    print(f'1st group: {g}')
                    print(f'2nd group: {g2}')
                    print(f'3rd group: {groups3[0]}')
                    print('min qe:',min_qe)
            print('done')
            exit()

