import random
# vraag hoeveel personen er zijn
aantal = int(input("Hoeveel personen zijn er?: "))
# maak een lijst om de namen op te slaan
namenLijst = []
# voor iedere persoon de naam vragen
for x in range(1, aantal + 1):
    print(x)  
    # vraag de naam
    naam = input("Voer je naam in ")
    # voeg de naam toe aan de lijst
    namenLijst.append(naam)
# kies een random persoon uit de lijst
randomPersoon = random.choice(namenLijst)
# zet de naam van de persoon die mag starten op het scherm
print(randomPersoon + " mag beginnen") 
