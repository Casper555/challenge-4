while True:

  getal_1 = int(input("Voer het eerste getal in: "))
  operator = input("Voeg een operator toe: ")
  getal_2 = int(input("Voer het tweede getal in: "))

  if operator == "+":
    print("Het antwoord is: " + str(getal_1 + getal_2))
  elif operator == "-":
    print("Het antwoord is: " + str(getal_1 - getal_2))
  elif operator == "*":
    print("Het antwoord is: " + str(getal_1 * getal_2))
  elif operator == "/":
    print("Het antwoord is: " + str(getal_1 / getal_2))
  else:
    print("Ik herken die operator niet, probeer het opnieuw.")