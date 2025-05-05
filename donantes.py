from persona import persona
from organo import organo
class donantes(persona):

    def __init__(self, fecha_de_muerte, lista_de_organos:list[organo]):

        self.fecha_de_muerte=fecha_de_muerte
        self.lista_organos =lista_de_organos