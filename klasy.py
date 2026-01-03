#klasa = szablon, przepis

class Czlowiek:
    # istota
    gatunek = "Homo sapiens"
    def __init__(self):
        # istnienie
        # specyficzna metoda bo to jest konstruktor
        print("Niech powstanie czlowiek")

#powstanie obiektu
#gotowanie z przepisu
adam = Czlowiek() # a = 4 # a = int(4)
print(adam.gatunek)
