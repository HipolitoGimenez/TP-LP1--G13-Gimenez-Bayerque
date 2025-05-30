from src.Personas.paciente import Paciente
from src.Modelos.organo import Organo
from datetime import datetime

class Donante(Paciente):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, fecha_de_muerte, fecha_hora_ablacion):
   
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)

        self.fecha_de_muerte=fecha_de_muerte
        self.fecha_hora_ablacion= None
        self.lista_organos=[]
    
    def get_Fecha_de_muerte(self):
        """
        Obtiene la fecha de muerte del donante.

        Returns:
        datetime: Fecha en que ocurrió el fallecimiento del donante.
        """
        return self.__fecha_de_muerte
    
    def get_Fecha_hora_ablacion(self):
        """
        Obtiene la fecha y hora de la ablación.

        Returns:
        datetime: Fecha y hora en que se realizó la ablación de órganos.
        """
        return self.__fecha_hora_ablacion
    
    def get_Lista_organos(self):
        """
        Obtiene la lista de órganos disponibles del donante.

        Returns:
        list: Lista de objetos órgano disponibles para trasplante.
        """
        return self.__lista_organos


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
    
    def cargarOrgano(self, organo: Organo):
        """
        Agrega un órgano a la lista de órganos del donante.

        Args:
        organo (Organo): Objeto órgano que será añadido al donante.
        """
        self.__lista_organos.append(organo)

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
    
    
       

   

    

    



   

    

    

