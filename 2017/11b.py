#!/usr/bin/env python
with open('11.txt','r') as f:
    dirs=f.read().strip().split(',')

# test
#dirs='''
#se,sw,se,sw,sw
#'''.strip().split(',')

def new_pos_with_dir(p,d):
    x,y=p
    if d=='n':
        return (x,y-1)
    if d=='s':
        return (x,y+1)
    e=1-int(x%2)
    if d=='nw':
        return (x-1,y-1+e)
    if d=='ne':
        return (x+1,y-1+e)
    if d=='sw':
        return (x-1,y+e)
    if d=='se':
        return (x+1,y+e)

from heapq import heappush,heappop

def get_space_pos(p):
    x,y=p
    if x%2==1:
        return (float(x),float(y)-0.5)
    else:
        return (float(x),float(y))

def get_distance(p1,p2):
    x1,y1=get_space_pos(p1)
    x2,y2=get_space_pos(p2)
    return abs(x1-x2)+abs(y1-y2)

def reconstruct_path(came_from,pos):
    path=[pos]
    while pos in came_from.keys():
        pos=came_from[pos]
        path.insert(0,pos)
    return path

def find_path(start,end):
    open_set=[]
    heappush(open_set,(0,start))
    came_from={}
    g_score={}
    g_score[start]=0
    f_score={}
    h=get_distance(start,end)
    f_score[start]=h
    while open_set:
        priority,pos=heappop(open_set)
        if pos==end:
            return reconstruct_path(came_from,pos)
        x,y=pos
        near_dirs=['n','ne','se','s','sw','nw']
        for d in near_dirs:
            near=new_pos_with_dir(pos,d)
            tentative_score=g_score[pos]+1
            if tentative_score<g_score.get(near,99999):
                came_from[near]=pos
                g_score[near]=tentative_score
                h=get_distance(near,end)
                f_score[near]=tentative_score+h
                if not near in open_set:
                    heappush(open_set,(h,near))
    print('path not found')
    exit()

max_n_steps=0
pos=(0,0)
for d in dirs:
    pos=new_pos_with_dir(pos,d)
    path=find_path((0,0),pos)
    n_steps=len(path)-1
    if n_steps>max_n_steps:
        max_n_steps=n_steps
        print(max_n_steps)

