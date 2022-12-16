import random
kans = random.randint(1, 200)
if kans >= 1 and kans <= 5:print("Legendary")
elif kans >= 6 and kans <= 20: print("Epic")
elif kans >= 21 and kans <= 50: print("Rare")
elif kans >= 51 and kans <= 120: print("Uncommon")
else: print("Common") 