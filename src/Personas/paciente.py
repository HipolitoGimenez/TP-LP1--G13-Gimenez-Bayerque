from src.Modelos.CentroDeSalud import CentroDeSalud

class Paciente:

 def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud):
    
        self.nombre=nombre#Guarda el nombre del paciente
        self.DNI=DNI#Guarda eel dni del paciente
        self.fecha_de_nacimiento=fecha_de_nacimiento#Guarda la fecha de nacimiento del paciente. 
        self.sexo=sexo#Guarda el sexo del paciente
        self.telefono=telefono#Guarda el número de teléfono del paciente.
        self.tipo_de_sangre=tipo_de_sangre#Guarda el tipo de sangre del paciente
        self.centro_de_salud: CentroDeSalud=centro_de_salud#Guarda el centro de salud asociado al paciente.
        
# Método mágico que devuelve los datos importantes de una persona
def __str__(self):
        return f"Nombre: {self.nombre} , DNI: {self.DNI}"

def __eq__(self, otroPaciente): # Método mágico para comparar dos pacientes. Devuelve True si ambos pacientes tienen el mismo nombre y el mismo DNI.

        return self.nombre == otroPaciente.nombre and self.DNI == otroPaciente.DNI


    
    
    