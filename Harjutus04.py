#Ülesanne04
#Virgo Lootus
#03.02.2022

#korrutustabel




'''
for p in range(1,101):
    

    jaak = p%int(2)    

    if jaak == 0:
            print (p,"paaris arv")
    else:
            print (p,"paaritu arv")



#loto
import random

for e in range(1,6):
    a = int(random.randint(0,9))
    print (a,end="")



#tärnid

for e in range(1,6):
    for a in range(1,6):
        print ("* ",end="")
    print()
print ("-"*10)

for e in range(1,6):
    print(e*"* ")
print ("-"*10)

k = 5
for e in range(1,k+1):
    print(k*"* ")
    k = k - 1



#jalgpalli meeskond

sugu = input("sisestage oma sugu: ")

if sugu=="mees":
    vanus = int(input("sisestage oma vanus: "))
    if vanus >= 16 and vanus <=18:
        print("sobid meeskonda")
    else:
        print("ei ole sobilik")
else:
    ()


#müük

hind = int(input("sisestage toote hind: "))

if hind<10:
    ale = 0.1
else:
    ale = 0.2
vastus = hind-(hind*ale)
print (vastus)


#juubel

sp = input("sisestage oma sünnipäev kujul pp.kk.aaaa: ")
a=2022
pp, kk, aaaa = sp.split(".")

vanus = a - int(aaaa)
jaak = vanus % 5

if jaak==0:
    print("juubel")
else:
    print("ei ole juubel")


#matemaatika

arv1 = int(input("sisestage arv1: "))
arv2 = int(input("sisestage arv2: "))
tehe = input("sisestage tehe * / + -: ")

if tehe == "+":
    vastus = arv1 + arv2
elif tehe == "-":
     vastus = arv1 - arv2
elif tehe == "*":
     vastus = arv1 * arv2
else:
     vastus = arv1 / arv2

print(f"{arv1}{tehe}{arv2}={vastus}")

#ruut

a = int(input("esimese külje pikkus: "))
b = int(input("teise külje pikkus: "))
        
if a==b:
    print("ruut")
else:
    print("ristkülik")
'''