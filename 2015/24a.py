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
n_masses=len(masses)
total_mass=sum(masses)
group_mass=total_mass/3
#print(total_mass)
#print(group_mass)

masses.sort(reverse=True)
#print(masses)

import itertools
import functools
import operator

if group_mass in masses:
    print(group_mass)
    exit()

min_qe=0
should_stop=False
count=2
while True:
    print(f'first group size: {count}')
    first_groups=list(itertools.combinations(masses,count))
    first_groups_masses=[]
    first_groups_qe=[]
    for g in first_groups:
        first_groups_masses.append(functools.reduce(operator.add,g))
        first_groups_qe.append(functools.reduce(operator.mul,g))
    for i in range(len(first_groups)):
        if group_mass==first_groups_masses[i]:
            is_valid=False
            rem_masses=masses.copy()
            for m in first_groups[i]:
                rem_masses.remove(m)
            if group_mass in rem_masses:
                is_valid=True
            else:
                for n in range(2,n_masses-count):
                    groups=list(itertools.combinations(rem_masses,n))
                    for g in groups:
                        m=functools.reduce(operator.add,g)
                        if m==group_mass:
                            is_valid=True
                            break
                    if is_valid:
                        break
            if is_valid:
                qe=first_groups_qe[i]
                if qe<min_qe or min_qe==0:
                    min_qe=qe
                    print(f'min qe: {min_qe}')
                    should_stop=True
    if should_stop:
        print('done')
        exit()
    count+=1

