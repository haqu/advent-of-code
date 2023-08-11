#!/usr/bin/env python
import re
import itertools
import time
from hashlib import md5
from datetime import datetime

with open('11.txt','r') as f:
    lines=f.read().strip().split('\n')

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

materials.append('elerium')
item_id=len(materials)-1
floor_items[0].append(item_id)
floor_items[0].append(item_id+10)
n_items+=2

materials.append('dilithium')
item_id=len(materials)-1
floor_items[0].append(item_id)
floor_items[0].append(item_id+10)
n_items+=2

for arr in floor_items:
    arr.sort()

print('ITEMS:')
for i in range(len(materials)):
    print(  f' {i} - {materials[i]} microchip')
    print(f'{i+10} - {materials[i]} generator')

def print_floors(fi,ef):
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
    print('-----------------------------------')
    print('FLOORS:')
    print('\n'.join(reversed(lines)))
    print('-----------------------------------')

print_floors(floor_items,elevator_floor)

def copy_floor_items(fi):
    arr=[[],[],[],[]]
    for i in range(4):
        for e in fi[i]:
            arr[i].append(e)
    return arr

def get_state_hash(fi,ef):
    return md5((str(fi)+str(ef)).encode(),usedforsecurity=False).hexdigest()

def check_state_is_valid(fi):
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

states_queue=[]
states_queue.append([floor_items,elevator_floor,0])
previous_state_hashes={}
max_move=0

while True:
    state=states_queue.pop(0)
    fi=state[0]
    ef=state[1]
    move=state[2]

    if move>max_move:
        max_move=move
        ts=datetime.now().strftime("%H:%M:%S")
        print(f'{ts} move: {max_move}')

    if len(fi[n_floors-1])==n_items:
        ts=datetime.now().strftime("%H:%M:%S")
        print(f'{ts} done')
        print_floors(fi,ef)
        exit()

    # transfer 1 item
    for i in fi[ef]:
        if ef<n_floors-1: # up floor
            ef2=ef+1
            fi2=copy_floor_items(fi)
            fi2[ef].remove(i)
            fi2[ef2].append(i)
            fi2[ef2].sort()
            h=get_state_hash(fi2,ef2)
            if not previous_state_hashes.get(h,False) and check_state_is_valid(fi2):
                previous_state_hashes[h]=True
                states_queue.append([fi2,ef2,move+1])
        if ef>0: # down floor
            ef2=ef-1
            fi2=copy_floor_items(fi)
            fi2[ef].remove(i)
            fi2[ef2].append(i)
            fi2[ef2].sort()
            h=get_state_hash(fi2,ef2)
            if not previous_state_hashes.get(h,False) and check_state_is_valid(fi2):
                previous_state_hashes[h]=True
                states_queue.append([fi2,ef2,move+1])

    # transfer 2 items
    for group in itertools.combinations(fi[ef],2):
        if ef<n_floors-1: # up floor
            ef2=ef+1
            fi2=copy_floor_items(fi)
            for i in group:
                fi2[ef].remove(i)
                fi2[ef2].append(i)
            fi2[ef2].sort()
            h=get_state_hash(fi2,ef2)
            if not previous_state_hashes.get(h,False) and check_state_is_valid(fi2):
                previous_state_hashes[h]=True
                states_queue.append([fi2,ef2,move+1])
        if ef>0: # down floor
            ef2=ef-1
            fi2=copy_floor_items(fi)
            for i in group:
                fi2[ef].remove(i)
                fi2[ef2].append(i)
            fi2[ef2].sort()
            h=get_state_hash(fi2,ef2)
            if not previous_state_hashes.get(h,False) and check_state_is_valid(fi2):
                previous_state_hashes[h]=True
                states_queue.append([fi2,ef2,move+1])

