#!/usr/bin/env python
import hashlib
secret_key='iwrupvqb'
num=0
while True:
    str=f'{secret_key}{num}'
    md5=hashlib.md5(str.encode()).hexdigest()
    if md5[:5]=='00000':
        print(num)
        exit()
    num+=1

