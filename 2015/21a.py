#!/usr/bin/env python

with open('21.txt','r') as f:
    lines=f.read().strip().split('\n')

boss_hp0=int(lines[0].split(': ')[1])
boss_damage0=int(lines[1].split(': ')[1])
boss_armor0=int(lines[2].split(': ')[1])

weapons=[
    [8,   4],
    [10,  5],
    [25,  6],
    [40,  7],
    [74,  8],
]
armors=[
    [13,  1],
    [31,  2],
    [53,  3],
    [75,  4],
    [102, 5],
]
rings=[
    [25,  1,  0],
    [50,  2,  0],
    [100, 3,  0],
    [20,  0,  1],
    [40,  0,  2],
    [80,  0,  3],
]

indices=[1,0,0,0]
# 0 - weapon - 1..5
# 1 - armor  - 0..5 (0 is no armor)
# 2 - ring1  - 0..6 (0 is no ring)
# 3 - ring2  - 0..6 (0 is no ring)

def increment_indices(pos):
    indices[pos]+=1
    if pos==0 and indices[pos]>5: # weapon
        indices[pos]=1
    elif pos==1 and indices[pos]>5: # armor
        indices[pos]=0
        increment_indices(pos-1)
    elif pos==2 and indices[pos]>6: # ring1
        indices[pos]=0
        increment_indices(pos-1)
    elif pos==3 and indices[pos]>6: # ring2
        indices[pos]=0
        increment_indices(pos-1)

min_gold_spent=999
countdown=5*6*7*7
while countdown>0:

    boss_hp=boss_hp0
    boss_damage=boss_damage0
    boss_armor=boss_armor0
    hp=100
    damage=0
    armor=0
    gold_spent=0
    players_turn=True

    it=weapons[indices[0]-1]
    gold_spent+=it[0]
    damage=it[1]
    if indices[1]==0:
        armor=0
    else:
        it=armors[indices[1]-1]
        gold_spent+=it[0]
        armor=it[1]
    if indices[2]>0:
        r=rings[indices[2]-1]
        gold_spent+=r[0]
        damage+=r[1]
        armor+=r[2]
    if indices[3]>0:
        r=rings[indices[3]-1]
        gold_spent+=r[0]
        damage+=r[1]
        armor+=r[2]

    while True:
        if players_turn:
            boss_hp-=max(damage-boss_armor,1)
            if boss_hp<=0:
                print(f'win, gold_spent: {gold_spent}')
                if gold_spent<min_gold_spent:
                    min_gold_spent=gold_spent
                break
        else:
            hp-=max(boss_damage-armor,1)
            if hp<=0:
                break
        players_turn=not players_turn

    countdown-=1
    increment_indices(3)

print('min gold spent: ',min_gold_spent)
