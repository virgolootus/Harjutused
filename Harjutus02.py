import math
#Ülesanne 02
#Virgo Lootus
#31.01.2022

#kütusekulu arvutamine

liitrid = int(input("sisestage tangitud kütuse liitrid: "))
km = int(input("sisestage läbitud kilomeetrid: "))
dist = 100
kulu = liitrid/(km/100)
print("keskmine kütuse kulu",kulu,"liitrit 100km kohta")

#arvusüsteemid

täisarv = int(input("sisestage kümnendarv: "))
print(bin(täisarv))
print(hex(täisarv))

#ajateisendus

aeg = int(input("sisestage aeg minutites: "))
tunnid = aeg//60
minutid = aeg%60
print(tunnid,":",minutid) 

#hüpotenuus

a = 16
b = 9
c = math.sqrt(a**2+b**2)
print("hüpotenuus on",c)

#rulluisutajad

kiirus = 29.9
aeg = 0.4

summa = (kiirus/aeg)
print(summa)

#pitsa

sopru = 3
hind = 12.90
jootraha = 0.1

summa=(hind+hind*jootraha)/sopru
print(sopru,"igaüks peab maksma",summa,"€")

#toote hind

hind = 36.75
soodus = 0.4
kogus = 3

summa = (hind-(hind*soodus))*kogus
print(kogus,"toote hind on",summa,"€")

#kolmnurga ümbermõõt

a = int(input("Sisestage külje a pikkus: "))
b = int(input("Sisestage külje b pikkus: "))
c = int(input("Sisestage külje c pikkus: "))
P = a + b + c
print("Vastus: kolmnurga ümbermõõt on ", str(P)+"cm⌃2")

