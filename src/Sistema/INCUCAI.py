from src.Personas.donantes import Donante
from src.Personas.paciente import Paciente
from src.Personas.receptor import Receptor
from src.Modelos.organo import Organo
from src.Personas.cirujano import Cirujano
from src.Modelos.CentroDeSalud import CentroDeSalud
import random
from src.Vehiculos.auto import Auto

class INCUCAI:

    def __init__(self):
            """
        Inicializa las listas vacías para donantes, receptores, centros de salud y coincidencias.
        """
            self.lista_donantes=[] 
            
            self.lista_receptores=[]
            self.lista_coincidencia=[]
            self.lista_centro_salud=[]
    
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
        print("   ")
        print("  ")
        print("Registrando Paciente, paciente es :"+str(paciente.get_Nombre()))
        print("  ")
        if not self._estaRegistradoPaciente(paciente):
            if isinstance(paciente, Donante):
                self.lista_donantes.append(paciente)
                print("Buscando receptores")
                self._buscarReceptores(paciente)
               
            else:
                    self.lista_receptores.append(paciente)
                    print("Buscando donantes")
                    donante= self._buscarDonantes(paciente)
                    if donante:
                        print("Cantidad de donantes: "+str(len(self.lista_donantes)))
                        self.lista_donantes.remove(donante)
                        print("Cantidad de donantes luego de la ablacion: "+str(len(self.lista_donantes)))
                    else:
                        print("No hay donantes para ese receptores.")
        else:
            print('El paciente ya fue registrado previamente')
        print("    ")
    
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
            print("====================")
            print("organo del donante: "+str(organo.tipo))
            print("====================")




            for receptor in self.lista_receptores:
                print(f"Organo del receptor: {receptor.get_Organonecesario().tipo}")
                print(f"Receptor sangre: {receptor.getTipo_de_sangre()}")
                print(f"Donante sangre: {donante.getTipo_de_sangre()}")
                print("_______")
                print("es compatible: "+str(self.es_compatible(receptor,donante,organo)))
                if self.es_compatible(receptor,donante,organo):
                    print("  ")   
                    print("Resultado: COINCIDENCIA.") 
                    listaReceptoresParaDonante.append(receptor)
                    print("Se agrega Receptor:"+receptor.get_Nombre())
                    print(" ")
                    print("_________")
                    self.procesar_lista_organos(listaReceptoresParaDonante,donante,organo)
                    
                else:
                    print("Resultado: SIN coincidencia")
                    print(" ")
                    print(" ")
                print("_________")
            print("fin organo: "+str(organo.tipo))

                    
                
        
    def procesar_lista_organos(self,listaReceptoresParaDonante,donante,organo):
        print("Longitud Receptores: "+str(len(listaReceptoresParaDonante)))
        if len(listaReceptoresParaDonante) > 0:
            receptorElegido:Receptor
            receptorElegido = listaReceptoresParaDonante[0]
            for receptor in listaReceptoresParaDonante:
                if receptor.prioridad < receptorElegido.prioridad:
                    print("prioridad del primer receptor en la lista: "+str(receptorElegido.prioridad))
                    print("prioridad del receptor con menor prioridad: "+str(receptor.prioridad))

                    receptorElegido = receptor
                    
                else:
                    if receptor.prioridad == receptorElegido.prioridad:# siempre el bucle primero se compara el receptor con el mismo y despues si en la segunda el primero con el segudno, por eso siempre va aimprimir los dos comentarios con misma fecha de ingreso por qu es el mismo receptor
                        print("posibles receptores en la lista del donante: "+str(receptor.get_Nombre()))
                        print("fecha de ingreso del segundo receptor que hay en la lista: "+str(receptor.get_Fecha_de_ingreso()))
                        print("fecha de ingreso del receptor elegido(el primero): "+str(receptorElegido.get_Fecha_de_ingreso()))
                        receptor.get_Fecha_de_ingreso()< receptorElegido.get_Fecha_de_ingreso()
                        receptorElegido = receptor

            print("Receptor elegido: "+receptorElegido.get_Nombre())
            if receptorElegido is not None:
                self._enviarOrganoAUbicacionReceptor(receptorElegido,donante,organo,receptorElegido.getCentro_de_salud())
                #donante.get_Lista_organos().remove(organo)
                self.quitarDonantesSinOrganos()
                
        else :
            print("No se encontro el Organo, queda en lista de espera")  
            

    def es_compatible(self,receptor: Receptor,donante: Donante, organo :Organo):

        return receptor.getTipo_de_sangre() == donante.getTipo_de_sangre() and organo.tipo==receptor.get_Organonecesario().tipo

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
            for organo in donante.get_Lista_organos():
                if self.es_compatible(receptor,donante,organo):
                    print("Se encontro organo")
                    print("envio del organo...")
                    self._enviarOrganoAUbicacionReceptor(receptor,donante,receptor.get_Organonecesario(),receptor.getCentro_de_salud())
                    donante.get_Lista_organos().remove(receptor.get_Organonecesario())
                    self.quitarDonantesSinOrganos()
                    print("Se removio de la lista de donantes")
                    return donante
        print("fin buscar donantes")
        print(" ")
        return None

            


    def _enviarOrganoAUbicacionReceptor(self, receptor: Receptor, donante: Donante,organo:Organo,centro: CentroDeSalud, ):
        """
        Marca que el receptor recibió un órgano.

        Args:
            receptor (Receptor): Receptor que recibirá el órgano.

        Returns:
            Bool
        """
        print("enviar organo: asignar vehiculo")
        #centro.asignarVehiculo(donante.centro_de_salud,4, 1)
        receptor.__recibioOrgano = True
        
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
        if donante.getCentro_de_salud().get_Direccion() == receptor.getCentro_de_salud().get_Direccion():
            exito=centro.asignar_cirujano(organo)
            print("Operacion exitosa: "+str(exito))
            self.operar(exito,donante,receptor,organo,centro)
            print("Mismo centro de salud no se necesita vehiculo")
            
        else:

            #distancia=random.randint(1, 200)#REVISAR
            nivelTrafico=random.randint(1,10)
            vehiculo_asignado=donante.getCentro_de_salud().asignarVehiculo(centro, nivelTrafico)
            if vehiculo_asignado==None:
                print("No se puede asignar vehiculo por que el tiempo es mayor a 20")
            else:
                if isinstance(vehiculo_asignado,Auto):
                    print("nivel de trafico prueba: "+str(nivelTrafico))
                exito= centro.asignar_cirujano(organo)
                print("Operacion exitosa: "+str(exito))
                self.operar(exito,donante,receptor,organo,centro)
                vehiculo_asignado.desocupar()
                
    
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
            if receptor.getCentro_de_salud() == centroDeSalud:
                pacientesListaEspera.append(receptor)
     

    
    
    
    def operar(self,exito,donante,receptor,organo,centro: CentroDeSalud):
        if exito:
                print("realizar transplante y eliminar de la lista de receptores")
                centro.realizarAblacion(donante,organo)
                print("Cantidad de receptores : "+str(len(self.lista_receptores)))
                self.lista_receptores.remove(receptor)
                print("Cantidad de receptores despues del transplante: "+str(len(self.lista_receptores)))
        else:
                print("No se remueve de la lista de receptores") 
    
    