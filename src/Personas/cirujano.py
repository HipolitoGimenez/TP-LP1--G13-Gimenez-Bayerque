
import random 
from src.Modelos.organo import Organo

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
        self.disponibilidad = disponibilidad
        self.cantidad_operaciones = cantidad_operaciones
        self.dni = dni
        self.centro_de_salud = centro_de_salud 



    def __str__(self): 
        """
        Devuelve una representación legible del cirujano.

        Returns:
            str: Nombre y especialidad del cirujano.
        """
        return f"Cirujano: {self.nombre} - Especialidad: {self.especialidad}"
    

    def ocupado(self): 
        """
        Marca al cirujano como ocupado (no disponible).

        Returns:
            None
        """
        self.disponibilidad = False


    def disponible(self):
        """
        Marca al cirujano como disponible para operar.

        Returns:
            bool: True si está disponible, False si no.
        """
        self.disponibilidad = True
        
    def estaDisponible(self):
        """
        Indica si el cirujano está disponible para operar.

        Returns:
        bool: True si está disponible, False si no lo está.
        """
        return self.disponibilidad

    def es_especialista(self, organo: Organo):
        """
        Verifica si el cirujano es especialista en operar un órgano específico.

        Args:
            organo (str): Tipo de órgano a verificar.

        Returns:
            bool: True si el cirujano es especialista en el órgano, False en caso contrario.
        """
        
        ESPECIALIDADES = {
        "cardiovascular": ["corazon"],
        "pulmonar": ["pulmones"],
        "plastico": ["corneas", "piel"],
        "traumatologo": ["huesos"],
        "gastroenterologo": ["intestino", "riñon", "higado", "pancreas"]
    }
        return self.especialidad is not None and organo.tipo in ESPECIALIDADES.get(self.especialidad, [])
    

    def operacion(self):
        """
        Registra una operación realizada por el cirujano. Marca como ocupado y aumenta contador.

        Returns:
            None
        """
        if not self.disponibilidad: 
            print (f"Cirujano {self.nombre} ya opero hoy.")
            self.cantidad_operaciones += 1


    def calcular_exito(self, organo_tipo):
        """
        Simula el éxito de una operación para un órgano específico.

        Args:
            organo_tipo (str): Tipo de órgano a operar.

        Returns:
            bool: True si la operación fue exitosa, False si no.
        """
        organos_de_su_especialidad = ESPECIALIDADES.get(self.especialidad.lower(), []) 
        
        resultado = random.randint(1, 10)
        if organo_tipo.lower() in organos_de_su_especialidad: 
            return resultado >= 3
        return resultado > 5