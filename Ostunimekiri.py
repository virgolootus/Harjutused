#Nimekiri
#Virgo Lootus
#02.03.2022

def nimekiri():    
    #massiiv
    ostu_nimekiri = []

    #annab kasutajale juhised
    print("Lisa vajalikud tooted nimekirja")
    print("Vajuta tühjalt ENTER, kui nimekiri on valmis")

    #tsükkel mis lisab tooteid massiivi
    while True:
        #küsib, mis tooteid lisada    
        toode = input("- ")

        #toodete lisamisest väljumine    
        if toode == "":
            break
        #lisab tooted nimekirja
        ostu_nimekiri.append(toode)

    print("Siin on teie nimekiri:")

    #tsükkel mis kirjutab massiivist ükshaaval tooted nimekirja
    for asi in ostu_nimekiri:
         print(asi)
nimekiri()
