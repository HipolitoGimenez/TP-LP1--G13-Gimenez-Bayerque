from persona import persona
from datetime import datetime


class receptor(persona):

  def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia):
    super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)

    self.organo_necesario=organo_necesario
    self.estado=estado
    self.fecha_de_ingreso=fecha_de_ingreso
    self.prioridad=prioridad
    self.patologia=patologia

def __str__ (self):
  return f"{super().__str__}, Organo: {self.organo_necesario}"
