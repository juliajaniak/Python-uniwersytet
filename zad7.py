def szyfruj(tekst, klucz='malinowebuty'):
    while True:
        klucz2=[]
        for j in range(0,len(klucz)):
            klucz2.append(klucz[j])
        klucz21=set(klucz2)
        if (len(klucz2)>len(klucz21) and len(klucz)%2!=0) or len(klucz2)>len(klucz21) or len(klucz)%2!=0:
            raise ValueError('Nieprawidłowy klucz!')
        break
    nowy=''
    for i in range(0,len(tekst)):
        if tekst[i] in klucz:
            if klucz.index(tekst[i])%2==0:
                nowy += klucz[klucz.index(tekst[i])+1]
            else:
                nowy += klucz[klucz.index(tekst[i])-1]
        else:
            nowy += str(tekst[i])
    return nowy

# W słowniku szyfry_test klucz to tekst do zaszyfrowania, 
# wartość to klucz po zaszyfrowaniu. 
szyfry_test = {'a': 'm', 'm': 'a', 
               'x': 'x', 'A': 'A', 
               'malinowebuty': 'amilonewubyt', 
               'ziemia jest płaska': 'zlwalm jwsy płmskm'}

for jawny, tajny in szyfry_test.items():
    assert szyfruj(str(jawny)) == str(tajny)

# Nieprawidłowe klucze do testowania wyjątków.
nieprawidłowe_klucze = ['x', 'xyz', 'xyzx']
for klucz in nieprawidłowe_klucze:
    try:
        szyfruj('abc', klucz)
    except ValueError as err:
        assert str(err) == 'Nieprawidłowy klucz!', 'Niewłaściwy komunikat.'
    except Exception as err:
        raise AssertionError('Nieprawidłowy wyjątek {!r}'.format(err))
    else:
        raise AssertionError(f"Brak wyjątku: '{klucz}' nie jest prawidłowym kluczem!")

# Krotki (klucz, tekst_jawny, tekst_tajny)
test_klucz_jawny_tajny = [('ab', 'abc', 'bac'),
                          ('XYUV', 'xVyU', 'xUyV'),
                          ('gaderypoluki', 'gaderypoluki', 'agedyropulik')]

for klucz, jawny, tajny in test_klucz_jawny_tajny:
    assert szyfruj(str(jawny), str(klucz)) == str(tajny)