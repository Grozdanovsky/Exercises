
class ZicanInstrument:

    def __init__(self,ime,broj,cena):
        self.ime = ime
        self.broj = broj
        self.cena = cena

    def __str__(self):
        return self.ime,self.cena,self.broj

class Mandolina(ZicanInstrument):
    def __init__(self,ime,broj,cena,forma):
        ZicanInstrument.__init__(self,ime,broj,cena)
        self.forma = forma

    def return_price(self):
        if self.forma == "Neapolitan":
            self.cena += (self.cena * 0.15)

    def printaj_mandolina(self):
        print(self.ime,self.broj,self.cena,self.forma)


    def return_strings(self):
        return self.broj



class Violina(ZicanInstrument):
    def __init__(self,ime,broj,cena,golemina):
        ZicanInstrument.__init__(self,ime,broj,cena)
        self.golemina = golemina

    def retrun_price(self):
        if self.golemina == 0.25:
            self.cena += (self.cena * 0.10)

        elif self.golemina == 1:
            self.cena += (self.cena * 0.20)


    def printaj_violina(self):
        print(self.ime,self.broj,self.cena,self.golemina)