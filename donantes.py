from paciente import Paciente
from datetime import datetime


class Donante(Paciente):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,patologia, fecha_de_muerte, fecha_hora_ablacion):
   
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.tipo_de_sangre=tipo_de_sangre#lo voy a necesitar para el match 
        self.fecha_de_muerte=fecha_de_muerte
        self.lista_organos=[]
        self.fecha_hora_ablacion= fecha_hora_ablacion

    def tieneOrgano(self, organo):
        for organo in self.lista_organos:
            organo.tipo == organo.tipo
            return True
        return False
    
    def __str__ (self):
        return f"{super().__str__}, Donante desde: {self.fecha_de_muerte}"

    
    def quitarOrgano(self, organo):
        self.lista_organos.remove(organo)

    '''def calculo_horas (self,datetime):
        self.fecha_hora_ablacion - self.fecha_de_muerte <'''
       

   

    

    

