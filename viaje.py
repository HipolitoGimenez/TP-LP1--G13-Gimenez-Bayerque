
class Viaje:
#registrar viaje quiere un objeto no un valor
    def __init__(self, direccion, tiempo, fecha):
        self.direccion=direccion
        self.tiempo=tiempo
        self.fecha=fecha