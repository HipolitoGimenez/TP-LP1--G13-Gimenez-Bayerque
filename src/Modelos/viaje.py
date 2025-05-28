
class Viaje:
    """
    Representa un viaje realizado por un vehículo con destino, duración y fecha.
    """

    def __init__(self, direccion, tiempo, fecha):
        """
        Inicializa un viaje con dirección, tiempo y fecha.

        Args:
            direccion (str): Dirección o destino del viaje.
            tiempo (float/int): Duración estimada del viaje (por ejemplo, en minutos o horas).
            fecha (datetime): Fecha y hora en que se realizó el viaje.

        Returns:
            None
        """
        self.direccion=direccion
        self.tiempo=tiempo
        self.fecha=fecha