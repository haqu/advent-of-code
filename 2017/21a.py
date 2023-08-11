#!/usr/bin/env python

grid='''
.#.
..#
###
'''.strip().replace('\n','')

grid_w=3
grid_h=3

with open('21.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#lines='''
#../.# => ##./#../...
#.#./..#/### => #..#/..../..../#..#
#'''.strip().split('\n')

rules={}
for line in lines:
    lp,rp,*_=line.split(' => ')
    lp=lp.replace('/','')
    rp=rp.replace('/','')
    rules[lp]=rp

for lp in list(rules.keys()):
    lplen=len(lp)
    lp2=['.']*lplen
    if lplen==4:
        sz=2
    else:
        sz=3
    for _ in range(4):
        # flip x
        for y in range(sz):
            for x in range(sz):
                lp2[x+y*sz]=lp[sz-1-x+y*sz]
        rules[''.join(lp2)]=rules[lp]
        # flip y
        for y in range(sz):
            for x in range(sz):
                lp2[x+y*sz]=lp[x+(sz-1-y)*sz]
        rules[''.join(lp2)]=rules[lp]
        # rotate 90
        for y in range(sz):
            for x in range(sz):
                lp2[x+y*sz]=lp[y+(sz-1-x)*sz]
        rules[''.join(lp2)]=rules[lp]
        lp=''.join(lp2)

print(f'rules: {len(rules)}')

for it in range(5):
    if grid_w%2==0:
        pw=int(grid_w/2)
        ph=int(grid_h/2)
        grid2_w=pw*3
        grid2_h=ph*3
        grid2=['.']*grid2_w*grid2_h
        for i0 in range(ph):
            for j0 in range(pw):
                for pattern in rules:
                    if len(pattern)!=4:
                        continue
                    valid=True
                    for y in range(2):
                        for x in range(2):
                            if grid[j0*2+x+(i0*2+y)*grid_w]!=pattern[x+y*2]:
                                valid=False
                                break
                        if not valid:
                            break
                    if not valid:
                        continue
                    pattern2=rules[pattern]
                    for y in range(3):
                        for x in range(3):
                            grid2[j0*3+x+(i0*3+y)*grid2_w]=pattern2[x+y*3]
    else:
        pw=int(grid_w/3)
        ph=int(grid_h/3)
        grid2_w=pw*4
        grid2_h=ph*4
        grid2=['.']*grid2_w*grid2_h
        for i0 in range(ph):
            for j0 in range(pw):
                for pattern in rules:
                    if len(pattern)!=9:
                        continue
                    valid=True
                    for y in range(3):
                        for x in range(3):
                            if grid[j0*3+x+(i0*3+y)*grid_w]!=pattern[x+y*3]:
                                valid=False
                                break
                        if not valid:
                            break
                    if not valid:
                        continue
                    pattern2=rules[pattern]
                    for y in range(4):
                        for x in range(4):
                            grid2[j0*4+x+(i0*4+y)*grid2_w]=pattern2[x+y*4]
    grid=grid2
    grid_w=grid2_w
    grid_h=grid2_h
    total=0
    line=''
    for y in range(grid_h):
        for x in range(grid_w):
            c=grid[x+y*grid_w]
            line+=c
            if c=='#':
                total+=1
        print(line)
        line=''
    print(f'{it+1} {total} {grid_w}x{grid_h}')
    input()


