from persona import persona

class receptor(persona):

    def __init__(self, organo_necesario, estado, fecha_de_ingreso, prioridad, patologia):
        

        self.organo_necesario=organo_necesario
        self.estado=estado
        self.fecha_de_ingreso=fecha_de_ingreso
        self.prioridad=prioridad
        self.patologia=patologia