#!/usr/bin/env python
with open('18.txt','r') as f:
    first_row=f.read().strip()

nrows=400000

# test
#first_row='.^^.^.^^^^'
#nrows=10

#print(first_row)

rowlen=len(first_row)

def check_trap(i,r):
    if i<0 or i>=rowlen:
        return False
    return r[i]=='^'

n_safe=0
for c in first_row:
    if c=='.':
        n_safe+=1

row_i=0
prev_row=first_row
while True:
    row_i+=1
    if row_i==nrows:
        print(f'nrows: {row_i}')
        print(f'safe tiles: {n_safe}')
        exit()
    row=''
    for i in range(rowlen):
        t1=check_trap(i-1,prev_row)
        t2=check_trap(i,prev_row)
        t3=check_trap(i+1,prev_row)
        if (t1 and t2 and not t3) or (not t1 and t2 and t3) or (t1 and not t2 and not t3) or (not t1 and not t2 and t3):
            row+='^'
        else:
            row+='.'
            n_safe+=1
    prev_row=row
    if row_i%50000==0:
        print(f'nrows: {row_i}')

