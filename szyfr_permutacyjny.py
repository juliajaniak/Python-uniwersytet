import numpy

def wypisz(L,n):
    for i in range(n):
        print("%s"%L[i],end='') 

def kod(tekst):
    T=[]
    for i in tekst:
        T.append(ord(i)-97)
    return T

def dekod(szyfr):
    L=[]
    for i in szyfr:
        L.append(chr(i+97))
    return L 

def szyfr_permutacyjny(T,M):
    A = numpy.array(M)
    b = numpy.array(T)
    return numpy.dot(A,b)

tekst = input('Podaj tekst: ')
T = kod(tekst)
n = len(tekst)
init = [i for i in range(n)]
find = list(numpy.random.permutation(init)) 

M = numpy.zeros((n,n), dtype=int) 
M[init,find]=1

C=szyfr_permutacyjny(T,M)
S=dekod(C) 
print("Szyfrogram: ")
wypisz(S,n)
print("\nM=\n",M)

##funkcja deszyfrująca
szyfrogram=input("\nPodaj szyfrogram: ")
S = kod(szyfrogram)
n = len(szyfrogram)

def zamien(d):
    nowy={}
    for klucze,wartosci in d.items():
        nowy[wartosci] = klucze
    return nowy

def sortuj(d):
    sortowane = {}
    sort_klucze=sorted(d.keys())
    for klucz in sort_klucze:
        sortowane[klucz] = d[klucz]
    return sortowane

d={}
for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] == 1:
            d[i] = j 


sortowanie = sortuj(d) 
zamiana = zamien(sortowanie) 


M1=numpy.zeros((n,n), dtype=int)
for klucze, wartosci in zamiana.items():
    M1[klucze,wartosci] = 1 

print("\nM1=\n",M1)
K=szyfr_permutacyjny(S,M1)
O=dekod(K)
print("Tekst odszyfrowany: ")
wypisz(O,n)