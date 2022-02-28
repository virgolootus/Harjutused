#Harjutus09
#Virgo Lootus
#16.02.2022

import datetime
from datetime import date

#Isikukood
ik = "50412031111"
aasta = int("20" + ik[1] + ik[2])
kuu = int(ik[3] + ik[4])
paev = int(ik[5] + ik[6])
tana = date.today()
kuup = datetime.date(aasta, kuu, paev)
paevad = tana - kuup
print(paevad/365)
print(kuup)




#Eesti kuup

kuup = date.today()
p1 = kuup.strftime("%d.  Märts  %Y")  #:D
print(p1)


#Tänane kuupäev

kuup = date.today()
p1 = kuup.strftime("%d. %B %Y")
print(p1)
