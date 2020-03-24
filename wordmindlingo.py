import random

# in deze functie vraagt hij om een naam en roept de functie bergroet aan.
def hoe_heet_je():
    naam = input("Hoe heet je: ")
    begroet(naam)
    return(naam)


# hier maakt hij de code aan.
def code_maken(lengte_geheimwoord):
    code = lengte_geheimwoord * "-"
    print(code)
    return(code)
    
#dit is de belangrijkste code want hier worden ook de andere functies aangeroepen. Verder test hij of de woorden wel vergeleken
#mogen worden door de lengte te testem
def wordmind(geheimwoord, lengte_geheimwoord, code):
    geradenwoord = input("Geef een woord van " + str(lengte_geheimwoord) + " letters: ")
    lengte_geradenwoord = len(geradenwoord)
    while geradenwoord != geheimwoord:
        if lengte_geradenwoord == lengte_geheimwoord:
            code = vraagteken_weg(lengte_geheimwoord, code)                            
            code = vergelijk(lengte_geheimwoord, geheimwoord, geradenwoord, code)
        elif lengte_geradenwoord < lengte_geheimwoord:
            print("Sorry het woord dat jij hebt geraden was korter dan " + str(lengte_geheimwoord) + " letters")
        elif lengte_geradenwoord > lengte_geheimwoord:
            print("Sorry het woord dat jij hebt geraden was langer dan " + str(lengte_geheimwoord) + " letters")
        print(" ")
        print(code)
        print(" ")
        geradenwoord = input("Geef een woord van " + str(lengte_geheimwoord) + " letters: ")
        lengte_geradenwoord = len(geradenwoord)
    print("Je hebt het goed geraden.")
    print(geheimwoord)


# de functie vergelijk vergelijkt de 2 woorden met elkaar en zet vraagtekens en letters op de plekken waar ze moeten staan.
def vergelijk(lengte_geheimwoord, geheimwoord, geradenwoord, code):
    for t in range(lengte_geheimwoord):
        if str(geheimwoord)[t] == str(geradenwoord)[t]:
            lijst_code = list(code)
            lijst_code[t] = geradenwoord[t]
            code = ''.join(lijst_code)
        elif str(geradenwoord)[t] in str(geheimwoord):
            lijst_code = list(code)
            lijst_code[t] = "?"
            code = ''.join(lijst_code)
    return(code)

# de functie vraagteken_weg haalt de vraagtekens weg die nog in de code staan zodat de code alleen streepjes en letters laat zien.
def vraagteken_weg(lengte_geheimwoord, code):
    for i in range(lengte_geheimwoord ):
        if code[i] == "?":
            lijst_code = list(code)
            lijst_code[i] = "-"
            code = ''.join(lijst_code)
    return(code)
            
# de functie begroet bergroet de speler aan het begin en geeft het een uitleg over het spel.
def begroet(naam):
    print ("Hallo " + naam + " we gaan het spelletje wordmind spelen. het werkt zo:")
    print ("Geef een woord aan de computer.")
    print ("Als er een streepje staat komt die letter er niet in voor.")
    print ("Als er een letter komt te staan dan heb je de goede letter geraden.")
    print ("Als er een vraagteken komt te staan dan zit de letter er wel in maar staat hij niet op de juiste plek.")

#Hier gebereurt alles en in deze functie worden ook weer functies aangeroepen.
def main():
    woorden = ["banaan", "fakkel", "paneel", "kungfu", "walvis", "onweer", "balpen", "ganzen", "toffee", "varken", "vis", "vliegtuig", "kat", "vogel", "boek", "stift"]
    geheimwoord = random.choice(woorden)
    lengte_geheimwoord = len(geheimwoord)
    naam = hoe_heet_je()
    code = code_maken(lengte_geheimwoord)
    wordmind(geheimwoord, lengte_geheimwoord, code)

main()