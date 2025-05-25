from persona import persona
from datetime import datetime

class donante(persona):

    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, lista_organos):
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)
        self.lista_organos = lista_organos

    def __str__(self):
        return f"Donante - {self.nombre} (DNI: {self.DNI}), Órganos: {', '.join(self.lista_organos)}, Sangre: {self.tipo_de_sangre}, Centro: {self.centro_de_salud.nombre}"
    
    '''def calculo_horas (self,datetime):
        self.fecha_hora_ablacion - self.fecha_de_muerte <'''
       

   

    

    

