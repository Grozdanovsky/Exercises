from classes import *


l1 = Lekar(22222,"Stefan","Cvetanovski",20000,)

m1 = MaticenLekar(123321,"Viktor","Grozdanovski",15600,10,[100,200,300,400,500,600,700,800,900,1000])


l1.pecati()
print(l1.get_plata())
m1.pecati()
print(m1.get_plata())
m1.prosek_kotizacii()
print(m1.get_plata())