from datetime import datetime
from typing import List
from src.Vehiculos.auto import Auto
from src.Vehiculos.avion import Avion
from src.Vehiculos.helicoptero import Helicoptero
from src.Vehiculos.vehiculo import Vehiculo
from src.Personas.cirujano import Cirujano

class CentroDeSalud:
    def __init__(self, nombre: str, direccion: str, partido: str, provincia: str, telefono: str):
        """
        Inicializa un centro de salud con sus datos principales.
        Crea listas vacías para cirujanos y vehículos, e inicializa el contador de trasplantes realizados.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono
        self.cirujanos = []  
        self.vehiculos = []  
        self.transplante_realizado = 0 

    
    def agregar_vehiculos(self, vehiculo):
        """
        Recibe: un objeto Vehiculo.
        Hace: lo agrega a la lista de vehículos del centro.
        Devuelve: nada.
        """
        self.vehiculos.append(vehiculo)


    def agregar_cirujano(self, nuevo_cirujano: Cirujano):  
        """
        Recibe: un objeto Cirujano.
        Hace: lo agrega a la lista de cirujanos del centro.
        Devuelve: nada.
        """     
        self.cirujanos.append(nuevo_cirujano)


    def asignar_cirujano(self, organo_necesario):
      """
        Recibe: un objeto Organo.
        Hace: busca un cirujano disponible y especializado en el tipo de órgano necesario.
              Si lo encuentra, lo marca como ocupado y lo devuelve.
        Devuelve: el cirujano asignado o None si no hay uno disponible.
        """
      if not self.cirujanos:
        print("No hay cirujanos registrados.")
        return None

      for i in range(len(self.cirujanos)):
        ciru = self.cirujanos[i]  
        if ciru.disponibilidad and ciru.es_especialista(organo_necesario):
            ciru.ocupado()
            print(f"Cirujano asignado: {ciru.nombre} para el órgano {organo_necesario}")
            return ciru

        print(f"No se encontró cirujano disponible para el órgano {organo_necesario}")
        return None


    def asignarVehiculo(self, otroCentroSalud, distancia, nivelTrafico):
        """
        Recibe: otro CentroDeSalud, una distancia (float/int), y un nivel de tráfico (str/int).
        Hace: elige un tipo de vehículo apropiado (Auto, Helicóptero, Avión) según la ubicación del otro centro,
              y lo usa para transportar el órgano.
        Devuelve: nada.
        """
        if(self._estanEnLaMismaProvinciaYPartido(otroCentroSalud)):
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Auto'), distancia, nivelTrafico)
        elif (self._estanEnMismaProvincia(otroCentroSalud)):
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Helicoptero'), distancia, nivelTrafico)
        else:
           self.transportarOrgano(otroCentroSalud, self._obtenerVehiculo('Avion'), distancia, nivelTrafico)


    def _estanEnLaMismaProvinciaYPartido(self, otroCentroSalud):
       """
        Recibe: otro CentroDeSalud.
        Hace: compara provincia y partido entre ambos centros.
        Devuelve: True si están en el mismo partido y provincia, False si no.
        """
       return self.provincia == otroCentroSalud.provincia and self.partido == otroCentroSalud.partido
    

    def _estanEnMismaProvincia(self, otroCentroSalud):
       """
        Recibe: otro CentroDeSalud.
        Hace: compara solo la provincia entre ambos centros.
        Devuelve: True si están en la misma provincia, False si no.
        """
       return self.provincia == otroCentroSalud.provincia
    

    def transportarOrgano(self, vehiculo, distancia, nivelTrafico):
       """
        Recibe: un objeto Vehiculo, una distancia y un nivel de tráfico.
        Hace: asigna esos valores al vehículo y registra el viaje con destino al centro de salud actual.
        Devuelve: nada.
        """
       vehiculo.distancia = distancia
       vehiculo.nivelTrafico = nivelTrafico
       vehiculo.registrar_viaje(self.direccion)
    
    def _obtenerVehiculo(self, tipo):
       """
        Recibe: un string que indica el tipo de vehículo ('Auto', 'Avion', 'Helicoptero').
        Hace: busca el primer vehículo disponible del tipo especificado, lo marca como ocupado.
        Devuelve: el vehículo encontrado o None si no hay disponible.
        """
       vehiculoAsignado = None
       for vehiculo in self.vehiculos:
          if tipo == vehiculo.get_class_name() and not vehiculo.ocupado():
            vehiculo.ocupar()
            vehiculoAsignado = vehiculo
            break
       return vehiculoAsignado
    

    def asignarCirujano(self):
        """
        (Método incompleto)
        Recorre la lista de cirujanos y verifica si hay alguno disponible.
        Actualmente no hace nada más. Podés eliminarlo o completarlo.
        """
        for cirujano in self.cirujanos:
           if cirujano.estaDisponible():
              pass


    def realizarAblacion(self, donante, organo):
        """
        Recibe: un objeto Donante y un objeto Organo.
        Hace: registra la fecha y hora de ablación del órgano y lo quita de la lista del donante.
        Devuelve: nada.
        """
        organo.fecha_hora_de_ablacion = datetime.now()
        donante.lista_organos.remove(organo)


    def realizarTrasplante(self, vehiculo):
        """
        (Método aún no implementado)
        Recibe: un objeto Vehiculo.
        Hace: (pendiente por definir la lógica del trasplante y actualización de estado).
        """
        pass

    def __eq__(self, otroCentroSalud): 
        """
        Recibe: otro objeto CentroDeSalud.
        Hace: compara nombre y dirección entre ambos objetos.
        Devuelve: True si ambos centros son considerados iguales, False si no.
        """
        return self.nombre == otroCentroSalud.nombre and self.direccion == otroCentroSalud.direccion 


   
 


        
        




    