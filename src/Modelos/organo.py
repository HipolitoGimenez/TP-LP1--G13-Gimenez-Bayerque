from datetime import datetime


class Organo:

    def __init__(self, tipo):
        """
        Recibe:
            - tipo: str, tipo de órgano.
        Hace:
            - Inicializa el órgano con el tipo en minúsculas.
            - Inicializa la fecha y hora de ablación como None.
        Devuelve:
            - Nada explícito, solo crea la instancia.
        """
        self.tipo=tipo.lower() 
        self.fecha_hora_de_ablacion=None 
        
        
    
    def fecha_ablacion(self, fecha_hora: datetime):
        """
        Recibe:
            - fecha_hora: objeto datetime que indica cuándo se realizó la ablación.
        Hace:
            - Asigna la fecha y hora de ablación al órgano.
        Devuelve:
            - Nada explícito.
        """
        self.fecha_hora_de_ablacion = fecha_hora 
    

    def __str__(self): 
        """
        Recibe:
            - Ningún parámetro.
        Hace:
            - Construye una cadena descriptiva del órgano y su estado de ablación.
        Devuelve:
            - Una cadena con el tipo de órgano y la fecha/hora de ablación o un mensaje si no fue ablacionado.
        """
        ablacion = self.fecha_hora_de_ablacion.strftime("%Y-%m-%d %H:%M") if self.fecha_hora_de_ablacion else "No ablacionado" 
        return f"Órgano: {self.tipo.capitalize()}, Ablación: {ablacion}" 
        