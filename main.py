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
cirujano1 = Cirujano(
    "Adrian",                     # nombre
    "cardiovascular",             # especialidad
    True,                         # disponibilidad
    0,                            # cantidad_operaciones
    "12345678",                   # dni
    "1975-06-12",                 # fecha_de_nacimiento
    "M",                          # sexo
    "1134567890",                 # teléfono
    "A+",                         # tipo_de_sangre
    "Hospital Italiano",         # centro_de_salud
    ["corazon"]                   # órganos
)

cirujano2 = Cirujano(
    "Juan",
    "pulmonar",
    True,
    0,
    "48545678",
    "1982-09-30",
    "M",
    "1145678901",
    "B+",
    "Hospital Aleman",
    ["pulmones"]
)

cirujano3 = Cirujano(
    "Estela",
    "plastico",
    True,
    0,
    "31345678",
    "1978-04-22",
    "F",
    "1156789012",
    "AB-",
    "Hospital Italiano",
    ["corneas", "piel"]
)

cirujano4 = Cirujano(
    "Maria",
    "traumatologo",
    False,
    0,
    "22545678",
    "1985-11-05",
    "F",
    "1167890123",
    "O+",
    "Hospital Aleman",
    ["huesos"]
)

cirujano5 = Cirujano(
    "Maria",
    "gastroenterologo",
    True,
    0,
    "33545678",
    "1981-02-18",
    "F",
    "1178901234",
    "A-",
    "Hospital Aleman",
    ["intestino", "riñon", "higado", "pancreas"]
)


#Organos
organo1 = Organo("Corazon")
organo2 = Organo("Corazon")
organo3 = Organo("Corazon")
organo4 = Organo("Corazon")
organo5 = Organo("Pulmon")
organo6 = Organo("Pulmon")
organo7 = Organo("Pulmon")
organo8 = Organo("Pulmon")
organo9 = Organo("Piel")
organo10 = Organo("Piel")
organo11 = Organo("Piel")
organo12 = Organo("Piel")
organo13 = Organo("Corneas")
organo14 = Organo("Corneas")
organo15 = Organo("Corneas")
organo16 = Organo("Corneas")
organo17 = Organo("Huesos")
organo18 = Organo("Huesos")
organo19 = Organo("Huesos")
organo20 = Organo("Huesos")
organo21 = Organo("Intestinos")
organo22 = Organo("Intestinos")
organo23 = Organo("Intestinos")
organo24 = Organo("Intestinos")
organo25 = Organo("Riñón")
organo26 = Organo("Riñón")
organo27 = Organo("Riñón")
organo28 = Organo("Riñón")
organo29 = Organo("Hígado")
organo30 = Organo("Hígado")
organo31 = Organo("Hígado")
organo32 = Organo("Hígado")
organo33 = Organo("Páncreas")
organo34 = Organo("Páncreas")
organo35 = Organo("Páncreas")
organo36 = Organo("Páncreas")

organo1 = Organo("Corazon")  
organo1.fecha_ablacion(datetime.now()) 
organo2 = Organo("Pulmon")  
organo1.fecha_ablacion(datetime.now()) 

#Personas/ donantes

donante1 = Donante("Adriana", "23060432", "02-06-1978", "F", "2494534523", "A+", "Italiano",
                   datetime.strptime("02-06-2010", "%d-%m-%Y"),
                   datetime.strptime("02-06-2010 12:00", "%d-%m-%Y %H:%M"))

donante1.cargarOrgano(organo1)   # Corazón
donante1.cargarOrgano(organo5)   # Pulmón
donante1.cargarOrgano(organo9)   # Piel
donante1.cargarOrgano(organo13)


donante2 = Donante("Juan", "25678456", "12-01-1990", "M", "15252523", "B+", "Aleman",
                   datetime.strptime("12-01-2025", "%d-%m-%Y"),
                   datetime.strptime("12-01-2025 13:00", "%d-%m-%Y %H:%M"))
donante2.cargarOrgano(organo6)  
donante2.cargarOrgano(organo10) 
donante2.cargarOrgano(organo14)  
donante2.cargarOrgano(organo17)  


donante3 = Donante("Marta", "23069832", "02-06-1979", "F", "24921234523", "A-", "Italiano",
                   datetime.strptime("02-04-2021", "%d-%m-%Y"),
                   datetime.strptime("02-04-2021 10:30", "%d-%m-%Y %H:%M"))
