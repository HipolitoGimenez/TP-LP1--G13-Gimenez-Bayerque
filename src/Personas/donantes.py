from src.Personas.paciente import Paciente
from datetime import datetime

class Donante(Paciente):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, fecha_de_muerte, fecha_hora_ablacion):
   
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.fecha_de_muerte=fecha_de_muerte
        self.fecha_hora_ablacion= fecha_hora_ablacion
        self.lista_organos=[]

    def tieneOrgano(self, organo):
        """
        Verifica si el donante tiene un órgano específico en su lista.

        Args:
            organo (Organo): El órgano a verificar.

        Returns:
            bool: True si el órgano está en la lista, False en caso contrario.
        """
        for organo in self.lista_organos:
            organo.tipo == organo.tipo
            return True
        return False


    def __str__ (self):
        """
        Devuelve una representación legible del donante.

        Returns:
            str: Cadena con el nombre, DNI y la fecha desde que es donante.
        """
        return f"{super().__str__}, Donante desde: {self.fecha_de_muerte}"
    
    def quitarOrgano(self, organo):
        """
        Elimina un órgano específico de la lista de órganos del donante.

        Args:
            organo (Organo): Órgano a eliminar de la lista.
        """
        self.lista_organos.remove(organo)
    
    
       

   

    

    



   

    

    

