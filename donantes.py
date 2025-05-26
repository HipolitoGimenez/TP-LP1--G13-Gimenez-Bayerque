from paciente import Paciente
from datetime import datetime

<<<<<<< HEAD
class Donante(persona):

<<<<<<< HEAD
    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, lista_organos):
=======
class Donante(Paciente):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, lista_organos,fecha_de_muerte,fecha_hora_ablacion):
        
>>>>>>> 7b5cabf (Guardo todos mis cambios)
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.fecha_de_muerte=fecha_de_muerte
        self.fecha_hora_ablacion= fecha_hora_ablacion
        self.lista_organos =[]

    def tieneOrgano(self, organo):
        for organo in self.lista_organos:
            organo.tipo == organo.tipo
            return True
        return False
    
    def __str__(self):
<<<<<<< HEAD
        return f"Donante - {self.nombre} (DNI: {self.DNI}), Órganos: {', '.join(self.lista_organos)}, Sangre: {self.tipo_de_sangre}, Centro: {self.centro_de_salud.nombre}"
=======
    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,patologia, fecha_de_muerte, fecha_hora_ablacion):
   
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.tipo_de_sangre=tipo_de_sangre#lo voy a necesitar para el match 
        self.fecha_de_muerte=fecha_de_muerte
        self.lista_organos=[]
        self.fecha_hora_ablacion= fecha_hora_ablacion


    def __str__ (self):
        return f"{super().__str__}, Donante desde: {self.fecha_de_muerte}"
>>>>>>> 90dcf3b (Mis cambios locales antes de hacer pull)
=======
        return f"{super().__str__}, Donante desde: {self.fecha_de_muerte}"
    
    def quitarOrgano(self, organo):
        self.lista_organos.remove(organo)
>>>>>>> 7b5cabf (Guardo todos mis cambios)
    
    '''def calculo_horas (self,datetime):
        self.fecha_hora_ablacion - self.fecha_de_muerte <'''
       

   

    

    

