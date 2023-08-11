#!/usr/bin/env python

# In state A:
#   0 - Write the value 1. Move one slot to the right. Continue with state B.
#   1 - Write the value 0. Move one slot to the left. Continue with state C.
#
# In state B:
#   0 - Write the value 1. Move one slot to the left. Continue with state A.
#   1 - Write the value 1. Move one slot to the right. Continue with state D.
#
# In state C:
#   0 - Write the value 0. Move one slot to the left. Continue with state B.
#   1 - Write the value 0. Move one slot to the left. Continue with state E.
#
# In state D:
#   0 - Write the value 1. Move one slot to the right. Continue with state A.
#   1 - Write the value 0. Move one slot to the right. Continue with state B.
#
# In state E:
#   0 - Write the value 1. Move one slot to the left. Continue with state F.
#   1 - Write the value 1. Move one slot to the left. Continue with state C.
#
# In state F:
#   0 - Write the value 1. Move one slot to the right. Continue with state D.
#   1 - Write the value 1. Move one slot to the right. Continue with state A.

states_dict={
    'A':((1,1,'B'),(0,-1,'C')),
    'B':((1,-1,'A'),(1,1,'D')),
    'C':((0,-1,'B'),(0,-1,'E')),
    'D':((1,1,'A'),(0,1,'B')),
    'E':((1,-1,'F'),(1,-1,'C')),
    'F':((1,1,'D'),(1,1,'A')),
}
iterations=12667664

# test
#states_dict={
#    'A':((1,1,'B'),(0,-1,'B')),
#    'B':((1,-1,'A'),(1,1,'A'))
#}
#iterations=6

tape={}
cursor=0
state='A'
counter=0

for _ in range(iterations):
    v=tape.get(cursor,0)
    cmd=states_dict[state][v]
    v2=cmd[0]
    if v2>v:
        counter+=1
    elif v2<v:
        counter-=1
    tape[cursor]=v2
    cursor+=cmd[1]
    state=cmd[2]

print(counter)

