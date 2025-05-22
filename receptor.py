from persona import Persona
from datetime import datetime


class Receptor(Persona):


    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, partido, provincia, organo_necesario,estado,fecha_de_ingreso,prioridad,patologia):
      super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, partido, provincia)


      self.organo_necesario=organo_necesario# estos son los atributos propios de receptor
      self.estado=estado
      self.fecha_de_ingreso=fecha_de_ingreso
      self.prioridad=prioridad
      self.patologia=patologia
      self.organos=[]

    def __str__ (self):
      return f"{super().__str__}, Necesita: {self.organo_necesario}, Prioridad: {self.prioridad}"
    
    # Metodo magico para ordenar por prioridad (it es less than)
    def __lt__ (self,otro):
       if self.prioridad != otro.prioridad:
          return self.prioridad < otro.prioridad
       return self.fecha_de_ingreso < otro.fecha_ingreso


