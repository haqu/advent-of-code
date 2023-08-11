#!/usr/bin/env python
with open('01.txt','r') as f:
    data=f.read()

# test
#data='R2, L3'
#data='R2, R2, R2'
#data='R5, L5, R5, R3'

commands=[]
for part in data.split(', '):
    commands.append([part[0],int(part[1:])])
#print(commands)

dirs=['N','E','S','W']
ndirs=len(dirs)
dir_index=0
cx,cy=0,0
for cmd in commands:
    if cmd[0]=='R':
        i=dir_index+1
        if i>ndirs-1:
            i=0
    elif cmd[0]=='L':
        i=dir_index-1
        if i<0:
            i=ndirs-1
    dir_index=i
    d=dirs[dir_index]
    if d=='N':
        cy+=cmd[1]
    elif d=='E':
        cx+=cmd[1]
    elif d=='S':
        cy-=cmd[1]
    elif d=='W':
        cx-=cmd[1]

print(abs(cx)+abs(cy))

