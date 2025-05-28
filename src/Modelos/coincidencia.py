from src.Personas.donantes import Donante
from src.Personas.receptor import Receptor
from src.Modelos.organo import Organo
class Coincidencia():
    def __init__(self,receptor,donante,organo):
        """
        Recibe: 
            - receptor: un objeto de tipo Receptor
            - donante: un objeto de tipo Donante
            - organo: un objeto de tipo Organo
        Hace: 
            - Inicializa una instancia de Coincidencia que representa un match entre un receptor, 
              un donante y un órgano compatible.
        Devuelve: 
            - Nada explícitamente. Crea el objeto Coincidencia con sus atributos asociados.
        
        Nota: Esta clase solo sirve como contenedor de la coincidencia. La lista que almacena estos 
              objetos se maneja dentro de la clase INCUCAI.
        """
        self.receptor=receptor
        self.donante=donante
        self.organo=organo 