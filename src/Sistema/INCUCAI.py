from src.Personas.donantes import Donante
from src.Personas.paciente import Paciente
from src.Personas.receptor import Receptor
from src.Modelos.coincidencia import Coincidencia
from src.Modelos.organo import Organo
from src.Personas.cirujano import Cirujano
from src.Modelos.CentroDeSalud import CentroDeSalud

class INCUCAI:

    def __init__(self):
            """
        Inicializa las listas vacías para donantes, receptores, centros de salud y coincidencias.
        """
            self.lista_donantes=[] 
            self.lista_centro_salud=[]
            self.lista_receptores=[]
            self.lista_coincidencia=[]
    
    
    def registrarPaciente(self, paciente: Paciente):
        """
        Recibe un objeto paciente (Donante o Receptor).
        Verifica que no esté registrado y lo agrega a la lista correspondiente.
        Busca coincidencias para donantes o receptores.
        
        Args:
            paciente (Paciente): Objeto Donante o Receptor para registrar.

        Returns:
            None
        """
        print("Registrando Paciente")
        if not self._estaRegistradoPaciente(paciente):
            if isinstance(paciente, Donante):
                self.lista_donantes.append(paciente)
                print("Buscando receptores")
                self._buscarReceptores(paciente)
            else:
                self.lista_receptores.append(paciente)
                print("Buscando donantes")
                self._buscarDonantes(paciente)
        else:
            print('El paciente ya fue registrado previamente')

    
    def _estaRegistradoPaciente(self, otroPaciente: Paciente):
        """
        Verifica si un paciente ya está registrado en listas de donantes o receptores.

        Args:
            otroPaciente (Paciente): Paciente a buscar.

        Returns:
            bool: True si está registrado, False si no.
        """
        yaFueRegistrado = False
        for paciente in self.lista_donantes:
            if paciente == otroPaciente:
                return True
            
        for paciente in self.lista_receptores:
            if paciente == otroPaciente:
                return True
        return yaFueRegistrado
        

    def _buscarReceptores(self, donante: Donante):
        
        """
        Busca receptores compatibles para los órganos del donante dado.
        Selecciona el receptor de mayor prioridad y actualiza listas.

        Args:
            donante (Donante): Donante cuyos órganos se evaluarán.

        Returns:
            None
        """
        listaReceptoresParaDonante = []
        print("recorrer lista organos del donante")
        print(" ")
        for organo in donante.get_Lista_organos():
            receptor: Receptor
            for receptor in self.lista_receptores:
                print(f"Receptor: {receptor.organo_necesario}")
                print(f"Organo: {organo.tipo}")
                print(f"Receptor sangre: {receptor.tipo_de_sangre}")
                print(f"Donante sangre: {donante.tipo_de_sangre}")
                print("_______")

                if receptor.organo_necesario == organo.tipo and receptor.tipo_de_sangre == donante.tipo_de_sangre:
                    print("coincidencia")
                    listaReceptoresParaDonante.append(receptor)
                    print("Se agrega Receptor:"+receptor.nombre)
                    print(" ")
                    break
                else:
                    print("sin coincidencia")
                    print(" ")
                    print(" ")
                
        
            print("Longitud Receptores: "+str(len(listaReceptoresParaDonante)))
            if len(listaReceptoresParaDonante) > 0:
                receptorElegido = listaReceptoresParaDonante[0]
                for receptor in listaReceptoresParaDonante:
                    receptor.prioridad < receptorElegido.prioridad
                    receptorElegido = receptor
                print("Receptor elegido: "+receptorElegido.nombre)
                if receptorElegido is not None:
                    self._enviarOrganoAUbicacionReceptor(receptorElegido,donante,organo,receptorElegido.centro_de_salud)
                    donante.get_Lista_organos().remove(organo)
                    self.quitarDonantesSinOrganos()
            else :
                print("No se encontro el Organo, queda en lista de espera")


    def _buscarDonantes(self, receptor: Receptor):
        """
        Busca donantes compatibles para el órgano que necesita el receptor.
        Actualiza listas eliminando órganos asignados.

        Args:
            receptor (Receptor): Receptor que necesita un órgano.

        Returns:
            None
        """
        donante: Donante = None
        for donante in self.lista_donantes:
            if receptor.tipo_de_sangre == donante.tipo_de_sangre and donante.tieneOrgano(receptor.organo_necesario):
                print("Se encontro organo")
                self._enviarOrganoAUbicacionReceptor(receptor,donante,receptor.organo_necesario,receptor.centro_de_salud)
                donante.lista_organos.remove(receptor.organo_necesario)
                print("Se removio de la lista de donantes")
        print("fin buscar donantes")
        print(" ")
            


    def _enviarOrganoAUbicacionReceptor(self, receptor: Receptor, donante: Donante,organo:Organo,centro: CentroDeSalud):
        """
        Marca que el receptor recibió un órgano.

        Args:
            receptor (Receptor): Receptor que recibirá el órgano.

        Returns:
            Bool
        """
        print("enviar organo: asignar vehiculo")
        
        centro.asignarVehiculo(donante.centro_de_salud,4,1)
        
        
        centro.asignarVehiculo(donante.centro_de_salud,4, 1)
        receptor.recibioOrgano = True

    
    def iniciarProtocoloTransplanteYTransporte(self, donante: Donante, centroSaludReceptor: CentroDeSalud, organo: Organo):
        """
        Inicia el proceso de asignación y transporte del órgano desde el donante al receptor.
        Incluye asignación de vehículo y cirujano, y realización de ablación.
        Yo asigno el nivel de trafico y la distancia

        Args:
            donante (Donante): Donante del órgano.
            centroSaludReceptor (CentroDeSalud): Centro de salud del receptor.
            organo (Organo): Órgano a trasplantar.

        Returns:
            None
        """
        distancia=10
        nivelTrafico=1
        centroSaludReceptor.asignarVehiculo(centroSaludReceptor,distancia, nivelTrafico)
        cirujanoCoincide= centroSaludReceptor.asignarCirujano(organo)
        centroSaludReceptor.realizarAblacion(organo)

    
    def quitarDonantesSinOrganos(self):
        """
        Elimina de la lista de donantes aquellos que ya no tienen órganos disponibles.

        Returns:
            None
        """
        donante: Donante
        for donante in self.lista_donantes:
            if not donante.get_Lista_organos():
                self.lista_donantes.remove(donante)

    
    def quitarReceptorConCirugiaExitosa(self):
        """
        Elimina de la lista de receptores aquellos que ya recibieron un órgano.

        Returns:
            None
        """
        receptor: Receptor
        for receptor in self.lista_receptores:
            if receptor.recibioOrgano:
                self.lista_receptores.remove(receptor)

   
    def buscarPacientesListaEsperaPorCentroSalud(self, centroDeSalud):
        """
        Busca receptores en lista de espera asociados a un centro de salud específico.

        Args:
            centroDeSalud (CentroDeSalud): Centro de salud a filtrar.

        Returns:
            list: Lista de receptores en espera en el centro.
        """
        pacientesListaEspera = []
        receptor: Receptor
        for receptor in self.lista_receptores:
            if receptor.centro_de_salud == centroDeSalud:
                pacientesListaEspera.append(receptor)
    

    def buscarPrioridadReceptor(self, receptorBuscado):
        """
        Busca y devuelve la prioridad de un receptor en la lista de espera.

        Args:
            receptorBuscado (Receptor): Receptor a buscar.

        Returns:
            int: Prioridad del receptor o None si no encontrado.
        """
        prioridad: int
        receptor: Receptor
        for receptor in self.lista_receptores:
            if receptor == receptorBuscado:
                return receptor.prioridad
        return prioridad

    
    def listarPacientes(self):
        """
        Imprime la información de los pacientes donantes y receptores registrados.

        Returns:
            None
        """
        for paciente in self.lista_donantes:
            print(paciente)
        for paciente in self.lista_receptores:
            print(paciente)


          
    
        