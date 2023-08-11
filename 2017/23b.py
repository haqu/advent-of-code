#!/usr/bin/env python

# -----------------------------------------------------
# | ASSEMBLY ANALYSIS
# -----------------------------------------------------
#  1   set b 93        b=93             b:93
#  2   set c b         c=b              c:93
#  3   jnz a 2         if a!=0: ip+=2   ----------+
#  4   jnz 1 5         ip+=5                      | ------+
#  5   mul b 100       b*=100           b:9300  <-+       |
#  6   sub b -100000   b+=100000        b:109300          |
#  7   set c b         c=b              c:109300          |
#  8   sub c -17000    c+=17000         c:126300          |
#  9   set f 1         f=1                          <-+ <-+
# 10   set d 2         d=2                            |
# 11   set e 2         e=2                        <-+ |
# 12   set g d         g=d              g:2     <-+ | |
# 13   mul g e         g*=e             g:4       | | |
# 14   sub g b         g-=b             g:-109296 | | |
# 15   jnz g 2         if g!=0: ip+=2   --------+ | | |
# 16   set f 0         f=0              f:0     | | | |
# 17   sub e -1        e+=1             e:3   <-+ | | |
# 18   set g e         g=e              g:3       | | |
# 19   sub g b         g-=b             g:-109297 | | |
# 20   jnz g -8        if g!=0: ip-=8   ----------+ | |
# 21   sub d -1        d+=1                         | |
# 22   set g d         g=d                          | |
# 23   sub g b         g-=b                         | |
# 24   jnz g -13       if g!=0: ip-=13  ------------+ |
# 25   jnz f 2         if f!=0: ip+=2   --+           |
# 26   sub h -1        h+=1               |           |
# 27   set g b         g=b              <-+           |
# 28   sub g c         g-=c                           |
# 29   jnz g 2         if g!=0: ip+=2   --+           |
# 30   jnz 1 3         ip+=3              | --+       |
# 31   sub b -17       b+=17            <-+   |       |
# 32   jnz 1 -23       ip-=23                 | ------+
#                                             V
#                                            END
#
# -----------------------------------------------------
# | CODE RECONSTRUCTION
# -----------------------------------------------------
# b=93*100+100000
# c=b+17000
# while True:
#     f=1
#     d=2
#     e=2
#     while True:
#         while True:
#             if d*e==b:
#                 f=0
#             e+=1
#             if e==b:
#                 break
#         d+=1
#         if d==b:
#             break
#     if f==0:
#         h+=1
#     if b==c:
#         print(h)
#         exit()
#     b+=17
#

b=109300
c=b+17000
h=0
while True:
    f=1
    d=2
    e=2
    while True:
        #while True:
        #    if d*e==b:
        #        f=0
        #    e+=1
        #    if e==b:
        #        break
        if b%d==0:
            f=0
            break
        d+=1
        if d==b:
            break
    if f==0:
        h+=1
    if b==c:
        print(h)
        exit()
    b+=17

