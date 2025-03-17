a = [1,2,3,0,0,0]
b = [2,3,4]
m = 3
n = 3
p1 = m-1
p2 = n-1
p = (m+n) - 1
# print(p)
while p1>=0 and p2>=0:
    if a[p1]>b[p2]:
        a[p] = a[p1]
        p1 -= 1
        
    else:
        a[p] = b[p2]
        p2 -= 1
    p -= 1
while p2>=0:
    a[p] = b[p2]
    p2 -= 1
    p1-=1
print(a)