from src.Personas.donantes import Donante
from src.Personas.receptor import Receptor
from src.Modelos.organo import Organo
class Coincidencia():
    def __init__(self,receptor,donante,organo):#esta clase solo almacenaria la coincidencia la lista la tengo en el Incucai
        self.receptor=receptor
        self.donante=donante
        self.organo=organo 