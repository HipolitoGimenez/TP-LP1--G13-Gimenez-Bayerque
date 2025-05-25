from persona import persona

class Receptor(persona):
    def __init__(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, organo_necesario, estado, fecha_de_ingreso, prioridad, patologia):
        super().__init__(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud)

        self.estado = estado
        self.fecha_de_ingreso = fecha_de_ingreso
        self.prioridad = prioridad
        self.patologia = patologia
        self.organos = [organo_necesario]  

    def __str__(self):
        return f"Receptor - {self.nombre} (DNI: {self.DNI}), Necesita: {', '.join(self.organos)}, Prioridad: {self.prioridad}"

    def __lt__(self, otro):
        if self.prioridad != otro.prioridad:
            return self.prioridad < otro.prioridad
        return self.fecha_de_ingreso < otro.fecha_de_ingreso
