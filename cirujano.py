from persona import persona
from organo import organo
import random 

ESPECIALIDADES={
    "cardiovascular":["corazon"], 
    "pulmonar":["pulmones"],
    "plastico":["corneas","piel"],
    "traumatologo":["huesos"], 
    "gastroenterologo":["intestino","riñon","higado","pancreas"]}

class cirujano(persona):

    def __init__(self, nombre, especialidad, disponibilidad, cantidad_operaciones, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud):
        
        super().__init__( nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad
        self.cantidad_operaciones = cantidad_operaciones

       
    def ocupado (self):
        self.disponibilidad=False
    def disponible (self):
        self.disponibilidad=True
   
    def operacion(self):
        if not self.disponibilidad:
            print (f"Cirujano {self.nombre} ya opero hoy.")
            self.cantidad_operaciones=+1
    
    def calcular_exito(self,organo_tipo):
        organos_de_su_especialidad = ESPECIALIDADES.get(self.especialidad.lower(), []) # busca en el diccionario el organo de especialidad del cirujano, Retorna ["corazon"] porque es lo que hay en el diccionario para esa especialidad.Y si no hay coincidencia Retorna una lista vacía [], así no se rompe el programa. Evita un KeyError.

        resultado = random.randint(1, 10)
        if organo_tipo in organos_de_su_especialidad:
            return resultado >= 3
        return resultado > 5

        
    def __str__(self):
        return f"Cirujano: {self.nombre} - Especialidad: {self.especialidad}"
