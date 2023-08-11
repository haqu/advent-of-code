#!/usr/bin/env python
with open('16.txt','r') as f:
    moves=f.read().strip().split(',')
dancers=list(range(16))

# test
#moves='''
#s1,x3/4,pe/b
#'''.strip().split(',')
#dancers=list(range(5))

letters=[chr(ord('a')+v) for v in dancers]
history={}
history2=[]

def print_dancers(it,dancers):
    s=f'{it:2d} '
    for d in dancers:
        s+=letters[d]
    print(s)

iterations=1000000000
for it in range(iterations):
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
    key=str(dancers)
    if history.get(key,False):
        i=iterations-1
        dancers=history2[i%it]
        print('...')
        print_dancers(i,dancers)
        exit()
    history[key]=True
    history2.append(dancers)
    print_dancers(it,dancers)

