#!/usr/bin/env python
from hashlib import md5
door_id='ojvtpuvg'
#door_id='abc' # test
password=''
i=0
while True:
    s=door_id+str(i)
    m=md5(s.encode()).hexdigest()
    if m.startswith('00000'):
        password+=m[5]
        print(s,m,password)
        if len(password)==8:
            exit()
    i+=1

