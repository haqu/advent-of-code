#!/usr/bin/env python
from hashlib import md5
door_id='ojvtpuvg'
#door_id='abc' # test
password='.'*8
countdown=8
i=-1
while True:
    i+=1
    s=door_id+str(i)
    m=md5(s.encode()).hexdigest()
    if m.startswith('00000'):
        if m[5]>'7':
            continue
        j=int(m[5])
        if password[j]!='.':
            continue
        password=password[:j]+m[6]+password[j+1:]
        print(s,m,password)
        countdown-=1
        if countdown==0:
            exit()

