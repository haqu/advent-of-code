#!/usr/bin/env python
designer_number=1358
target_coords=[31,39]

# test
#designer_number=10
#target_coords=[7,4]

def check_is_open(x,y):
    v=x*x+3*x+2*x*y+y+y*y+designer_number
    b=format(v,'b')
    return b.count('1')%2==0

states_queue=[[1,1,0]]
prev_states={}
max_move=0

while True:
    state=states_queue.pop(0)
    x=state[0]
    y=state[1]
    move=state[2]

    if move>max_move:
        max_move=move
        print(f'move: {move}')

    if x==target_coords[0] and y==target_coords[1]:
        print(f'done')
        exit()

    # right
    x2=x+1
    y2=y
    cs=f'{x2},{y2}'
    if not prev_states.get(cs,False) and check_is_open(x2,y2):
        prev_states[cs]=True
        states_queue.append([x2,y2,move+1])

    # left
    x2=x-1
    if x2>=0:
        y2=y
        cs=f'{x2},{y2}'
        if not prev_states.get(cs,False) and check_is_open(x2,y2):
            prev_states[cs]=True
            states_queue.append([x2,y2,move+1])

    # up
    y2=y-1
    if y2>=0:
        x2=x
        cs=f'{x2},{y2}'
        if not prev_states.get(cs,False) and check_is_open(x2,y2):
            prev_states[cs]=True
            states_queue.append([x2,y2,move+1])

    # down
    y2=y+1
    x2=x
    cs=f'{x2},{y2}'
    if not prev_states.get(cs,False) and check_is_open(x2,y2):
        prev_states[cs]=True
        states_queue.append([x2,y2,move+1])

