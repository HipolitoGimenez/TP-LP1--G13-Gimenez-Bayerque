from src.Modelos.CentroDeSalud import CentroDeSalud

class Paciente:

 def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud):
        """
        Inicializa un objeto Paciente con sus datos personales y centro de salud asociado.

        Args:
            nombre (str): Nombre completo del paciente.
            DNI (str o int): Documento Nacional de Identidad del paciente.
            fecha_de_nacimiento (str): Fecha de nacimiento del paciente.
            sexo (str): Sexo del paciente.
            telefono (str): Número de teléfono del paciente.
            tipo_de_sangre (str): Tipo de sangre del paciente.
            centro_de_salud (CentroDeSalud): Centro de salud asociado al paciente.

        Returns:
            None
        """
        self.nombre=nombre
        self.DNI=DNI
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.sexo=sexo
        self.telefono=telefono
        self.tipo_de_sangre=tipo_de_sangre
        self.centro_de_salud: CentroDeSalud=centro_de_salud
        

def __str__(self):
        """
        Devuelve una representación legible con los datos principales del paciente.

        Returns:
            str: Cadena con nombre y DNI del paciente.
        """
        return f"Nombre: {self.nombre} , DNI: {self.DNI}"


def __eq__(self, otroPaciente): 
        """
        Compara dos pacientes por nombre y DNI para determinar si son iguales.

        Args:
            otroPaciente (Paciente): Otro objeto paciente para comparar.

        Returns:
            bool: True si ambos pacientes tienen el mismo nombre y DNI, False en caso contrario.
        """
        return self.nombre == otroPaciente.nombre and self.DNI == otroPaciente.DNI


    
    
    