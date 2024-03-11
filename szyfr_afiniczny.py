def szyfr_afiniczny(a,b,tekst):
    szyfr =''
    
    for litera in tekst:
        d = chr((((ord(litera)-97)*a+b)%26)+97)
        szyfr += d
    return szyfr
    
tekst=input("Podaj tekst: ")
a=int(input("Podaj a: "))
b=int(input("Podaj b: "))

if a==1:
    if b==3:
        print("Szyfr cezara")
    elif b==13:
        print("Szyfr ROT13")
else:
    print("Szyfr afiniczny")

szyfrogram = szyfr_afiniczny(a,b,tekst)
print("Szyfrogram: ",szyfrogram)

def egcd(a,b):
    if a==0:
        return b,0,1
    else:
        d,x,y=egcd(b%a,a)
    return d,y-(b//a)*x,x

def odwrotnosc_modulo(a,m=26):
    d,x,y=egcd(a,m)
    if d!=1:
        print('Błąd!')
    else:
        return x%m


def deszyfr_afiniczny(a,b,szyfrogram):
    tekst=''
    A = odwrotnosc_modulo(a)
    for litera in szyfrogram:
        e = chr((A*((ord(litera)-97)-b))%26+97)
        tekst += e
    return tekst

print("Tekst odszyfr: ", deszyfr_afiniczny(a,b,szyfrogram))
    
