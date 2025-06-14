from src.Personas.paciente import Paciente
from src.Modelos.organo import Organo
from datetime import datetime



class Receptor(Paciente):


    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre,
                 centro_de_salud, organo_necesario, estado, fecha_de_ingreso, prioridad, patologia):
        
        estado_normalizado = estado.capitalize()
        if estado_normalizado not in ["Estable", "Inestable"]:
            raise ValueError("El estado debe ser 'Estable' o 'Inestable'.")

        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)

        self.__organo_necesario: Organo = organo_necesario
        self.__estado = estado_normalizado
        self.__fecha_de_ingreso = fecha_de_ingreso
        self.prioridad = prioridad
        self.__patologia = patologia
        self.__recibioOrgano = False

    def get_Estado(self):
        """
    Devuelve el estado actual del receptor.

    Returns:
        str: "Estable" o "Inestable"
    """
        return self.__estado

    def get_Fecha_de_ingreso(self):
        """
    Devuelve la fecha en la que el receptor fue ingresado a la lista de espera.

    Returns:
        datetime: Fecha de ingreso.
    """
        return self.__fecha_de_ingreso

    def get_Prioridad(self):
        """
    Devuelve la prioridad del receptor en la lista de espera.

    Returns:
        int: Valor entero de prioridad (mayor número, mayor urgencia).
    """
        return self.prioridad#lo dejamos publico por que el objeto receptor esta contenido en una lista y si no salta error

    def get_Patologia(self):
        """
    Devuelve la patología que presenta el receptor.

    Returns:
        str: Descripción de la patología.
    """
        return self.__patologia

    def get_RecibioOrgano(self):
        """
    Indica si el receptor ya recibió un órgano.

    Returns:
        bool: True si ya recibió un órgano, False si no.
    """
        return self.__recibioOrgano

    def get_Organonecesario(self):
        return self.__organo_necesario

    def set_estado(self, nuevo_estado):
        """
    Cambia el estado de salud del receptor.

    Args:
        nuevo_estado (str): Debe ser "Estable" o "Inestable".

    Raises:
        ValueError: Si el estado no es válido.
    """
        nuevo_estado = nuevo_estado.capitalize()
        if nuevo_estado not in ["Estable", "Inestable"]:
            raise ValueError("El estado debe ser 'Estable' o 'Inestable'.")
        self.__estado = nuevo_estado

    def __str__(self):
        """
    Devuelve una representación legible del receptor.

    Returns:
        str: Información relevante sobre el receptor.
    """
        return (f"Receptor: {self.get_Nombre()}, DNI:{self.get_DNI()}, Necesita: {self.__organo_necesario}, "
                f"Prioridad: {self.prioridad}, Estado: {self.__estado}")

    def __lt__(self, otro):
        """
    Permite comparar dos receptores según su prioridad y fecha de ingreso.

    Args:
        otro (Receptor): Otro objeto Receptor.

    Returns:
        bool: True si este receptor tiene menor prioridad o fue ingresado antes,
              False en caso contrario.
    """
        if self.prioridad != otro.get_Prioridad():
            return self.prioridad < otro.get_Prioridad()
        return self.__fecha_de_ingreso < otro.get_Fecha_de_ingreso()
