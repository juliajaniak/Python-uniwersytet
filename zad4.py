def maks_fragment(seq, f):
    max_fragment = None
    if not seq:
        return []
    for i in range(len(seq)):
        for j in range(i+1, len(seq)+1):
            if f(seq[i:j]):
                if max_fragment is None or len(seq[i:j]) > len(max_fragment):
                    max_fragment = seq[i:j]

    return max_fragment
        

def sprawdź_sąsiednie(seq,pred):
    n = len(seq)
    for i in range(n-1):
        if not pred(seq[i], seq[i+1]):
            return False
    return True


def jest_stały(seq):
    return sprawdź_sąsiednie(seq,lambda x,y: x==y)

def jest_rosnący(seq):
    return sprawdź_sąsiednie(seq, lambda x,y: x < y)

  
assert maks_fragment([], lambda s: True) == []
assert maks_fragment([], lambda s: False if s else True) == []
assert maks_fragment([3, 6, 9, 0], lambda s: True) == [3, 6, 9, 0]

s = 'abaaabb'
assert maks_fragment(s, jest_stały) == 'aaa'

s = 'abaaabbb'
assert maks_fragment(s, jest_stały) == 'aaa'

s = 'abaaabbbb'
assert maks_fragment(s, jest_stały) == 'bbbb'

seq = list(range(100_000))

assert maks_fragment(seq, lambda s: True) == seq
assert maks_fragment(seq, lambda s: True if not s else False) == []