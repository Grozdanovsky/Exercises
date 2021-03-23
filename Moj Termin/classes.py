
class Lekar:
    def __init__(self,maticen,ime,prezime,plata):
        self.maticen = maticen
        self.ime = ime
        self.prezime = prezime
        self.plata = plata


    def __str__(self):
        return self.maticen,self.ime,self.prezime,self.plata

    def pecati(self):
        print(f"Ime: {self.ime}\nPrezime: {self.prezime}")

    def get_plata(self):
        return self.plata

    

class MaticenLekar(Lekar):
    def __init__(self,maticen,ime,prezime,plata,br_pacietni,kotizacii):
        Lekar.__init__(self,maticen,ime,prezime,plata)
        self.br_pacienti = br_pacietni
        self.kotizacii = kotizacii

    def pecati(self):
        Lekar.pecati(self)


    def get_plata(self):
        return self.plata


    def prosek_kotizacii(self):
        suma = 0
        prosek = 0
        for kotizacija in self.kotizacii:
            suma += kotizacija

        prosek = suma / len(self.kotizacii)
        prosek += (prosek * 0.30)
        self.plata = self.plata + (prosek * 0.30)

