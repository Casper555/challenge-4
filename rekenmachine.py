while True:

  getal1 = int(input("Voer het eerste getal in: "))
  teken = input("Voeg een teken toe: ")
  getal2 = int(input("Voer het tweede getal in: "))
  uitkomst = input("klik op = en dan enter voor de uitkomst: ")

  if teken == "+":
    print(uitkomst)
  elif teken == "-":
    print(uitkomst)
  elif teken == "*":
    print(uitkomst)
  elif teken == "/":
    print(uitkomst)
  else:
    print("Ik herken het teken niet, probeer het opnieuw.")
  if uitkomst == "=":
    print(getal1 * getal2)