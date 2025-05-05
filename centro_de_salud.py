from organo import organo
from vehiculo import vehiculo
from cirujano import cirujano



class centro_de_salud:



    def __init__(self, nombre_institucion, direccion, partido, provincia, telefono,
                  lista_cirujanos:list[cirujano], lista_vehiculos:list[vehiculo]):
        
        self.nombre_institucion=nombre_institucion
        self.direccion=direccion
        self.partido=partido
        self.provincia=provincia
        self.telefono=telefono
        self.lista_cirujanos=lista_cirujanos
        self.lista_vehiculos=lista_vehiculos
        
    

    def buscar_transporte(self, provincia, partido):


    
    def buscar_cirujano(self, cir : cirujano)
        




    