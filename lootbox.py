import random
kans = random.randint(1, 200)
if kans >=1 and kans <= 5:print("legendary")
elif kans >= 6 and kans <= 20: print("epic")
elif kans >= 21 and kans <= 50: print("rare")
elif kans >= 51 and kans <= 120: print("uncommon")
elif kans >= 121 and kans <= 200: print("common")