from persona import persona
from organo import organo
from cirujano import cirujano
from centro_de_salud import centro_de_salud
from receptor import receptor
from datetime import timedelta
class INCUCAI:

    def __init__(self):
       
       self.lista_receptores=[]
       self.lista_donates=[]
       self.lista_centros_de_salud=[]
    
    def registrar_receptores(self, receptor):  

        self.lista_receptores.append(receptor)
    
    def registrar_donantes(self, donante):
         
             self.lista_donates.append(donante)


    def buscar_posibles_receptores(self, donante, organo):
       
        if len(self.lista_receptores) == 0:
         print("No hay receptores registrados.")
         return []
        posibles = []
        for i in range(len(self.lista_receptores)):
          receptor = self.lista_receptores[i]
          if receptor.organo== organo_donado and receptor.grupo_sanguineo == grupo_donante:
             posibles.append(receptor)


        if len(posibles) == 0:
            print("No se encontraron receptores compatibles.")
        else:
             print(f"Se encontraron {len(posibles)} receptor(es) compatible(s):")
             for r in posibles:
              print(f"  - {r.nombre} | DNI: {r.dni} | Prioridad: {r.prioridad}")
        
        return posibles



       
       
    
    def eliminar_donante(self, donante):
        for donante in self.lista_donates:
     
            self.lista_donates.remove(donante)
            return
       # print(f"No se encontró un donante con DNI {dni}.")

     # def match_pacientes(self,per:tipo_de_sangre ):

     # match_cirujanos(self)