#!/usr/bin/env python
import re
import itertools
from hashlib import md5

with open('11.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
#The second floor contains a hydrogen generator.
#The third floor contains a lithium generator.
#The fourth floor contains nothing relevant.
#'''
#lines=data.strip().split('\n')

materials=[]
floor_items=[]
elevator_floor=0
n_floors=0
n_items=0

for line in lines:
    line=line.replace(' a ',' ').replace(', and ',', ').replace(' and ',', ').replace('-compatible','').replace('.','')
    floor_items.append([])
    n_floors+=1
    lp,rp=line.split(' contains ')
    if 'first' in lp:
        floor_index=0
    elif 'second' in lp:
        floor_index=1
    elif 'third' in lp:
        floor_index=2
    elif 'fourth' in lp:
        floor_index=3
    if 'nothing' in rp:
        continue
    arr=rp.split(', ')
    for part in arr:
        material,device,*_=part.split(' ')
        if not material in materials:
            materials.append(material)
            item_id=len(materials)-1
        else:
            item_id=materials.index(material)
        if device=='generator':
            item_id+=10
        floor_items[floor_index].append(item_id)
        n_items+=1

def debug_print_floors(fi,ef):
    lines=[]
    for index in range(4):
        line=f'F{index+1} '
        items=fi[index]
        if ef==index:
            line+='E '
        else:
            line+='. '
        for i in items:
            line+=f'{i} '
        lines.append(line)
    print('------------------------------')
    print('\n'.join(reversed(lines)))
    print('------------------------------')

debug_print_floors(floor_items,elevator_floor)

def copy_floor_items(fi):
    arr=[[],[],[],[]]
    for i in range(4):
        for e in fi[i]:
            arr[i].append(e)
    return arr

def check_is_valid(fi):
    for index in range(4):
        gens=[]
        microchips=[]
        for i in fi[index]:
            if i<10:
                microchips.append(i)
            else:
                gens.append(i)
        if not len(gens):
            continue
        for m in microchips:
            if not (m+10) in gens:
                return False
    return True

queue=[]
queue.append([floor_items,elevator_floor,0])
state_hashes=[]
max_move=0

while True:
    state=queue.pop(0)

    fi=state[0]
    ef=state[1]
    move=state[2]

    h=md5((str(fi)+str(ef)).encode(),usedforsecurity=False).hexdigest()
    if h in state_hashes:
        continue
    state_hashes.append(h)

    if move>max_move:
        max_move=move
        print(max_move)

    if len(fi[n_floors-1])==n_items:
        print('done')
        debug_print_floors(fi,ef)
        exit()

    # transfer 1 item
    for i in fi[ef]:
        if ef<n_floors-1: # up floor
            ef2=ef+1
            fi2=copy_floor_items(fi)
            fi2[ef].remove(i)
            fi2[ef2].append(i)
            fi2[ef2].sort()
            if check_is_valid(fi2):
                queue.append([fi2,ef2,move+1])
        if ef>0: # down floor
            ef2=ef-1
            fi2=copy_floor_items(fi)
            fi2[ef].remove(i)
            fi2[ef2].append(i)
            fi2[ef2].sort()
            if check_is_valid(fi2):
                queue.append([fi2,ef2,move+1])

    # transfer 2 items
    for group in itertools.combinations(fi[ef],2):
        if ef<n_floors-1: # up floor
            ef2=ef+1
            fi2=copy_floor_items(fi)
            for i in group:
                fi2[ef].remove(i)
                fi2[ef2].append(i)
            fi2[ef2].sort()
            if check_is_valid(fi2):
                queue.append([fi2,ef2,move+1])
        if ef>0: # down floor
            ef2=ef-1
            fi2=copy_floor_items(fi)
            for i in group:
                fi2[ef].remove(i)
                fi2[ef2].append(i)
            fi2[ef2].sort()
            if check_is_valid(fi2):
                queue.append([fi2,ef2,move+1])

