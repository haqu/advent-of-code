#!/usr/bin/env python

with open('22.txt','r') as f:
    lines=f.read().strip().split('\n')

boss_hp0=int(lines[0].split(': ')[1])
boss_damage=int(lines[1].split(': ')[1])

spells=[
    # name,          mana, damage, heal, dot, aot, mot, duration
    # 0              1     2       3     4    5    6    7
    ['MagicMissile', 53,   4,      0,    0,   0,   0,   0],
    ['Drain',        73,   2,      2,    0,   0,   0,   0],
    ['Shield',       113,  0,      0,    0,   7,   0,   6],
    ['Poison',       173,  0,      0,    3,   0,   0,   6],
    ['Recharge',     229,  0,      0,    0,   0,   101, 5],
]

import numpy

mana_spent=0
min_mana_spent=10000
n_wins=0

def check_win(boss_hp):
    if boss_hp<=0:
        global min_mana_spent
        if mana_spent<min_mana_spent:
            min_mana_spent=mana_spent
            print(f'win, min mana spent: {min_mana_spent}')
        return True
    return False

i=0
while True:

    indices_str=str(numpy.base_repr(i,5))
    indices=[int(c) for c in list(indices_str)]
    boss_hp=boss_hp0
    hp=50
    armor=0
    mana=500
    mana_spent=0
    shield_timer=0
    poison_timer=0
    recharge_timer=0
    players_turn=True

    while True:

        if players_turn:
            hp-=1
            if hp<=0:
                #lose
                break

        if shield_timer>0:
            shield_timer-=1
            armor=spells[2][5]
        if poison_timer>0:
            poison_timer-=1
            boss_hp-=spells[3][4]
            if check_win(boss_hp):
                break
        if recharge_timer>0:
            recharge_timer-=1
            mana+=spells[4][6]

        if players_turn:
            if len(indices):
                s=spells[indices.pop(0)]
            else:
                s=spells[0]
            m=s[1]
            if mana<m:
                #lose
                break
            mana-=m
            mana_spent+=m
            if mana_spent>min_mana_spent:
                break
            boss_hp-=s[2]
            if check_win(boss_hp):
                break
            hp+=s[3]
            if s[0]=='Shield':
                shield_timer=s[7]
            elif s[0]=='Poison':
                poison_timer=s[7]
            elif s[0]=='Recharge':
                recharge_timer=s[7]
        else:
            hp-=max(boss_damage-armor,1)
            if hp<=0:
                #lose
                break

        if armor>0 and shield_timer==0:
            armor=0

        players_turn=not players_turn

    i+=1

