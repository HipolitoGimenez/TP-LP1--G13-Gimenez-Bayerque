
from donantes import Donante
from paciente import Paciente
from receptor import Receptor
from coincidencia import Coincidencia
from organo import Organo
from cirujano import Cirujano
from centro_de_salud import CentroDeSalud

class INCUCAI:

    def __init__(self):
             #listas vacias y luego voy agregando
             self.lista_donantes=[] # en el main tengo todos los datos pero el incucai agrega entonces lo invoco en el main
             self.lista_centro_salud=[]
             self.lista_receptores=[]
             self.lista_coincidencia=[]
    
    
    #  Registrar pacientes nuevos (Validando que no se encuentre en otra lista ni se repita).
    def registrarPaciente(self, paciente: Paciente):

        if not self._estaRegistradoPaciente(paciente):
            if isinstance(paciente, Donante):
                self.lista_donantes.append(paciente)
                self._buscarReceptores(paciente)
            else:
                self.lista_receptores.append(paciente)
                self._buscarDonantes(paciente)
        else:
            print('El paciente ya fue registrado previamente')

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
        listaReceptoresParaDonante = []
        for organo in donante.lista_organos:
            receptor: Receptor
            for receptor in self.lista_receptores:
                if receptor.organo_necesario.tipo == organo.tipo and receptor.tipo_de_sangre == donante.tipo_de_sangre:
                    listaReceptoresParaDonante.append(receptor)
        
            receptorElegido = listaReceptoresParaDonante.index(0)
            for receptor in listaReceptoresParaDonante:
                receptor.prioridad < receptorElegido.prioridad # Esto se pudo hacer por la funcion __lt__
                receptorElegido = receptor
            if receptorElegido is not None:
                self._enviarOrganoAUbicacionReceptor(receptorElegido)
                donante.lista_organos.remove(organo)

    def _buscarDonantes(self, receptor: Receptor):
        donante: Donante = None
        for donante in self.lista_donantes:
            if receptor.tipo_de_sangre == donante.tipo_de_sangre and donante.tieneOrgano(receptor.organo_necesario):
                self._enviarOrganoAUbicacionReceptor(receptor)
                donante.lista_organos.remove(receptor.organo_necesario)

    def _enviarOrganoAUbicacionReceptor(self, receptor: Receptor):
        receptor.recibioOrgano = True

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


          
    
        