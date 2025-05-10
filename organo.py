from datetime import datetime

class organo:

    def __init__(self, tipo):
        print("Constructor correcto llamado")


        self.tipo=tipo.lower() 
        self.fecha_hora_de_ablacion=None
        self.fecha_extraccion=None

    def fecha_extraccion(self, fecha):

        self.fecha_extraccion=fecha
        
    def fecha_ablacion(self, fecha_hora: datetime):
        
        self.fecha_hora_de_ablacion = fecha_hora 

    def esta_disponible(self):
        
        return self.fecha_hora_de_ablacion is None 

    def __str__(self): 
        ablacion = self.fecha_hora_de_ablacion.strftime("%Y-%m-%d %H:%M") if self.fecha_hora_de_ablacion else "No ablacionado" 
        return f"Órgano: {self.tipo.capitalize()}, Ablación: {ablacion}" 
        