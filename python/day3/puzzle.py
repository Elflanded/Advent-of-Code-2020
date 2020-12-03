m = [e for e in open("input.py","rt").read().split()]

def count(m:list,r:int,b:int)->int:
  w = len(m[0])
  p = 0
  c = 0
  for i in range(0,len(m),b):
    if m[i][p]=='#':
      c += 1
    p = (p+r)%w
  return c

print( count(m,3,1) )

p = 1
for r,b in ((1,1),(3,1),(5,1),(7,1),(1,2)):
  p *= count(m,r,b)
print( p )
