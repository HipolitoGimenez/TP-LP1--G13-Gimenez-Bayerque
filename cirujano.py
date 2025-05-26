
from paciente import Paciente
from organo import Organo
import random 
ESPECIALIDADES = {
            "cardiovascular": ["corazon"],
            "pulmonar": ["pulmones"],
            "plastico": ["corneas", "piel"],
            "traumatologo": ["huesos"],
            "gastroenterologo": ["intestino", "riñon", "higado", "pancreas"]}

class Cirujano:
    def __init__(self, nombre, especialidad, disponibilidad, cantidad_operaciones, dni, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, organos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad
        self.cantidad_operaciones = cantidad_operaciones
        self.dni = dni
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.tipo_de_sangre = tipo_de_sangre
        self.centro_de_salud = centro_de_salud
        self.organos = organos

    def __str__(self):
        return f"Cirujano: {self.nombre} - Especialidad: {self.especialidad}"
    
    def ocupado(self):
        self.disponibilidad = False

    def disponible(self):
        self.disponibilidad = True

    def es_especialista(self, organo):
        ESPECIALIDADES = {
        "cardiovascular": ["corazon"],
        "pulmonar": ["pulmones"],
        "plastico": ["corneas", "piel"],
        "traumatologo": ["huesos"],
        "gastroenterologo": ["intestino", "riñon", "higado", "pancreas"]
    }
        return self.especialidad is not None and organo in ESPECIALIDADES.get(self.especialidad, [])

        
    def operacion(self):
        if not self.disponibilidad:
            print (f"Cirujano {self.nombre} ya opero hoy.")
            self.cantidad_operaciones=+1

    def calcular_exito(self, organo_tipo):
        organos_de_su_especialidad = ESPECIALIDADES.get(self.especialidad.lower(), []) # busca en el diccionario el organo de especialidad del cirujano, Retorna ["corazon"] porque es lo que hay en el diccionario para esa especialidad.Y si no hay coincidencia Retorna una lista vacía [], así no se rompe el programa. Evita un KeyError.
        
        resultado = random.randint(1, 10)
        if organo_tipo.lower() in organos_de_su_especialidad:
            return resultado >= 3
        return resultado > 5