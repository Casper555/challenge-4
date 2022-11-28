from datetime import date
date.year
geboorte = input("Voer je geboortedatum in: ")
if geboorte > date.today() : print("mag rijden")
else: print("mag niet rijden")