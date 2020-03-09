import random

woorden = ["banaan", "fakkel", "paneel", "kungfu", "walvis", "onweer", "balpen", "ganzen", "toffee", "varken", "vis", "vliegtuig", "kat", "vogel", "boek", "stift"]
geheimwoord = random.choice(woorden)
lengtegeheimwoord = len(geheimwoord)


# in deze functie vraagt hij om een naam en roept de functie bergroet aan.
def hoeheetje(begroet):
    naam = input("Hoe heet je: ")
    bergroet(naam)
    return(naam)


# hier maakt hij de code aan.
def codemaken(lengtegeheimwoord):
    code = lengtegeheimwoord * "-"
    print(code)
    return(code)

#dit is de belangrijkste code want hier worden ook de andere functies aangeroepen. Verder test hij of de woorden wel vergeleken
#mogen worden door de lengte te testem
def wordmind(geradenwoord, geheimwoord, lengtegeradenwoord, lengtegeheimwoord, code, vergelijk, vraagtekenweg):
    while geradenwoord != geheimwoord:
        if lengtegeradenwoord == lengtegeheimwoord:
            code = vraagtekenweg(lengtegeheimwoord, code)
            code = vergelijk(lengtegeheimwoord, geheimwoord, geradenwoord, code)
        elif lengtegeradenwoord < lengtegeheimwoord:
            print("Sorry het woord dat jij hebt geraden was korter dan " + str(lengtegeheimwoord) + " letters")
        elif lengtegeradenwoord > lengtegeheimwoord:
            print("Sorry het woord dat jij hebt geraden was langer dan " + str(lengtegeheimwoord) + " letters")
        print(" ")
        print(code)
        print(" ")
        geradenwoord = input("Geef een woord: ")
        lengtegeradenwoord = len(geradenwoord)
    print("Je hebt het goed geraden.")
    print(geheimwoord)


# de functie vergelijk vergelijkt de 2 woorden met elkaar en zet vraagtekens en letters op de plekken waar ze moeten staan.
def vergelijk(lengtegeheimwoord, geheimwoord, geradewoord, code):
    for t in range(lengtegeheimwoord):
        if geheimwoord[t] == geradewoord[t]:
            lijstcode = list(code)
            lijstcode[t] = geradewoord[t]
            code = ''.join(lijstcode)
        elif geradewoord[t] in geheimwoord:
            lijstcode = list(code)
            lijstcode[t] = "?"
            code = ''.join(lijstcode)
    return(code)

# de functie vraagtekenweg haalt de vraagtekens weg die nog in de code staan zodat de code alleen streepjes en letters laat zien.
def vraagtekenweg(lengtegeheimwoord, code):
    for i in range(lengtegeheimwoord ):
        if code[i] == "?":
            lijstcode = list(code)
            lijstcode[i] = "-"
            code = ''.join(lijstcode)
    return(code)

# de functie begroet bergroet de speler aan het begin en geeft het een uitleg over het spel.
def bergroet(naam):
    print ("Hallo " + naam + " we gaan het spelletje wordmind spelen. het werkt zo:")
    print ("Geef een woord aan de computer.")
    print ("Als er een streepje staat komt die letter er niet in voor.")
    print ("Als er een letter komt te staan dan heb je de goede letter geraden.")
    print ("Als er een vraagteken komt te staan dan zit de letter er wel in maar staat hij niet op de juiste plek.")

#Hier gebereurt alles en in deze functie worden ook weer functies aangeroepen.
def main(geheimwoord, lengtegeheimwoord):
    naam = hoeheetje(bergroet)
    code = codemaken(lengtegeheimwoord)
    geradenwoord = input("Geef een woord van " + str(lengtegeheimwoord) + " letters: ")
    lengtegeradenwoord = len(geradenwoord)
    wordmind(geradenwoord, geheimwoord, lengtegeradenwoord, lengtegeheimwoord, code, vergelijk, vraagtekenweg)

main(geheimwoord, lengtegeheimwoord)
