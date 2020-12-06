with open('input.py','r') as f:
    data=f.read().splitlines()


ans=0
cur=set()
for line in data:
    if line:
        cur|=set(line)
    else:
        ans+=len(cur)
        cur.clear()
ans+=len(cur)
print(f'Part 1: {ans}')

ans=0
cur=set('abcdefghijklmnopqrstuvwxyz')
for line in data:
    if line:
        cur&=set(line)
    else:
        ans+=len(cur)
        cur=set('abcdefghijklmnopqrstuvwxyz')
ans+=len(cur)
print(f'Part 2: {ans}')
