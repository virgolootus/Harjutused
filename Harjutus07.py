#Harjutus07
#Virgo Lootus
#15.02.2022
import math

#ruumala
def kuup(a):
    v = a ** 3
    return v

def kera(r):
    v = round(4/3*math.pi*r**3,2)
    return v
    
def koonus(r,h):
    v = round(1/3*math.pi*r**2*h,2)
    return v

def silinder(r,h):
    v = round(math.pi*r**2*h,2)
    return v


print("********** LEIAME RUUMALA ***********")
print("Vali kujund:\n1 Kuup\n2 Kera\n3 Koonus\n4 Silinder")
valik = int(input("Vali soovitud kujundi number: "))
if valik == 1:
    print("----------\nValisid kuubi ruumala arvutamise")
    a = int(input("Sisestage kuubi külje pikkus a="))
    print(kuup(a))
elif valik == 2:
    print("----------\nValisid kera ruumala arvutamise")
    r = int(input("Sisestage kera raadius r="))
    print(kera(r))
elif valik == 3:
    print("-----------\nValisid koonuse ruumala arvutamise")
    r = int(input("Sisestage koonuse põhja raadius r="))
    h = int(input("Sisestage koonuse kõrgus h="))
    print(koonus(r,h))
else:
    print("-----------\nValisid silindri ruumala arvutamise")
    r = int(input("Sisestage silindri põhja raadius r="))
    h = int(input("Sisestage silindri kõrgus h="))
    print(silinder(r,h))

#tervitus
def tervita(nimi, keel="de"):
    if keel == "et":
        print(f"Tere {nimi}!")
    elif keel == "en":
        print(f"Hi {nimi}!")
    else:
        print(f"Hallo {nimi}")
    
n = input("sisestage nimi: ")
k = input("vali keel et/en/de: ")
tervita(n,k)