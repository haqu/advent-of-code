#!/usr/bin/env python
with open('16.txt','r') as f:
    moves=f.read().strip().split(',')
dancers=list(range(16))

# test
#moves='''
#s1,x3/4,pe/b
#'''.strip().split(',')
#dancers=list(range(5))

def print_dancers():
    s=''
    for d in dancers:
        s+=letters[d]
    print(s)

letters=[chr(ord('a')+v) for v in dancers]
for m in moves:
    if m.startswith('s'):
        n=int(m[1:])
        dancers=dancers[-n:]+dancers[:-n]
    elif m.startswith('x'):
        p=m[1:].split('/')
        i1,i2=int(p[0]),int(p[1])
        dancers[i1],dancers[i2]=dancers[i2],dancers[i1]
    elif m.startswith('p'):
        p=m[1:].split('/')
        i1=dancers.index(letters.index(p[0]))
        i2=dancers.index(letters.index(p[1]))
        dancers[i1],dancers[i2]=dancers[i2],dancers[i1]

print_dancers()

