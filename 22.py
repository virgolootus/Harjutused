#4.6
kuup = "08.03.2022"
def kuu_nimi(a):
    ekkuud = ["","jaanuar","veebruar","märts"]
    return ekkuud[a]
       
def kuupaev_sonana(a):
    k,p,aa = a.split(".")
    kp = (f"{k}. {kuu_nimi(int(p))} {aa}")
    return kp
print(kuupaev_sonana(kuup))


#4.5
def pronks():
    konto = 0
    for a in open("mündid.txt"):
        if int(a) <= 5:
            konto += int(a)
    print(konto)
pronks()
#4.4
arv = int(input("Sisesta külaliste arv: "))
def tervitus(a):
    
    for i in range(a):
        print('Võõrustaja: "Tere!"')
        print(f'Täna {i+1}. kord tervitada, mõtiskleb võõrustaja')
        print('Külaline: "Suur tänu kutse eest!"')
tervitus(arv)
#4.3
def eelarve(i):
    inimesed = 10 * i + 55
    return inimesed
g = int(input("Mitu inimest on kutsutud: "))
t = int(input("Mitu inimest ei tule: "))
print('max_eelarve: ' ,eelarve(g))
print('min_eelarve: ' ,eelarve(t)) 
#4.2
kogus = int(input("Sisestage õunad kilodes: "))
def mahlapakkide_arv(x):
    kogus = x*0.4/3
    return round(kogus)
print(mahlapakkide_arv(kogus))
#4.1
def banner(a):
    l = a.upper()
    return l 
h = int(input("kordade arv: "))
for i in range(h):
    print(banner("osta noonesid"))

#3.5
fail = open("nimekiri.txt")
n = 1
for i in fail:
    if n == datetime.now().day:
        print(i)
    n += 1
#3.4
fail = input("Palun sisestage faili nimi: ")
fail = open(fail,encoding="UTF-8")
number = 0
for i in fail:
    number+=1
    print(str(number)+". " +str(i),end="")
print("\n")

    

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

def tervitus():
    
    print("Tere, maailm!")
    
tervitus()