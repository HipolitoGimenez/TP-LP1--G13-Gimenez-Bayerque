
import random 

ESPECIALIDADES = {
            "cardiovascular": ["corazon"],
            "pulmonar": ["pulmones"],
            "plastico": ["corneas", "piel"],
            "traumatologo": ["huesos"],
            "gastroenterologo": ["intestino", "riñon", "higado", "pancreas"]
            }

class Cirujano:
    def __init__(self, nombre, especialidad, disponibilidad, cantidad_operaciones, dni, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, organos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponibilidad = disponibilidad#True o False
        self.cantidad_operaciones = cantidad_operaciones
        self.dni = dni
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.tipo_de_sangre = tipo_de_sangre
        self.centro_de_salud = centro_de_salud #asociacion a un centro
        self.organos = organos#lista de organos que puede operar o ha operado


    def __str__(self): #este metodo permite que cuando hagas print(cirujano), te muestre un texto legible con su nombre y especialidad
        return f"Cirujano: {self.nombre} - Especialidad: {self.especialidad}"
    
    def ocupado(self): #metodos para marcar cirujano como ocupado o disponible
        self.disponibilidad = False

    def disponible(self):
        self.disponibilidad = True

    def es_especialista(self, organo): #usa el diccionario para buscar los organos que puede operar segun su especialidad
        ESPECIALIDADES = {
        "cardiovascular": ["corazon"],
        "pulmonar": ["pulmones"],
        "plastico": ["corneas", "piel"],
        "traumatologo": ["huesos"],
        "gastroenterologo": ["intestino", "riñon", "higado", "pancreas"]
    }
        return self.especialidad is not None and organo in ESPECIALIDADES.get(self.especialidad, [])# usa get para evitar errores si la especialidad no existe, devuelve true si el organo esta en la lista correspondiente

        
    def operacion(self):
        if not self.disponibilidad: #imprime mensaje si no esta disponible para operar
            print (f"Cirujano {self.nombre} ya opero hoy.")
            self.cantidad_operaciones += 1

    def calcular_exito(self, organo_tipo):#simula exito de una operacion
        organos_de_su_especialidad = ESPECIALIDADES.get(self.especialidad.lower(), []) # busca en el diccionario el organo de especialidad del cirujano, Retorna ["corazon"] porque es lo que hay en el diccionario para esa especialidad.Y si no hay coincidencia Retorna una lista vacía [], así no se rompe el programa. Evita un KeyError.
        
        resultado = random.randint(1, 10)#genera numero aleatorio entre 1 y 10
        if organo_tipo.lower() in organos_de_su_especialidad: #si el organo es de su especialidad
            return resultado >= 3# de 3 a 10 70% de exito la operacion
        return resultado > 5#si no lo de 6 a 10 %50