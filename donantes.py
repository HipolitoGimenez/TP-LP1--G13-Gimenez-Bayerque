from paciente import Paciente
from datetime import datetime

class Donante(Paciente):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, fecha_de_muerte, fecha_hora_ablacion):
   
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.fecha_de_muerte=fecha_de_muerte
        self.fecha_hora_ablacion= fecha_hora_ablacion
        self.lista_organos=[]

    def tieneOrgano(self, organo):
        for organo in self.lista_organos:
            organo.tipo == organo.tipo
            return True
        return False


    def __str__ (self):
        return f"{super().__str__}, Donante desde: {self.fecha_de_muerte}"
    
    def quitarOrgano(self, organo):
        self.lista_organos.remove(organo)
    
    
       

   

    

    



   

    

    

