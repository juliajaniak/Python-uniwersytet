def euklides(a,b):
    lst=[a,b]
    while b!=0:
        a,b = b,a%b
        lst.append(b)
    return lst
maks = 0
for b in range(2,1000):
    for a in range(b+1,1001):
        if len(euklides(a,b)) > maks:
            maks = len(euklides(a,b))
            a0,b0 = a,b
print(a0,b0)
