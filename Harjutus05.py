#Harjutus 5
#Virgo Lootus
#10.02.2022

'''
#tärnid
import random

arvud = []
for a in range(5):
    arvud.append(random.randint(1,99))
print(arvud)
for a in range(len(arvud)):
    print("*"*arvud[a])


#vanused
import random

vanused = []
for a in range(5):
    vanused.append(random.randint(1,99))

print(vanused)
print(min(vanused),max(vanused))
print(sum(vanused)/len(vanused))


#duplikaadid

opilased = ['Juhan','Kati','Mario','Mario','Mati']
opilased = sorted(set(opilased))
print(opilased)


#õpilased
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
print("vali number, mis soovid muuta: ")
for a in range (len(opilased)):
    print(f"{a+1}. {opilased[a]}")
valik = int(input("sisestage number: "))
del opilased[valik-1]
u_nimi = input("sisestage uus nimi: ")
opilased.insert(valik-1,u_nimi)
print("Nimi uuendatud")
print(opilased)


#nimede lisamine

nimed = []

for a in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)
nimed.sort()
print (nimed)
'''