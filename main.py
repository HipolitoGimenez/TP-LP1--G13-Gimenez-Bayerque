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
    "Hospital Central",
    ["huesos"]
)

cirujano5 = Cirujano(
    "Luz",
    "gastroenterologo",
    True,
    0,
    "33545678",
    "1981-02-18",
    "F",
    "1178901234",
    "A-",
    "Hospital Posadas",
    ["intestino", "riñon", "higado", "pancreas"]
)


#Organos
organocorazon = Organo("corazon")
organoPulmon = Organo("pulmon")
organoPiel = Organo("piel")
organoCorneas = Organo("corneas")
organoHuesos = Organo("huesos")
organoIntestinos = Organo("intestinos")
organoRiñon = Organo("riñón")
organoHigado = Organo("hígado")
organoPancreas = Organo("páncreas")


 
organocorazon.fecha_ablacion(datetime.now()) 
organoPulmon.fecha_ablacion(datetime.now()) 
organoPiel.fecha_ablacion(datetime.now()) 
organoCorneas.fecha_ablacion(datetime.now()) 
organoHuesos.fecha_ablacion(datetime.now()) 
organoIntestinos.fecha_ablacion(datetime.now()) 
organoRiñon.fecha_ablacion(datetime.now()) 
organoHigado.fecha_ablacion(datetime.now()) 
organoPancreas.fecha_ablacion(datetime.now()) 
 

#Personas/ donantes

"""donante1 = Donante("Adriana", "23060432", "02-06-1978", "F", "2494534523", "A+", "Italiano",
                   datetime.strptime("02-06-2010", "%d-%m-%Y"),
                   datetime.strptime("02-06-2010 12:00", "%d-%m-%Y %H:%M"))

donante1.cargarOrgano(organo1)   # Corazón
donante1.cargarOrgano(organo2)   # Pulmón



donante2 = Donante("Juan", "25678456", "12-01-1990", "M", "15252523", "B+", "Aleman",
                   datetime.strptime("12-01-2025", "%d-%m-%Y"),
                   datetime.strptime("12-01-2025 13:00", "%d-%m-%Y %H:%M"))
donante2.cargarOrgano(organo6)  
donante2.cargarOrgano(organo17)  

"""
donante3 = Donante("Marta", "23069832", "02-06-1979", "F", "24921234523", "A+", "Italiano",
                   datetime.strptime("02-04-2021", "%d-%m-%Y"),
                   datetime.strptime("02-04-2021 10:30", "%d-%m-%Y %H:%M"))
  
donante3.cargarOrgano(organocorazon)  
donante3.cargarOrgano(organoRiñon) 



"""donante4 = Donante("Beatriz", "25258425", "12-01-1991", "F", "155452523", "B-", "Aleman",
                   datetime.strptime("02-05-2024", "%d-%m-%Y"),
                   datetime.strptime("02-05-2024 09:45", "%d-%m-%Y %H:%M"))
donante4.cargarOrgano(organo20)  # Huesos
#donante4.cargarOrgano(organo24)  # Intestinos
donante4.cargarOrgano(organo33)  # Páncreas
donante4.cargarOrgano(organo29)"""

#Receptores 
receptor1 = Receptor(
    "Lucía", "2345763388", "04-11-2000", "F", "1122334455", "A+", "hospital_italiano",
    "corazon",  # Corazón
    "Inestable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Paro cardíaco"
)

receptor2 = Receptor(
    "Claudio", "335555966", "09-06-1999", "M", "1155566685", "A+", "hospital_aleman",
    "pulmon",  # Pulmón
    "Estable", datetime.strptime("2025-01-05", "%Y-%m-%d"), 2, "Neumonía"
)
"""

receptor3 = Receptor(
    "Susana", "3145768988", "04-11-2001", "F", "1122334455", "AB+", "hospital_italiano",
    "huesos",  # Pulmón
    "Estable", datetime.strptime("2025-02-05", "%Y-%m-%d"), 2, "Neumonía"
)

receptor4 = Receptor(
    "Julieta", "33543366", "09-06-1990", "M", "1155566685", "B+", "hospital_italiano",
    "riñon",  # Piel
    "Estable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Quemaduras"
)"""
#Centros de salud misma provincia y partido
hospital1=CentroDeSalud("Hospital Italiano", "AV Italia 145", "CABA", "Buenos Aires", "84515262385")
hospital2=CentroDeSalud("Hospital Aleman", "AV Italia 145", "CABA", "Buenos Aires", "48545262385")
#Centro de salud distinto partido
hospital3=CentroDeSalud("Hospital Posadas","AV Rivadabia 234","Moron","Buenos Aires","345676543")
#Centro de salud distinta provincia y partido
hospital4=CentroDeSalud("Hospital Central","Av España 23","Capital","Cordoba","7653456787")

#vehiculos
ambulancia1=Auto( 120)
helicoptero1=Helicoptero( 300)
avion2 = Avion(600)

#hospital1.agregar_donantes(donante1)
hospital1.agregar_receptor(receptor1)#y asi de cada uno hacer

#agrego vehiculos a los hospitales
hospital1.agregar_vehiculos(ambulancia1)
hospital1.agregar_vehiculos(helicoptero1)
hospital2.agregar_vehiculos(avion2)

#Agrego cirujanos a los hospitales
hospital1.agregar_cirujano(cirujano1)
hospital2.agregar_cirujano(cirujano1)

hospitales=[]
hospitales.append(hospital1)
hospitales.append(hospital2)

#me imprime todos 
for hospital in hospitales:
    print("Cirujanos del Hospital:"+hospital.nombre)
    for cirujano in hospital.cirujanos:
        print (cirujano)
        print(f"_____")
    print("Pacientes del Hospital:"+hospital.nombre)
    for paciente in hospital.pacientes:
        print (paciente)

"""print("Cirujanos del Hospital Italiano:")
for c in hospital1.cirujanos:
    print(c)

print(f" ")
print("Pacientes del Hospital Italiano:")
for c in hospital1.paciente:
    print(c)"""

hospital1.agregar_vehiculos(ambulancia1)
hospital2.agregar_vehiculos(helicoptero1)


"""#si coincide hago el procesos
cirujano_asignado = hospital1.asignar_cirujano(receptor1.organo_necesario)
if cirujano_asignado:
    print(f"El cirujano : {cirujano_asignado.nombre} fue asignado a {receptor1.get_Nombre()}")
else:
    print("No se pudo asignar un cirujano.")"""



# Asignar cirujano al órgano necesario del receptor
#cirujano_asignado = hospital1.(receptor1.organo_necesario)


#print(f"Vehiculo: Auto Velocidad: {auto1.velocidad}km/h.  Distancia Recorrida: {auto1.distancia} kms")
#print(f"Vehiculo: Avion  Velocidad: {avion1.velocidad}km/h. Distancia Recorrida: {avion1.distancia} kms")
###

#registra donantes y pacientes
incucai = INCUCAI()
#receptor 1 con donante 3 hay match, receptor 2 con conante 3 no hay match
incucai.registrarPaciente(receptor1)
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(donante3)

"""incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(receptor3)
incucai.registrarPaciente(receptor4)
incucai.registrarPaciente(donante1)
incucai.registrarPaciente(donante2)
incucai.registrarPaciente(donante3)
incucai.registrarPaciente(donante4)
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(receptor1)"""

#