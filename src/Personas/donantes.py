from src.Personas.paciente import Paciente
from src.Modelos.organo import Organo
from datetime import datetime

class Donante(Paciente):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, fecha_de_muerte, fecha_hora_ablacion):
   
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)


        self.__fecha_de_muerte=fecha_de_muerte
        self.__fecha_hora_ablacion = fecha_hora_ablacion
        self.__lista_organos=[]
    
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
        Verifica si el donante posee un órgano del mismo tipo que el proporcionado.

        Args:
        organo (Organo): El órgano a verificar, del cual se evalúa el tipo.

        Returns:
        bool: True si el donante tiene al menos un órgano del mismo tipo en su lista,
              False en caso contrario.

        Detalles:
        - Compara el atributo 'tipo' del órgano proporcionado con los órganos en
          la lista del donante (__lista_organos).
        - No requiere que sea el mismo objeto, solo que coincida el tipo.
        """
        for o in self.__lista_organos:
            if o.tipo == organo.tipo:
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
        return f"Donante: {self.nombre}, Donante DNI:{self.DNI}, Donante desde: {self.__fecha_de_muerte}"
    
    def quitarOrgano(self, organo):
        """
        Elimina un órgano específico de la lista de órganos del donante.

        Args:
            organo (Organo): Órgano a eliminar de la lista.
        """
        if organo not in self.__lista_organos:
            raise ValueError("El órgano no se encuentra en el donante.")
        self.lista_organos.remove(organo)
        
    
    
    
       

   

    

    



   

    

    

