def bliźniacze(n):
    '''
    '''
    lst2=['F','F']
    for m in range(2,n+1):
        lst2.append('T')
    for k in range(2,len(lst2)):
        for p in range(k+1,len(lst2)):
            if p % k == 0:
                lst2[p] = 'F'
    lst=[]
    for i in range(0,len(lst2)):
        if lst2[i]=='T':
            lst.append(i)
    blizniacze=[]
    for b in range(0,len(lst)):
        for a in range(b+1,len(lst)):
            if abs(lst[b] - lst[a]) == 2:
                blizniacze.append((lst[b],lst[a]))
                break
    return blizniacze
assert bliźniacze(20) == [(3, 5), (5, 7), (11, 13), (17, 19)]

# http://www.wolframalpha.com/input/?i=number+of+twin+primes+less+than+200
assert len(bliźniacze(200)) == 15

assert bliźniacze.__doc__, 'Nie napisałeś docstringu!'
