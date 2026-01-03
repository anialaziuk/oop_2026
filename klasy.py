#klasa = szablon, przepis

class Czlowiek:
    # istota
    gatunek = "Homo sapiens"
    def __init__(self, imie):
        # istnienie
        # specyficzna metoda bo to jest konstruktor
        print(f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie

#powstanie obiektu
#gotowanie z przepisu
adam = Czlowiek("Adam") # a = 4 # a = int(4)
ewa = Czlowiek("Ewa")
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)
print(ewa.imie)