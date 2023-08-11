#!/usr/bin/env python3
import time
from heapq import heappush,heappop

with open('22.txt','r') as f:
    lines=f.read().strip().split('\n')
lines.pop(0)
lines.pop(0)

#test='''
#Filesystem            Size  Used  Avail  Use%
#/dev/grid/node-x0-y0   10T    8T     2T   80%
#/dev/grid/node-x0-y1   11T    6T     5T   54%
#/dev/grid/node-x0-y2   32T   28T     4T   87%
#/dev/grid/node-x1-y0    9T    7T     2T   77%
#/dev/grid/node-x1-y1    8T    0T     8T    0%
#/dev/grid/node-x1-y2   11T    7T     4T   63%
#/dev/grid/node-x2-y0   10T    6T     4T   60%
#/dev/grid/node-x2-y1    9T    8T     1T   88%
#/dev/grid/node-x2-y2    9T    6T     3T   66%
#'''
#lines=test.strip().split('\n')
#lines.pop(0)

nodes=[]
grid_w=0
grid_h=0

import re
for line in lines:
    m=re.match(r'/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%',line).groups()
    x=int(m[0])
    y=int(m[1])
    used=int(m[3])
    avail=int(m[4])
    nodes.append([x,y,used,avail])
    if x>grid_w-1:
        grid_w=x+1
    if y>grid_h-1:
        grid_h=y+1

used_grid=[0]*grid_w*grid_h
avail_grid=[0]*grid_w*grid_h
for node in nodes:
    x,y=node[0],node[1]
    used=node[2]
    avail=node[3]
    used_grid[x+y*grid_w]=used
    avail_grid[x+y*grid_w]=avail

def print_used_grid(used_grid):
    print('-USED--------------------')
    for y in range(grid_h):
        line=''
        for x in range(grid_w):
            used=used_grid[x+y*grid_w]
            line+=f'{used:3d} '
        print(line)
    print('-------------------------')

def print_avail_grid(avail_grid):
    print('-AVAIL-------------------')
    for y in range(grid_h):
        line=''
        for x in range(grid_w):
            avail=avail_grid[x+y*grid_w]
            line+=f'{avail:3d} '
        print(line)
    print('-------------------------')

def reconstruct_path(came_from, current):
    total_path=[current]
    while current in came_from.keys():
        current=came_from[current]
        total_path.insert(0,current)
    return total_path

def find_path(start,end,used_grid,avail_grid):
    queue=[]
    heappush(queue,(0,start,used_grid,avail_grid))
    came_from={}
    g_score={}
    g_score[start]=0
    f_score={}
    h=abs(start[0]-end[0])+abs(start[1]-end[1])
    f_score[start]=h
    while queue:
        pri,pos,used_grid,avail_grid=heappop(queue)
        if pos==end:
            return (reconstruct_path(came_from,pos),used_grid,avail_grid)
        x,y=pos
        avail=avail_grid[x+y*grid_w]
        nears=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for near in nears:
            x2,y2=near
            if x2<0 or x2>grid_w-1 or y2<0 or y2>grid_h-1:
                continue
            if x2==data_pos[0] and y2==data_pos[1]:
                # skip data cell
                continue
            used2=used_grid[x2+y2*grid_w]
            #print(pos,near,used2,avail)
            if used2>avail:
                continue
            n_used_grid=used_grid.copy()
            n_used_grid[x2+y2*grid_w]=0
            n_used_grid[x+y*grid_w]+=used2
            n_avail_grid=avail_grid.copy()
            n_avail_grid[x+y*grid_w]-=used2
            n_avail_grid[x2+y2*grid_w]+=used2
            #print_used_grid(n_used_grid)
            #print_avail_grid(n_avail_grid)
            t_score=g_score[pos]+1
            if t_score<g_score.get(near,999):
                came_from[near]=pos
                g_score[near]=t_score
                h=abs(near[0]-end[0])+abs(near[1]-end[1])
                f_score[near]=t_score+h
                if not near in queue:
                    heappush(queue,(-h,near,n_used_grid,n_avail_grid))
    print('path not found')
    exit()

#print_used_grid(used_grid)
#print_avail_grid(avail_grid)

max_avail=0
for y in range(grid_h):
    for x in range(grid_w):
        avail=avail_grid[x+y*grid_w]
        if avail>max_avail:
            max_avail=avail
            start=(x,y)
print(f'max avail: {max_avail}')
print(f'start: {start}')

moves=0
data_pos=(grid_w-1,0)
end=(data_pos[0]-1,data_pos[1])
print(f'end: {end}')
path,used_grid,avail_grid=find_path(start,end,used_grid,avail_grid)
moves+=len(path)-1
print(f'moves: {moves}')

#print_used_grid(used_grid)
#print_avail_grid(avail_grid)

while True:

    print('move data cell left')
    x2,y2=data_pos
    x,y=x2-1,y2
    avail=avail_grid[x+y*grid_w]
    used2=used_grid[x2+y2*grid_w]
    if used2>avail:
        print('error')
        exit()
    used_grid[x2+y2*grid_w]=0
    used_grid[x+y*grid_w]+=used2
    avail_grid[x+y*grid_w]-=used2
    avail_grid[x2+y2*grid_w]+=used2
    moves+=1
    data_pos=(data_pos[0]-1,data_pos[1])
    if data_pos==(0,0):
        print('done')
        print(f'moves: {moves}')
        exit()

    #print_used_grid(used_grid)
    #print_avail_grid(avail_grid)

    start=x+1,y
    end=x-1,y
    path,used_grid,avail_grid=find_path(start,end,used_grid,avail_grid)
    moves+=len(path)-1
    print(f'moves: {moves}')

    #print_used_grid(used_grid)
    #print_avail_grid(avail_grid)
