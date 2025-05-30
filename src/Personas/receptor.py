from src.Personas.paciente import Paciente
from src.Modelos.organo import Organo
from datetime import datetime


class Receptor(Paciente):


  def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia):
    """
        Inicializa un objeto Receptor con atributos heredados de Paciente y propios de un receptor.

        Args:
            nombre (str): Nombre completo del receptor.
            DNI (str o int): Documento Nacional de Identidad.
            fecha_de_nacimiento (str): Fecha de nacimiento.
            sexo (str): Sexo.
            telefono (str): Teléfono de contacto.
            tipo_de_sangre (str): Tipo de sangre.
            centro_de_salud (CentroDeSalud): Centro de salud asociado.
            organo_necesario (str): Tipo de órgano que necesita.
            estado (str): Estado del receptor (Ej: estable, inestable).
            fecha_de_ingreso (datetime): Fecha de ingreso a la lista de espera.
            prioridad (int): Prioridad en la lista de espera.
            patologia (str): Patología del receptor.

        Returns:
            None
        """
    super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
    self.organo_necesario: Organo=organo_necesario
    self.estado=estado
    self.fecha_de_ingreso=fecha_de_ingreso
    self.prioridad=prioridad
    self.patologia=patologia
    self.recibioOrgano=False
  def get_Estado(self):
     """
    Devuelve el estado clínico del receptor (por ejemplo: Estable o Inestable).

    Returns:
        str: Estado del receptor.
    """
     return self.__estado
  
  def get_Fecha_de_ingreso(self):
     """
    Devuelve la fecha en la que el receptor ingresó a la lista de espera.

    Returns:
        datetime: Fecha de ingreso a la lista de espera.
    """
     return self.__fecha_de_ingreso
  
  def get_Prioridad(self):
     """
    Devuelve el nivel de prioridad asignado al receptor.

    Returns:
        int: Prioridad del receptor (menor número indica mayor prioridad).
    """
     return self.__prioridad
  
  def get_Patologia(self):
     """
    Devuelve la patología por la cual el receptor necesita un trasplante.

    Returns:
        str: Nombre de la patología.
    """
     return self.__patologia
  
  def get_RecibioOrgano(self):
     """
    Indica si el receptor ya recibió un órgano o no.

    Returns:
        bool: True si recibió un órgano, False en caso contrario.
    """
     return self.__recibioOrgano

  def __str__ (self):
    """
        Devuelve una cadena legible con los datos principales del receptor, incluyendo órgano necesario y prioridad.

        Returns:
            str: Representación del receptor.
        """
    return f"{super().__str__}, Necesita: {self.organo_necesario}, Prioridad: {self.prioridad}"

  
  def __lt__(self, otro):
        """
        Permite comparar dos receptores usando el operador < basado en prioridad y fecha de ingreso.

        Args:
            otro (Receptor): Otro objeto receptor para comparar.

        Returns:
            bool: True si self tiene menor prioridad (número más bajo) o, en caso de empate, ingreso más antiguo.
        """
        if self.prioridad != otro.prioridad:
            return self.prioridad < otro.prioridad
        return self.fecha_de_ingreso < otro.fecha_de_ingreso

