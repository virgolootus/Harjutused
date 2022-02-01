#Harjutus 3
#Virgo Lootus
#01.02.2022
'''
#palindroom

sisestus = input("sisestage palindroom: ")
print(sisestus == sisestus[::-1])

#tudide aeg
aeg1 = input("algusaeg: ")
aeg2 = input("loppaeg: ")
hh1, mm1 = aeg1.split(":")
hh2, mm2 = aeg2.split(":")
vastus = (int(hh2)*60+int(mm2)) - (int(hh1)*60+int(mm1))
tund = vastus//60
minut = vastus%60
print("õpilase päev 10kestab {}:{}".format(tund,minut))


#email
email = input("sisestage oma email: ")
print("@" in email)


#Vandmuine

s = (input("ara utle kurat: "))
s = s.lower()
v = s.replace("kurat","*****")
print(v)
'''

#Korralik nimi

nimi = input("sisestage nimi: ")
puhas = (nimi.strip().capitalize())
print("Tere",puhas)