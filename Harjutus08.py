#Harjutus08
#Virgo Lootus
#16.02.2022

#Klass auto

class Auto:
    mark = 'teadmata'
    aasta = 'teadmata'
    hind = 0
    varv = 'teadmata'
    kiirus = 'teadmata'
    
    def __init__(self,x,y,z,a,c):
        self.mark = x
        self.aasta = y
        self.hind = z
        self.varv = a
        self.kiirus = c
    def kuva(self):
        print(f"Mark: {self.mark} \nAasta: {self.aasta} \nHind: {self.hind} \nVarv: {self.varv} \nKiirus: {self.kiirus}")

uusObjekt = Auto("Audi", 2004, 600, "Pruun", "160km/h")
uusObjekt.kuva()
print("----------")
MinuAuto = Auto("Mersu",2020,20000,"Valge","220km/h")
MinuAuto.kuva()
    
