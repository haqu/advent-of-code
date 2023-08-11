#!/usr/bin/env python

print('TOO SLOW')
target=33100000
house=770000
max_presents=0
while True:
    house+=1
    divisors=[1]
    for i in range(2,int(house/2)+1):
        if house%i==0:
            divisors.append(i)
    if house>1:
        divisors.append(house)
    presents=0
    for d in divisors:
        presents+=d*10
    if presents>max_presents:
        max_presents=presents
        print(f'presents: {presents}, house: {house}')
        if presents>=target:
            print('done')
            exit()

