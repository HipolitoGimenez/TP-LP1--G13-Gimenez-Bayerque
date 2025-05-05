from persona import persona
from organo import organo
import random 

ESPECIALIDADES={"cardiovascular":["corazon"], "pulmonar":["pulmones"],"plastico":["corneas","piel"], "traumatologo":["huesos"], "gastroenterologo":["intestino","riñon","higado","pancreas"]}

class cirujano(persona):

    def __init__(self, nombre, especialidad, disponibilidad, cantidad_operaciones, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud):
        
        super().__init__( nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad
        self.cantidad_operaciones = cantidad_operaciones

        self.nombre=nombre
        self.especialidad=especialidad
        self.disponibilidad=True
        self.cantidad_operaciones=cantidad_operaciones

    def ocupado (self):
        self.disponibilidad=False
    def disponible (self):
        self.disponibilidad=True
   
    def operacion(self):
        if self.disponibilidad==False:
            print (f"Cirujano {self.nombre} ya opero hoy!")
            self.cantidad_operaciones=+1
    
    def calcular_exito(self,organo_tipo):

        if self.especialidad is None:
            resultado=random.randint(1,10)
            return resultado >5
        else: 
            organo_especialidad= ESPECIALIDADES

        if organo_tipo in organo_especialidad:
            resultado=random.randint(1,10)
            return resultado >=3
        else: 
            resultado=random.randit(1,10)
            return resultado >5 #donde pondriamos si es exitoso o no

    def __str__(self):
        if self.especialidad:
            esp= f"especialidad{self.especialidad}"
        else: 
            esp="general"
        return f"Cirujano:{self.nombre}"
    

