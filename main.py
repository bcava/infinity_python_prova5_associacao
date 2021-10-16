
from PrefeituraSalvador import PrefeituraSalvador
from Prefeito import Prefeito
from Burger import Burger
from Croissant import Croissant


pref1 = Prefeito ("hghf", "7667546", "hgfcxxzw")



emp1 = Burger ("x", "65665", "10", 2000000)
emp2 = Croissant ("y", "979785675", "15", 3000000)



empresas = [emp1, emp2]


prefeitura1 = PrefeituraSalvador ("Salvador", pref1, empresas)



print (prefeitura1.total())