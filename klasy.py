#klasa = szablon, przepis

class Czlowiek:
    # istota
    # atrybut klasy
    gatunek = "Homo sapiens"
    def __init__(self, imie, plec):
        # istnienie
        # specyficzna metoda bo to jest konstruktor
        print(f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie
        self.plec = plec

#powstanie obiektu
#gotowanie z przepisu
#adam = Czlowiek("Adam") # a = 4 # a = int(4)
#ewa = Czlowiek("Ewa")


#metoda
#moznosc, mozliwosc, zdolnosc, umiejetnosc
    def przedstaw_sie(self):
        print(f"Dzien dobry, mam na imie {self.imie} i jestem ", end="")
        if self.plec=="M":
            print("mezczyzna")
        else:
            print("kobieta")

    def przedstaw(self, osoba):
        print(f"Oto {osoba.imie}")

#powstanie obiektu
adam = Czlowiek("Adam", "M")
ewa = Czlowiek("Ewa", "K")

ewa.przedstaw_sie()
ewa.przedstaw(adam)