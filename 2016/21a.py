#!/usr/bin/env python
with open('21.txt','r') as f:
    lines=f.read().strip().split('\n')

password='abcdefgh'

#test='''
#swap position 4 with position 0
#swap letter d with letter b
#reverse positions 0 through 4
#rotate left 1 step
#move position 1 to position 4
#move position 3 to position 0
#rotate based on position of letter b
#rotate based on position of letter d
#'''
#lines=test.strip().split('\n')
#password='abcde'

print(password)
for line in lines:
    print('-------------------------')
    print(line)
    if line.startswith('swap position'):
        parts=line.split(' ')
        p1=int(parts[2])
        p2=int(parts[5])
        arr=list(password)
        arr[p1],arr[p2]=arr[p2],arr[p1]
        password=''.join(arr)
        print(password)
        continue
    elif line.startswith('swap letter'):
        parts=line.split(' ')
        c1,c2=parts[2],parts[5]
        password=password.replace(c1,'T')
        password=password.replace(c2,c1)
        password=password.replace('T',c2)
        print(password)
    elif line.startswith('rotate'):
        parts=line.split(' ')
        if parts[1]=='left':
            arr=list(password)
            steps=int(parts[2])
            while steps>0:
                c=arr.pop(0)
                arr.append(c)
                steps-=1
            password=''.join(arr)
        elif parts[1]=='right':
            arr=list(password)
            steps=int(parts[2])
            while steps>0:
                c=arr.pop()
                arr.insert(0,c)
                steps-=1
            password=''.join(arr)
        elif parts[1]=='based':
            arr=list(password)
            steps=arr.index(parts[6])
            if steps>=4:
                steps+=1
            steps+=1
            while steps>0:
                c=arr.pop()
                arr.insert(0,c)
                steps-=1
            password=''.join(arr)
        print(password)
        continue
    elif line.startswith('reverse'):
        parts=line.split(' ')
        arr=list(password)
        i0=int(parts[2])
        i1=int(parts[4])
        arr2=arr[:i0]
        arr2+=list(reversed(arr[i0:i1+1]))
        if i1<len(password)-1:
            arr2+=arr[i1+1:]
        password=''.join(arr2)
        print(password)
        continue
    elif line.startswith('move position'):
        parts=line.split(' ')
        arr=list(password)
        p1=int(parts[2])
        p2=int(parts[5])
        c=arr.pop(p1)
        arr.insert(p2,c)
        password=''.join(arr)
        print(password)
        continue


