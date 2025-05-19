from persona import persona
from datetime import datetime


class receptor(persona):


    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, partido, provincia, organo_necesario,estado,fecha_de_ingreso,prioridad,patologia):
      super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, partido, provincia)


      self.organo_necesario=organo_necesario# estos son los atributos propios de receptor
      self.estado=estado
      self.fecha_de_ingreso=fecha_de_ingreso
      self.prioridad=prioridad
      self.patologia=patologia

    def __str__(self):
      return f"{self.nombre}. Organo: {self.organo_necesario}, Prioridad: {self.prioridad}"