from persona import persona
from datetime import datetime

class donante(persona):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia, fecha_de_muerte, fecha_hora_ablacion):
   
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)

        self.fecha_de_muerte=fecha_de_muerte
        self.lista_de_organos=[]
        self.fecha_hora_ablacion= fecha_hora_ablacion


    def __str__ (self):
        return f"{super().__str__}, Donante desde: {self.fecha_de_muerte}"
    
    '''def calculo_horas (self,datetime):
        self.fecha_hora_ablacion - self.fecha_de_muerte <'''
       

   

    

    

