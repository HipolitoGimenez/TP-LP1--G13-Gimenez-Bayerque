from src.Personas.paciente import Paciente
from src.Modelos.organo import Organo
from datetime import datetime


class Receptor(Paciente):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre,
                 centro_de_salud, organo_necesario, estado, fecha_de_ingreso, prioridad, patologia):

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un string no vacío.")
        if not isinstance(DNI, (str, int)):
            raise TypeError("El DNI debe ser un string o entero.")
        if not isinstance(fecha_de_nacimiento, str):
            raise TypeError("La fecha de nacimiento debe ser un string.")
        if not isinstance(fecha_de_ingreso, datetime):
            raise TypeError("La fecha de ingreso debe ser un objeto datetime.")
        if not isinstance(prioridad, int) or prioridad < 0:
            raise ValueError("La prioridad debe ser un entero no negativo.")
        if not isinstance(organo_necesario, Organo):
            raise TypeError("El órgano necesario debe ser una instancia de la clase Organo.")
        
        estado_normalizado = estado.capitalize()
        if estado_normalizado not in ["Estable", "Inestable"]:
            raise ValueError("El estado debe ser 'Estable' o 'Inestable'.")

        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)

        self.organo_necesario: Organo = organo_necesario
        self.__estado = estado_normalizado
        self.__fecha_de_ingreso = fecha_de_ingreso
        self.__prioridad = prioridad
        self.__patologia = patologia
        self.__recibioOrgano = False

    def get_Estado(self):
        return self.__estado

    def get_Nombre(self):
        return self.nombre

    def get_Fecha_de_ingreso(self):
        return self.__fecha_de_ingreso

    def get_Prioridad(self):
        return self.__prioridad

    def get_Patologia(self):
        return self.__patologia

    def get_RecibioOrgano(self):
        return self.__recibioOrgano

    def set_estado(self, nuevo_estado):
        nuevo_estado = nuevo_estado.capitalize()
        if nuevo_estado not in ["Estable", "Inestable"]:
            raise ValueError("El estado debe ser 'Estable' o 'Inestable'.")
        self.__estado = nuevo_estado

    def __str__(self):
        return (f"{super().__str__()}, Necesita: {self.organo_necesario}, "
                f"Prioridad: {self.__prioridad}, Estado: {self.__estado}")

    def __lt__(self, otro):
        if self.__prioridad != otro.__prioridad:
            return self.__prioridad < otro.__prioridad
        return self.__fecha_de_ingreso < otro.__fecha_de_ingreso
