
from datetime import datetime
from src.Modelos.CentroDeSalud import CentroDeSalud
from src.Modelos.organo import Organo
from src.Modelos.tipoOrganoEnum import TipoOrganoEnum
from src.Modelos.viaje import Viaje

from src.Personas.paciente import Paciente
from src.Personas.receptor import Receptor
from src.Personas.donantes import Donante
from src.Personas.cirujano import Cirujano

from src.Sistema.INCUCAI import INCUCAI

from src.Vehiculos.auto import Auto
from src.Vehiculos.avion import Avion
from src.Vehiculos.helicoptero import Helicoptero
from src.Vehiculos.vehiculo import Vehiculo


#Cirujanos
cirujano1 = Cirujano( "Adrian","cardiovascular",True,0,"12345678","1980-01-01","masculino","1122334455","A+","Hospital Italiano", "[Corazon]")
cirujano2 = Cirujano( "Juan","Pulmonar",True,0,"48545678","1975-06-11","masculino","114434455","B+","Hospital Aleman", "[Pulmones]")


#Personas/ donantes
persona1 = Paciente("Adriana", "23060432", "02-06-1978", "F", "2494534523", "A+", "Italiano")
persona2 = Paciente("Juan", "25258456", "12-01-1994", "M", "15252523", "B+", "Aleman")

#Receptores
receptor1 = Receptor("Lucía","2345768988","04-11-2000","F","1122334455","A+","Hospital Italiano","Corazón","Estable","2025-05-05", "Alta","Paro cardíaco")
receptor2= Receptor("Claudio","33545966","09-06-1999","M","1155566685","B+","Hospital Aleman","Pulmon","Estable","2025-05-05", "Alta","Neumonia")

#Organos
organo1 = Organo("Corazon")  
organo1.fecha_ablacion(datetime.now()) 
organo2 = Organo("Pulmon")  
organo1.fecha_ablacion(datetime.now()) 

#Centros de salud
hospital1=CentroDeSalud("Hospital Italiano", "AV Italia 145", "CABA", "Buenos Aires", "84515262385")
hospital2=CentroDeSalud("Hospital Aleman", "AV Italia 145", "CABA", "Buenos Aires", "48545262385")

#vehiculos
ambulancia1=Auto( 120)
helicoptero1=Helicoptero( 300)
avion2 = Avion(600)

#agrego vehiculos a los hospitales
hospital1.agregar_vehiculos(ambulancia1)
hospital1.agregar_vehiculos(helicoptero1)
hospital2.agregar_vehiculos(avion2)

#Agrego cirujanos a los hospitales
hospital1.agregar_cirujano(cirujano1)
hospital2.agregar_cirujano(cirujano1)

print("Cirujanos del Hospital Italiano:")
for c in hospital1.cirujanos:
    print(c)

hospital1.agregar_vehiculos(ambulancia1)
hospital2.agregar_vehiculos(helicoptero1)


#lista_vehiculos_Hospital_Italiano=[]
print(f"Paciente {receptor1.nombre} Se en cuentra{ receptor1.estado}")
print(cirujano1.operacion())
print(cirujano1) 
print("Se encuentra disponible {cirujano1.}")
print(organo1)


cirujano_asignado = hospital1.asignar_cirujano(receptor1.organo_necesario)
if cirujano_asignado:
    print(f"El cirujano : {cirujano_asignado.nombre} fue asignado a {receptor1.nombre}")
else:
    print("No se pudo asignar un cirujano.")




incucai = INCUCAI()
incucai.registrarPaciente(Receptor(receptor1.nombre, receptor1.DNI, receptor1.fecha_de_nacimiento, receptor1.sexo, receptor1.telefono, receptor1.tipo_de_sangre, receptor1.centro_de_salud,receptor1.organo_necesario,receptor1.estado,receptor1.fecha_de_ingreso,receptor1.prioridad,receptor1.patologia))
incucai.registrarPaciente(Receptor(receptor2.nombre, receptor2.DNI, receptor2.fecha_de_nacimiento, receptor2.sexo, receptor2.telefono, receptor2.tipo_de_sangre, receptor2.centro_de_salud,receptor2.organo_necesario,receptor2.estado,receptor2.fecha_de_ingreso,receptor2.prioridad,receptor2.patologia))




