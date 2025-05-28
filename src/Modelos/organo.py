from datetime import datetime

class Organo:

    def __init__(self, tipo):
        self.tipo=tipo.lower() #Guarda el tipo de órgano como una cadena en minúsculas.
        self.fecha_hora_de_ablacion=None #Inicializa la fecha y hora de ablación como None. 
        
    def fecha_ablacion(self, fecha_hora: datetime):#Método para asignar la fecha y hora de ablación. Recibe un objeto datetime como parámetro.
        
        self.fecha_hora_de_ablacion = fecha_hora #Guarda la fecha y hora recibida en el atributo correspondiente del órgano.

    def esta_disponible(self):# Metodo que indica si el organo esta disponible
        
        return self.fecha_hora_de_ablacion is None #Devuelve True si el órgano no fue ablacionado todavía (es decir, si su fecha de ablación sigue siendo None), y False si ya fue extraído.

# Método mágico que devuelve los datos importantes de la ablacion de un organo
    def __str__(self): 
        ablacion = self.fecha_hora_de_ablacion.strftime("%Y-%m-%d %H:%M") if self.fecha_hora_de_ablacion else "No ablacionado" 
        return f"Órgano: {self.tipo.capitalize()}, Ablación: {ablacion}" 
        