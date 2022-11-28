from datetime import date
date.today
geboorte = input(int("Voer je geboortedatum in: "))
if geboorte > date.today() : print("mag rijden")
else: print("mag niet rijden")