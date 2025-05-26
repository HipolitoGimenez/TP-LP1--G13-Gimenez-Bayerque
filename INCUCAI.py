<<<<<<< HEAD
from donantes import Donante
from paciente import Paciente
from receptor import Receptor
from coincidencia import Coincidencia 
from organo import Organo
from cirujano import Cirujano
from centro_de_salud import CentroDeSalud
=======

from donantes import Donante
from receptor import Receptor
from coincidencia import Coincidencia
from organo import Organo
from cirujano import cirujano
from centro_de_salud import centro_de_salud

>>>>>>> 90dcf3b (Mis cambios locales antes de hacer pull)

class INCUCAI:

    def __init__(self):
             #listas vacias y luego voy agregando
<<<<<<< HEAD
             self.lista_donantes=[] # en el main tengo todos los datos pero el incucai agrega entonces lo invoco en el main
<<<<<<< HEAD
=======
             self.lista_dontantes=[] # en el main tengo todos los datos pero el incucai agrega entonces lo invoco en el main
>>>>>>> 90dcf3b (Mis cambios locales antes de hacer pull)
             self.lista_organos=[]
             self.lista_cirujanos=[]
=======
>>>>>>> 7b5cabf (Guardo todos mis cambios)
             self.lista_centro_salud=[]
             self.lista_receptores=[]
             self.lista_coincidencia=[]
<<<<<<< HEAD

    '''def match_pacientes(self):
     receptores_a_eliminar = []
     donantes_a_eliminar = []

     for receptor in self.lista_receptores:
        for receptor_organo in receptor.organos:
            for donante in self.lista_donantes:
                for organo in donante.lista_organos:
                    if organo == receptor_organo and receptor.tipo_sangre == donante.tipo_de_sangre:
                        coincidencia = Coincidencia(donante, receptor)
                        self.lista_coincidencias.append(coincidencia)
                        
                        # Marcar receptor para eliminar (asumimos que se asigna solo un órgano)
                        if receptor not in receptores_a_eliminar:
                            receptores_a_eliminar.append(receptor)
                        
                        # Quitar el órgano del donante
                        donante.lista_organos.remove(organo)
                        # Si donante sin órganos, marcar para eliminar
                        if len(donante.lista_organos) == 0 and donante not in donantes_a_eliminar:
                            donantes_a_eliminar.append(donante)
                        break  # Salir de ciclo de órganos donante (porque se asignó uno)
                else:
                    continue
                break  # Salir de ciclo de donantes si hubo coincidencia
            else:
                continue
            break  # Salir de ciclo órganos receptor si hubo coincidencia

    # Eliminar receptores y donantes marcados
     for r in receptores_a_eliminar:
        self.lista_receptores.remove(r)
     for d in donantes_a_eliminar:
        self.lista_donantes.remove(d)
                   
    def agregar_receptor(self,nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia):
    #recibe por parametro todos los datos 
    #generar un nuevo objeto de receptor y lo guardo en la lista
    
        receptor=Receptor(nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia)
        pos=0#pos va a ser contado va a ser 0 y va sumar uno mientras recorra el for
        fue_agregado=False    
        for receptor_existente in self.lista_receptores:
            if fecha_de_nacimiento<receptor_existente.fecha_de_nacimiento:
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
        self.lista_donantes.append(donante)
        self.match_pacientes() #una vez que se inserta un donante debe hacer match hacer la busqueda
          
<<<<<<< HEAD
    #
=======
    
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
    
        receptor=Receptor(self, nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia)
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
          
    
>>>>>>> 90dcf3b (Mis cambios locales antes de hacer pull)
=======
    '''

    def registrarPaciente(self, paciente:Paciente):

        if not self.estaRegistradoPaciente(paciente):
            if isinstance(paciente, Donante):
                  self.lista_donantes.append(paciente)
                  self.buscarReceptores(paciente)
            else:
                  self.lista_receptores.append(paciente)
                  self.buscarDonante(paciente)
        else:
             print('El paciente ya fue registrado previamente')

    # Valida si el paciente ya esta registrado en cualquiera de las 2 listas
    def estaRegistradoPaciente(self, otroPaciente: Paciente):
        yaFueRegistrado = False
        for paciente in self.lista_donantes:
            if paciente == otroPaciente:
                return True
            
        for paciente in self.lista_receptores:
            if paciente == otroPaciente:
                return True
        return yaFueRegistrado

    def buscarReceptores(self, donante: Donante):
        listaReceptoresParaDonante=[]
        for organo in donante.lista_organos:
            receptor: Receptor
            for receptor in self.lista_receptores:
                  if receptor.organo_necesario.tipo == organo.tipo and receptor.tipo_de_sangre == donante.tipo_de_sangre:
                        listaReceptoresParaDonante.append(receptor)
            
            receptorElegido = listaReceptoresParaDonante.index(0)
            for receptor in listaReceptoresParaDonante:
                receptor.prioridad < receptorElegido.prioridad #esto se puede hacer por la funcion __lt__
                receptorElegido=receptor
            if receptorElegido is not None:
                  self.enviarOrganosAUbicacionReceptor(receptorElegido)
                  donante.lista_organos.remove(organo)

                
    def buscarDonante(self, receptor:Receptor):
          donante: Donante=None
          for donante in self.lista_donantes:
                if receptor.tipo_de_sangre == donante.tipo_de_sangre and donante.tieneOrgano(receptor.organo_necesario):
                      self.enviarOrganosAUbicacionReceptor(receptor)
                      donante.lista_organos.remove(receptor.organo_necesario)

    def enviarOrganoAUbicacionReceptor(self,receptor:Receptor):
          receptor.recibioOrgano = True
    
    def iniciarProtocoloTransplanteYTransporte(self,donante: Donante,centroSaludReceptor: CentroDeSalud, organo: Organo):
          donante.centro_de_salud.asignarVehiculo(centroSaludReceptor, organo)
          donante.centro_de_salud.asignarCirujano(organo)
          donante.centro_de_salud.realizarAblacion(organo)

    # Quitar de la lista de donantes a aquellos cuyos organos ya han sido utilizados en su totalidad
    def quitarDonantesSinOrganos(self):
        donante: Donante
        for donante in self.lista_donantes:
            if not donante.lista_organos:
                self.lista_donantes.remove(donante)

    # Quitar de la lista a un receptor una vez que ha recibido su organo exitosamente.
    def quitarReceptorConCirugiaExitosa(self):
        receptor: Receptor
        for receptor in self.lista_receptores:
            if receptor.recibioOrgano:
                self.lista_receptores.remove(receptor)

    # Buscar por centro de salud los pacientes de la lista de espera.
    def buscarPacientesListaEsperaPorCentroSalud(self, centroDeSalud):
        pacientesListaEspera = []
        receptor: Receptor
        for receptor in self.lista_receptores:
            if receptor.centro_de_salud == centroDeSalud:
                pacientesListaEspera.append(receptor)

    # Buscar un receptor e informar qué prioridad tiene en la lista de espera.
    def buscarPrioridadReceptor(self, receptorBuscado):
        prioridad: int
        receptor: Receptor
        for receptor in self.lista_receptores:
            if receptor == receptorBuscado:
                return receptor.prioridad
        return prioridad

    # Imprimir listado de pacientes donantes y receptores.
    def listarPacientes(self):
        for paciente in self.lista_donantes:
            print(paciente)
        for paciente in self.lista_receptores:
            print(paciente)


          
    
        
          

                  
    
>>>>>>> 7b5cabf (Guardo todos mis cambios)
        