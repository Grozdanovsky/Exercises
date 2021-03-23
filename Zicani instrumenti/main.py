from classes import *
from functions import *
m1 = Mandolina("Mozzart",4,1000,"Neapolitan")
m2 = Mandolina("Viktor",4,1200,"Barok")
m3 = Mandolina("Cefi",3,1500,"Rokoko")
lista_mandolini = [m1,m2,m3]
m1.return_price()


v1 = Violina("Rene",3,1600,1)
v1.retrun_price()

pecatiInstrumenti(m1,lista_mandolini)