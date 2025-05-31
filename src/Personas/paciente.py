

class Paciente:

        def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud):
                from src.Modelos.CentroDeSalud import CentroDeSalud  
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
                        
        def get_Nombre(self):
                """
                Devuelve el nombre del paciente.

                Returns:
                str: Nombre del paciente.
                """
                return self.__nombre
        
        def get_DNI(self):
                """
                Devuelve el número de DNI del paciente.

                Returns:
                int: DNI del paciente.
                """
                return self.__DNI
                
        def get_Fecha_de_nacimiento(self):
                """
        Devuelve la fecha de nacimiento del paciente.

        Returns:
                datetime: Fecha de nacimiento.
        """
                return self.__fecha_de_nacimiento
                
        def get_Sexo(self):
                """
        Devuelve el sexo del paciente.

        Returns:
                str: Sexo del paciente.
        """
                return self.__sexo
                
        def get_Telefono(self):
                """
        Devuelve el número de teléfono del paciente.

        Returns:
                str: Teléfono del paciente.
        """
                return self.__telefono
                
        def getTipo_de_sangre(self):
                """
        Devuelve el tipo de sangre del paciente.

        Returns:
                str: Tipo de sangre.
        """
                return self.__tipo_de_sangre
                
        def getCentro_de_salud(self):
                """
        Devuelve el centro de salud asociado al paciente.

        Returns:
                CentroDeSalud: Centro de salud del paciente.
        """
                return f"Centro de Salud: {self.__centro_de_salud}"
                
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


        
        
           