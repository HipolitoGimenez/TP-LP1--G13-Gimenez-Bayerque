from organo import datetime

class organo:

    def __init__(self, tipo, fecha_de_ablacion, hora_de_ablacion):

        self.tipo=tipo.lower() #para uniformidad El tipo lo pasás vos cuando instanciás un órgano (Organo("corazon")).Se guarda en el atributo self.tipo y se muestra bonito gracias a __str__.
        self.fecha_hora_de_ablacion=None
        
    def set_fecha_ablacion(self, fecha_hora: datetime):
        
        self.fecha_hora_ablacion = fecha_hora #la fecha hora que se ingrese que se va a ver como date time la  establece como fecha y hora de ablacion del organo

    def esta_disponible(self):
        
        return self.fecha_hora_ablacion is None # fecha hora de ablacion es none  retorna true si no false ya fue ablacionado

    def __str__(self): #-str_ sirve para el print organo
        ablacion = self.fecha_hora_ablacion.strftime("%Y-%m-%d %H:%M") if self.fecha_hora_ablacion else "No ablacionado" #ablacion es si tiene fecha hora de ablacion , usa strftime(...) para convertir la fecha a texto con formato: año-mes-día hora:minutos, por ejemplo: 2025-05-04 15:30 si es none se imprime el mensaje
        return f"Órgano: {self.tipo.capitalize()}, Ablación: {ablacion}" # se retorna el organo su tipo que lo pone la primera letra con mayuscula y su ablacion
        