donante3.cargarOrgano(organo18)  
donante3.cargarOrgano(organo21)  
donante3.cargarOrgano(organo25) 
donante3.cargarOrgano(organo29)  


donante4 = Donante("Beatriz", "25258425", "12-01-1991", "F", "155452523", "B-", "Aleman",
                   datetime.strptime("02-05-2024", "%d-%m-%Y"),
                   datetime.strptime("02-05-2024 09:45", "%d-%m-%Y %H:%M"))
donante4.cargarOrgano(organo20)  # Huesos
donante4.cargarOrgano(organo24)  # Intestinos
donante4.cargarOrgano(organo33)  # Páncreas
donante4.cargarOrgano(organo29)

#Receptores 
receptor1 = Receptor(
    "Lucía", "2345763388", "04-11-2000", "F", "1122334455", "A+", "hospital_italiano",
    organo1,  # Corazón
    "Inestable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Paro cardíaco"
)

receptor2 = Receptor(
    "Claudio", "335555966", "09-06-1999", "M", "1155566685", "B+", "hospital_aleman",
    organo5,  # Pulmón
    "Estable", datetime.strptime("2025-01-05", "%Y-%m-%d"), 2, "Neumonía"
)

receptor3 = Receptor(
    "Susana", "3145768988", "04-11-2001", "F", "1122334455", "AB+", "hospital_italiano",
    organo6,  # Pulmón
    "Estable", datetime.strptime("2025-02-05", "%Y-%m-%d"), 2, "Neumonía"
)

receptor4 = Receptor(
    "Julieta", "33543366", "09-06-1990", "M", "1155566685", "B+", "hospital_italiano",
    organo9,  # Piel
    "Estable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Quemaduras"
)
#Centros de salud
hospital1=CentroDeSalud("Hospital Italiano", "AV Italia 145", "CABA", "Buenos Aires", "84515262385")
hospital2=CentroDeSalud("Hospital Aleman", "AV Italia 145", "CABA", "Buenos Aires", "48545262385")

ambulancia1=Auto( 120)
helicoptero1=Helicoptero( 300)
avion2 = Avion(600)

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


#auto1 = auto(120)
#avion1 = avion(800)
#helicoptero1=helicoptero(500)
#lista_vehiculos_Hospital_Italiano=[]
print(f"Paciente {receptor1.get_Nombre()} Se encuentra {receptor1.get_Estado()}")
print(cirujano1.operacion())
print(cirujano1) 
print("Se encuentra disponible {cirujano1.}")
print(organo1)##Corre



cirujano_asignado = hospital1.asignar_cirujano(receptor1.organo_necesario)
if cirujano_asignado:
    print(f"El cirujano : {cirujano_asignado.nombre} fue asignado a {receptor1.get_Nombre()}")
else:
    print("No se pudo asignar un cirujano.")



# Asignar cirujano al órgano necesario del receptor
#cirujano_asignado = hospital1.(receptor1.organo_necesario)


#print(f"Vehiculo: Auto Velocidad: {auto1.velocidad}km/h.  Distancia Recorrida: {auto1.distancia} kms")
#print(f"Vehiculo: Avion  Velocidad: {avion1.velocidad}km/h. Distancia Recorrida: {avion1.distancia} kms")
###

# agregar_receptor(self,nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia)
incucai = INCUCAI()
incucai.registrarPaciente(receptor1)
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(receptor3)
incucai.registrarPaciente(receptor4)
incucai.registrarPaciente(donante1)
incucai.registrarPaciente(donante2)
incucai.registrarPaciente(donante3)
incucai.registrarPaciente(donante4)
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(receptor1)
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(donante3)
incucai.registrarPaciente(receptor4)
#incucai.agregar_receptor(receptor1.nombre, receptor1.DNI, receptor1.fecha_de_nacimiento, receptor1.sexo, receptor1.telefono, receptor1.tipo_de_sangre, receptor1.centro_de_salud,receptor1.organo_necesario,receptor1.estado,receptor1.fecha_de_ingreso,receptor1.prioridad,receptor1.patologia)
#incucai.agregar_receptor(receptor2.nombre, receptor2.DNI, receptor2.fecha_de_nacimiento, receptor2.sexo, receptor2.telefono, receptor2.tipo_de_sangre, receptor2.centro_de_salud,receptor2.organo_necesario,receptor2.estado,receptor2.fecha_de_ingreso,receptor2.prioridad,receptor2.patologia)