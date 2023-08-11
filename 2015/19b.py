#!/usr/bin/env python
with open('19.txt','r') as f:
    lines=f.read().strip().split('\n')

# test
#data='''
#e => H
#e => O
#H => HO
#H => OH
#O => HH
#
#HOH
#'''
#lines=data.strip().split('\n')

rep={}

next_line_is_molecule=False
for line in lines:
    if line=='':
        next_line_is_molecule=True
        continue
    if not next_line_is_molecule:
        p2,p1,*_=line.split(' => ') # reverse
        a=rep.get(p1,[])
        a.append(p2)
        rep[p1]=a
    else:
        molecule=line

#print(repr(rep))
#print(molecule)
molecule_len=len(molecule)

import re
import random

class Node(object):
    def __init__(self,data):
        self.data=data
        self.nodes=[]
        self.parent=None
        self.depth=0
    def add(self,data):
        n=Node(data)
        self.nodes.append(n)
        n.parent=self
        n.depth=self.depth+1
        return n

def grow_tree(n):
    for p1 in rep:
        arr=rep[p1].copy()
        for m in re.finditer(p1,n.data):
            for p2 in arr:
                var=n.data[:m.start()]
                var+=p2
                var+=n.data[m.end():]
                n2=n.add(var)
                if var=='e':
                    print(n2.depth)
                    exit()
                grow_tree(n2)

root=Node(molecule)
grow_tree(root) # grow tree from molecule to 'e'

