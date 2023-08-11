#!/usr/bin/env python
import re
with open('15.txt', 'r') as f:
    lines = f.read().strip().split('\n')

# data='''
# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# '''
# lines=data.strip().split('\n')

ingredients = []
mix = []
properties = {}

for line in lines:
    m = re.match(
        r'(\S+): capacity (\S+), durability (\S+), flavor (\S+), texture (\S+), calories (\S+)', line).groups()
    name = m[0]
    ingredients.append(name)
    mix.append(0)
    capacity, durability, flavor, texture, calories = [int(v) for v in m[1:]]
    properties[name] = [capacity, durability, flavor, texture, calories]


def increment(m, pos):
    if pos < 0:
        return m
    if m[pos] < 100:
        m[pos] += 1
    else:
        m[pos] = 0
        return increment(m, pos-1)
    return m


mix_len = len(mix)
max_res = 0
countdown = 100**mix_len
while countdown > 0:
    countdown -= 1
    mix = increment(mix, mix_len-1)
    if sum(mix) != 100:
        continue
    res = 1
    for i in range(4):
        v = 0
        for j in range(mix_len):
            p = properties[ingredients[j]][i]
            v += p*mix[j]
        if v < 0:
            v = 0
        res *= v
    if res > max_res:
        max_res = res
        # print(repr(mix))

print(max_res)
