#!/usr/bin/env python
with open('12.txt','r') as f:
    j=f.read()

#j='[1,2,3]'
#j='{"a":2,"b":4}'
#j='[[[3]]]'
#j='{"a":{"b":4},"c":-1}'
#j='{"a":[-1,1]}'
#j='[-1,{"a":1}]'
#j='[]'
#j='{}'

import json
data=json.loads(j)

def get_sum(d):
    if isinstance(d,int):
        return d
    if isinstance(d,dict):
        s=0
        for k,v in d.items():
            s+=get_sum(v)
        return s
    elif isinstance(d,list):
        s=0
        for v in d:
            s+=get_sum(v)
        return s
    else:
        return 0

print(get_sum(data))

