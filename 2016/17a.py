#!/usr/bin/env python
passcode='pxxbnzuo'

# test
#passcode='hijkl'
#passcode='ihgpwlah'

states=[[0,0,'']]
target=[3,3]

from hashlib import md5
while True:
    if not len(states):
        print('no path')
        exit()
    state=states.pop(0)
    x=state[0]
    y=state[1]
    path=state[2]
    if x==target[0] and y==target[1]:
        print(path)
        exit()
    h=md5((passcode+path).encode()).hexdigest()
    print(h[:4],x,y,path)
    # 0 1 2 3
    # U D L R
    # up
    x2=x
    y2=y-1
    if y2>=0 and h[0]>'a':
        states.append([x2,y2,path+'U'])
    # down
    x2=x
    y2=y+1
    if y2<4 and h[1]>'a':
        states.append([x2,y2,path+'D'])
    # left
    x2=x-1
    y2=y
    if x2>=0 and h[2]>'a':
        states.append([x2,y2,path+'L'])
    # right
    x2=x+1
    y2=y
    if x2<4 and h[3]>'a':
        states.append([x2,y2,path+'R'])

