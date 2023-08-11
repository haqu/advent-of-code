#!/usr/bin/env python3
from heapq import heappush,heappop
from itertools import permutations

with open('24.txt','r') as f:
    lines=f.read().strip().split('\n')

#test='''
############
##0.1.....2#
##.#######.#
##4.......3#
############
#'''
#lines=test.strip().split('\n')

#test='''
############
##0#...#...#
##.#.#.#.#.#
##.#.#...#.#
##.#.#####.#
##...#1....#
############
#'''
#lines=test.strip().split('\n')

grid_w=len(lines[0])
grid_h=len(lines)
walls={}
checkpoints=[]

x,y=0,0
for line in lines:
    for c in line:
        if c.isdigit():
            index=int(c)
            while len(checkpoints)<=index:
                checkpoints.append(())
            checkpoints[index]=(x,y)
        elif c=='#':
            walls[(x,y)]=True
        x+=1
    x=0
    y+=1

n_checkpoints=len(checkpoints)
print(f'n_checkpoints: {n_checkpoints}')

def reconstruct_path(came_from, current):
    total_path=[current]
    while current in came_from.keys():
        current=came_from[current]
        total_path.insert(0,current)
    return total_path

def find_path(start,goal,h):
    open_set=[]
    heappush(open_set,(0,start))
    came_from={}
    g_score={}
    g_score[start]=0
    f_score={}
    h=abs(start[0]-goal[0])+abs(start[1]-goal[1])
    f_score[start]=h
    while open_set:
        priority,pos=heappop(open_set)
        if pos==goal:
            return reconstruct_path(came_from,pos)
        x,y=pos
        neighbors=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        for neighbor in neighbors:
            if walls.get(neighbor,False):
                continue
            tentative_score=g_score[pos]+1
            if tentative_score<g_score.get(neighbor,999):
                came_from[neighbor]=pos
                g_score[neighbor]=tentative_score
                h=abs(neighbor[0]-goal[0])+abs(neighbor[1]-goal[1])
                f_score[neighbor]=tentative_score+h
                if not neighbor in open_set:
                    heappush(open_set,(-h,neighbor))
    print('path not found')
    exit()

print('distances between checkpoints:')
distances={}
for i in range(n_checkpoints-1):
    for i2 in range(i+1,n_checkpoints):
        start=checkpoints[i]
        goal=checkpoints[i2]
        path=find_path(start,goal,0)
        n_steps=len(path)-1
        print(f'{i}->{i2}: {n_steps}')
        distances[(i,i2)]=n_steps
        distances[(i2,i)]=n_steps

min_route_len=grid_w*grid_h
perms=permutations(range(1,n_checkpoints))
for perm in perms:
    route_len=0
    prev_index=0
    for index in perm:
        route_len+=distances[(prev_index,index)]
        prev_index=index
    if route_len<min_route_len:
        min_route_len=route_len
        order=[0]+list(perm)
        print(f'min route len: {route_len}, order: {order}')

