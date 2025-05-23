from donantes import Donante
from receptor import Receptor
from organo import Organo

#es dudosa esta clase voy a intentar que sea un metodo y la evito
class Coincidencia():
    def __init__(self,receptor,donante,organo):#esta clase solo almacenaria la coincidencia la lista la tengo en el Incucai
        self.receptor=receptor
        self.donante=donante
        self.organo=organo 