from persona import persona


class cirujano(persona):

    def __init__(self, nombre, especialidad, disponibilidad, cantidad_operaciones):
        
        super().__init__(nombre)
        self.nombre=nombre
        self.especialidad=especialidad
        self.disponibilidad=disponibilidad
        self.ccanridad_operaciones=cantidad_operaciones

