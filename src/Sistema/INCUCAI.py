
from src.Personas.donantes import Donante
from src.Personas.paciente import Paciente
from src.Personas.receptor import Receptor
from src.Modelos.coincidencia import Coincidencia
from src.Modelos.organo import Organo
from src.Personas.cirujano import Cirujano
from src.Modelos.CentroDeSalud import CentroDeSalud
class INCUCAI:

    def __init__(self):
             #listas vacias y luego voy agregando
             self.lista_donantes=[] # en el main tengo todos los datos pero el incucai agrega entonces lo invoco en el main
             self.lista_centro_salud=[]
             self.lista_receptores=[]
             self.lista_coincidencia=[]
    
    
    #  Registrar pacientes nuevos (Validando que no se encuentre en otra lista ni se repita).
    def registrarPaciente(self, paciente: Paciente):

        if not self._estaRegistradoPaciente(paciente):#verifica que el paciente no este registrado previament y llama al metodo
            if isinstance(paciente, Donante):#si el paciente es una instancia de la clase donante
                self.lista_donantes.append(paciente)#agrega ese paciente a la lista donante
                self._buscarReceptores(paciente)#llama al metodo priv para buscar receptores compatibles con los organos de ese donante
            else:
                self.lista_receptores.append(paciente)# si no es donante se agrega a la lista de receptores
                self._buscarDonantes(paciente)#y se busca donante compatible
        else:
            print('El paciente ya fue registrado previamente')#y si ya esta registrado se manda este mensaje

    # Valida si el paciente ya esta registrado en cualquiera de las 2 listas
    def _estaRegistradoPaciente(self, otroPaciente: Paciente):
        yaFueRegistrado = False
        for paciente in self.lista_donantes:
            if paciente == otroPaciente:
                return True
            
        for paciente in self.lista_receptores:
            if paciente == otroPaciente:
                return True
        return yaFueRegistrado
        
    def _buscarReceptores(self, donante: Donante):
        listaReceptoresParaDonante = []#crea una lista vacia para guardar los receptores compatibles que se vayan encontrando
        for organo in donante.lista_organos:#recorre cada organo disponible en la lista de organos del donante
            receptor: Receptor#la variable receptor sera de tipo receptor
            for receptor in self.lista_receptores:#recorre todos los receptores registrados en el sistema
                if receptor.organo_necesario.tipo == organo.tipo and receptor.tipo_de_sangre == donante.tipo_de_sangre:#comprueba que el receptor tenga mismotipo organo que el donante y tipo de sangre
                    listaReceptoresParaDonante.append(receptor)# si se cumple agrega el receptor a la lista
        
            receptorElegido = listaReceptoresParaDonante.index(0)#intenta obyener el indice del valor 0 de la lista
            for receptor in listaReceptoresParaDonante:#recorre nuevamente la lista para seleccionar el de mayor prioridad
                receptor.prioridad < receptorElegido.prioridad # Esto se pudo hacer por la funcion __lt__
                receptorElegido = receptor
            if receptorElegido is not None:#verifica que se haya elegido un receptor
                self._enviarOrganoAUbicacionReceptor(receptorElegido)#llama a metodo para marcar que el organo sera enviado a receptor
                donante.lista_organos.remove(organo)#elimina ese organo de la lista de donantes

    def _buscarDonantes(self, receptor: Receptor):
        donante: Donante = None
        for donante in self.lista_donantes:
            if receptor.tipo_de_sangre == donante.tipo_de_sangre and donante.tieneOrgano(receptor.organo_necesario):
                self._enviarOrganoAUbicacionReceptor(receptor)#llama al metodo para guardar info del receptor
                donante.lista_organos.remove(receptor.organo_necesario)#remueve le organo del donante

    def _enviarOrganoAUbicacionReceptor(self, receptor: Receptor):
        receptor.recibioOrgano = True#marca que el receptor recibio el organo

    # Realizar correctamente todo el proceso de asignación y derivación de un organo a un receptor,  contemplando el viaje, la disponibilidad en ese horario de los vehiculos de un centro medico y el tiempo de viaje.
    def iniciarProtocoloTransplanteYTransporte(self, donante: Donante, centroSaludReceptor: CentroDeSalud, organo: Organo):
        donante.centro_de_salud.asignarVehiculo(centroSaludReceptor, organo)
        donante.centro_de_salud.asignarCirujano(organo)
        donante.centro_de_salud.realizarAblacion(organo)

    # Quitar de la lista de donantes a aquellos cuyos organos ya han sido utilizados en su totalidad
    def quitarDonantesSinOrganos(self):
        donante: Donante
        for donante in self.lista_donantes:
            if not donante.lista_organos:
                self.lista_donantes.remove(donante)#elimina de la lista de donantes a quienes ya donaron todos sus organos

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
                pacientesListaEspera.append(receptor)#se lo agrega a la lista de espera que estan en un centro de salud especifico

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


          
    
        