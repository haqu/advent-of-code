#!/usr/bin/env python
puzzle_input=312051

# test
#puzzle_input=800

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...

spiral={}

x0=0
y0=0
spiral[(0,0)]=1

def calc_value(x,y):
    v=0
    nears=[(x-1,y-1),
           (x  ,y-1),
           (x+1,y-1),
           (x-1,y  ),
           (x+1,y  ),
           (x-1,y+1),
           (x  ,y+1),
           (x+1,y+1)]
    for n in nears:
        v+=spiral.get(n,0)
    if v>puzzle_input:
        print(v)
        exit()
    return v

while True:
    x0+=1
    y0+=1
    # up
    x=x0
    for y in range(y0-1,-y0,-1):
        spiral[(x,y)]=calc_value(x,y)
    # left
    y=-y0
    for x in range(x0,-x0,-1):
        spiral[(x,y)]=calc_value(x,y)
    # down
    x=-x0
    for y in range(-y0,y0,1):
        spiral[(x,y)]=calc_value(x,y)
    # right
    y=y0
    for x in range(-x0,x0+1,1):
        spiral[(x,y)]=calc_value(x,y)

