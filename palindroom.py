def Palindroom(inputwoord):
    return inputwoord == inputwoord[::-1]

woord = input("Voer een woord in: ")
palin = Palindroom(woord)
if palin:
    print("Het is wel een palindroom")
else:
    print("Het is niet een palindroom") 