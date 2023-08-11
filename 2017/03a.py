#!/usr/bin/env python3
target_index=312051

# test
#target_index=1
#target_index=12
#target_index=23
#target_index=1024

# 37  36  35  34  33  32  31
# 38  17  16  15  14  13  30
# 39  18   5   4   3  12  29
# 40  19   6   1   2  11  28
# 41  20   7   8   9  10  27
# 42  21  22  23  24  25  26
# 43  44  45  46  47  48  49

side=1
index=1
x=0
y=0
while True:
    side+=2
    x+=1
    y+=1
    index+=side*2+(side-2)*2
    print(f'cycle max index: {index}')
    if index>target_index:
        x2,y2=x,y
        while x2>-x:
            if index==target_index:
                print(abs(x2)+abs(y2))
                exit()
            x2-=1
            index-=1
        while y2>-y:
            if index==target_index:
                print(abs(x2)+abs(y2))
                exit()
            y2-=1
            index-=1
        while x2<x:
            if index==target_index:
                print(abs(x2)+abs(y2))
                exit()
            x2+=1
            index-=1
        while y2<y-1:
            if index==target_index:
                print(abs(x2)+abs(y2))
                exit()
            y2+=1
            index-=1

