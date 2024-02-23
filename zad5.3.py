#Niech p,q będą dodatnimi liczbami całkowitymi. Napisz program, który wyznaczy liczbę całkowitą x spełniającą równość
# x**3 + p * x = q 
# lub stwierdzi, że takiej liczby nie ma.
#wyszukiwanie binarne


def szukanie(p,q):
  x=0
  pomocny = q
  while x<=pomocny:
    srodek = (x + pomocny) //2
    eq = srodek**3 + p * srodek

    if eq == q:
      return srodek
      
    elif eq<q:
      x = srodek + 1
      
    else:
      pomocny = srodek - 1
  return 'Brak rozwiązania'

assert szukanie(1, 10) == 2
assert szukanie(123456789, 963418328815428240221153430) == 987654321
assert szukanie(2, 10) == 'Brak rozwiązania'
assert szukanie(123, 56798) == 'Brak rozwiązania'



def szukanie(p,q):

  środek = (p+q) // 2
  
  if środek**3 + p*środek == q:
    return środek
  elif środek < q:
    return szukanie(p,środek)
  else:
    return szukanie(środek,q)


