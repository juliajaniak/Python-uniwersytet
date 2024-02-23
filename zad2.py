def wykonaj_klucz(klucz):
    if not klucz or len(klucz) > len(set(klucz)) or len(klucz)%2 == 1:
       raise ValueError('nieprawidłowy klucz.')
    
    słownik={}
    for k,v in enumerate(klucz):
        if k%2 == 0:
            słownik[v] = klucz[k+1]
        else:
            słownik[v] = klucz[k-1]

    return słownik

def wykonaj_szyfrator(klucz='malinowebuty'):
    słownik = wykonaj_klucz(klucz)

    def szyfrator(tekst):
        tajny=''

        for znak in tekst:
            if znak in słownik:
                tajny += słownik[znak]
            else:
                tajny += znak
        return tajny
    return szyfrator

import timeit
tekst = 100000 * 'a'
szyfrator = wykonaj_szyfrator()
print(timeit.timeit('szyfrator(tekst)', globals=globals(), number=300))

szyfry_test = {'a': 'm', 'm': 'a', 
               'x': 'x', 'A': 'A', 
               'malinowebuty': 'amilonewubyt', 
               'ziemia jest płaska': 'zlwalm jwsy płmskm'}

try:
    malinowebuty = wykonaj_szyfrator()
except TypeError:
    raise AssertionError('Czy uczyniłeś "malinowebuty" wartością domyślną?')

for jawny, tajny in szyfry_test.items():
    assert malinowebuty(jawny) == tajny, 'Błąd, powinno być: {} ==> {}'.format(jawny, tajny)

test_klucz_jawny_tajny = [('ab', 'abc', 'bac'),
                          ('XYUV', 'xVyU', 'xUyV'),
                          ('gaderypoluki', 'gaderypoluki', 'agedyropulik')]

for klucz, jawny, tajny in test_klucz_jawny_tajny:
    szyfruj = wykonaj_szyfrator(klucz)
    assert szyfruj(jawny) == tajny, 'Klucz {} zamienia {} na {}'.format(klucz, jawny, tajny)




klucz = 'abcd'
assert wykonaj_klucz(klucz) == dict(a='b', b='a', c='d', d='c')

klucz = 'malinowebuty'
assert wykonaj_klucz(klucz) == dict(m='a', a='m', l='i', i='l',
                                    n='o', o='n', w='e', e='w',
                                   b='u', u='b', t='y', y='t')

nieprawidłowe_klucze = ['', 'x', 'xyz', 'xyzx']

for klucz in nieprawidłowe_klucze:
    try:
        wykonaj_klucz(klucz)
    except ValueError as err:
        assert str(err) == 'nieprawidłowy klucz.', 'Niewłaściwy komunikat.'
    else:
        raise AssertionError("'{}' nie jest prawidłowym kluczem!".format(klucz))