
#3.4
fail = input("Palun sisestage faili nimi: ")
fail = open(fail,encoding="UTF-8")
number = 1
for i in fail:
    print(number". ", i,end="")
    number+=1


#3.3
fail = open("konto.txt", encoding="UTF-8")
for rida in fail:
    if float(rida) > 0:
        print(rida,end="")
    print(rida)
#3.2

ringid = int(input("sisestage ringide arv: "))
porgand = 0
for i in range(1,ringid+1):
    if i%2==0:
        porgand +=i
print(f"saadavate porganite koguarv on {porgand}")
#3.1
fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in fail:
    vastuvoetud.append(int(rida))
aasta = input("Sisestage, milline aasta andmeid vajad: ")
print(f"{aasta}. aastal oli vastuvõetud{vastuvoetud} [int(aasta[3])-1]")

#2.5
import random
vmees = int(input("Mitu tahavad õuna: "))
lumi = 14
for a in range(vmees):
    oun = random.randint(1,2)
    print(oun)
    lumi = lumi - oun
print(f"Lumivalgekesele jäi {lumi}")

#2.4

arv = int(input("sisestage täisarv: "))
nisuterad = 1

i = 1
while i <= arv:
    
    nisuterad *= 2
    i += 1
print(f"nisuteri on {nisuterad}. ruudu eest: {arv} ")

#2.3

import random
taringud = int(input("Sisestage täringute arv"))

for a in range(taringud):
    print(random.randint(1,6))
#2.2

ringid = int(input("sisestage ringide arv: "))

i = 1
porgandid = 0
while i < ringid:
    if i%2 == 0:
        porgandid+=i
    i += 1
print(f"porgandeid on {porgandid} ja ringe on {ringid}")


#2.1

korrad = int(input("mitu korda peaks äratama: "))

for a in range(korrad):
    print("Tõuse ja sära")
#1.4
def bussid():
    inimesed = int(input("Sisesta inimeste arv: "))
    istekohad = int(input("Sisesta bussi kohtade arv: "))
    viimane = inimesed%istekohad
    if viimane == 0:
        bussid = inimesed//istekohad
        viimane = istekohad
    else:
        bussid = inimesed//istekohad+1
    print(f"Busse vaja: {bussid}\nViimases bussis inimesi: {viimane}")

bussid()

#1.2
def liblikas():
    aasta = 2020
    liblikas = "teelehe-mosaiikliblikas"
    lause_keskosa = ". aasta liblikas on"
    lause = str(aasta)+lause_keskosa+liblikas
    print(lause)
liblikas()
#1.1

def tere():
    print("Tere, maailm!")
tere()

