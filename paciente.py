from centro_de_salud import CentroDeSalud

class Paciente:

 def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud):
    
        self.nombre=nombre
        self.DNI=DNI
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.sexo=sexo
        self.telefono=telefono
        self.tipo_de_sangre=tipo_de_sangre
        self.centro_de_salud: CentroDeSalud=centro_de_salud
        
# Método mágico que devuelve los datos importantes de una persona
def __str__(self):
        return f"Nombre: {self.nombre} , DNI: {self.DNI}"

def __eq__(self, otroPaciente): 
        return self.nombre == otroPaciente.nombre and self.DNI == otroPaciente.DNI


    
    
    