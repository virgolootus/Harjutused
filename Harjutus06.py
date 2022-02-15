#Harjutus06
#Virgo Lootus
#15.02.2022



#tabel
reformikad, kesk, kokku = 0, 0, 0
erakonnad = []

with open("Pol.txt", "r") as poliitikud:
    for rida in poliitikud:
        enimi, pnimi, er, laigid = rida.split(" ") 
        print(f"{enimi:11} {pnimi:11} {er:4} {laigid:5}", end="")
        if er == "reformikad":
            reformikad+=1
        elif er == "kesk":
            kesk+=1
        elif er == :
            append.erakonnad
print("\n---------------")
print(f"reformikad: {reformikad}\nKesikuid: {kesk}")
print(f"erakondi kokku: {len(erakonnad)}")
print(erakonnad)
        