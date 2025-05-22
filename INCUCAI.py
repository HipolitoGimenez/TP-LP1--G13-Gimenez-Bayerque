from donantes import Donante
from receptor import Receptor
from coincidencia import Coincidencia 
from organo import Organo
from cirujano import Cirujano
from centro_de_salud import CentroDeSalud

class INCUCAI:

    def __init__(self):
             #listas vacias y luego voy agregando
             self.lista_dontantes=[] # en el main tengo todos los datos pero el incucai agrega entonces lo invoco en el main
             self.lista_organos=[]
             self.lista_cirujanos=[]
             self.lista_centro_salud=[]
             self.lista_receptores=[]
             self.lista_coincidencia=[]
    
    
    def match_pacientes(self):
        for receptor in self.lista_receptores:#la lista ya debe estar ordenada por prioridad, la recorro:
            for receptor_organo in receptor.organos: #receptor lista de organos
                for donante in self.lista_donantes:#corro lista de donantes 
                    for organo in donante.lista_organos:
                         if organo == receptor_organo and receptor.tipo_sangre==donante.tipo_de_sangre:
                               coincidencia=Coincidencia(donante,receptor) #creando un objeto de la clase coincidencia que guarda como parametro receptor y donante
                               self.lista_coincidencias.append(coincidencia)#nueva entidad guardar organo donante y receptor en una lista de coincidencias, utilizo el objeto que cree
                                #faltaria quitar ese receptor de la lista y ese donante si es que no tiene mas donante
                       
    def agregar_receptor(self,nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia):
    #recibe por parametro todos los datos 
    #generar un nuevo objeto de receptor y lo guardo en la lista
    
        receptor=Receptor(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia)
        pos=0#pos va a ser contado va a ser 0 y va sumar uno mientras recorra el for
        fue_agregado=False    
        for receptor in self.lista_receptores:
            if fecha_de_nacimiento<receptor.fecha_de_nacimiento:
                  self.lista_receptores.insert(pos,receptor)#se agrega el objeto con los datos a la lista de receptor con prioridad de menor nacimiento
                  fue_agregado=True
            elif fecha_de_nacimiento==receptor.fecha_de_nacimiento:
                 if fecha_de_ingreso<receptor.fecha_de_ingreso:
                    self.lista_receptores.insert(pos,receptor)
                    fue_agregado=True
            pos+=1#acumula uno a lo que tiene
        if fue_agregado==False:
             self.lista_receptores.append(receptor)#ya esta ordenado entonces el de edad mayor al final de la lista
        self.match_pacientes()#invoco a un miembro de esta clase

    def agregar_donante(self,nombre,DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, fecha_hora_de_muerte, fecha_hora_ablacion):
        donante=Donante(nombre,DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud, fecha_hora_de_muerte, fecha_hora_ablacion)
        self.lista_dontantes.append(donante)
        self.match_pacientes() #una vez que se inserta un donante debe hacer match hacer la busqueda
          
    
        