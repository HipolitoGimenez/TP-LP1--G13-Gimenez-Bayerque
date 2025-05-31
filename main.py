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

#Centros de salud misma provincia y partido
hospital1=CentroDeSalud("Hospital Italiano", "AV Italia 145", "CABA", "Buenos Aires", "84515262385")
hospital2=CentroDeSalud("Hospital Aleman", "AV Italia 145", "CABA", "Buenos Aires", "48545262385")
#Centro de salud distinto partido
hospital3=CentroDeSalud("Hospital Posadas","AV Rivadabia 234","Moron","Buenos Aires","345676543")
#Centro de salud distinta provincia y partido
hospital4=CentroDeSalud("Hospital Central","Av España 23","Capital","Cordoba","7653456787")


#Cirujanos
cirujano1 = Cirujano(
    "Adrian",                     
    "cardiovascular",             
    True,                         
    0,                            
    "12345678",                   
    "1975-06-12",                 
    "M",                          
    "1134567890",                 
    "A+",                         
    "Hospital Italiano",         
    ["corazon"]                   
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

donante1 = Donante("Adriana", "23060432", "02-06-1978", "F", "2494534523", "A+", hospital2,
                   datetime.strptime("02-06-2010", "%d-%m-%Y"),
                   datetime.strptime("02-06-2010 12:00", "%d-%m-%Y %H:%M"))

donante1.cargarOrgano(organocorazon)   
donante1.cargarOrgano(organoPulmon)   



donante2 = Donante("Juan", "25678456", "12-01-1990", "M", "15252523", "B+", hospital1,
                   datetime.strptime("12-01-2025", "%d-%m-%Y"),
                   datetime.strptime("12-01-2025 13:00", "%d-%m-%Y %H:%M"))
donante2.cargarOrgano(organoHuesos)  
donante2.cargarOrgano(organoPiel)  


donante3 = Donante("Marta", "23069832", "02-06-1979", "F", "24921234523", "A+", hospital1,
                   datetime.strptime("02-04-2021", "%d-%m-%Y"),
                   datetime.strptime("02-04-2021 10:30", "%d-%m-%Y %H:%M"))
  
donante3.cargarOrgano(organocorazon)  
donante3.cargarOrgano(organoRiñon) 



donante4 = Donante("Beatriz", "25258425", "12-01-1991", "F", "155452523", "B-", hospital4,
                   datetime.strptime("02-05-2024", "%d-%m-%Y"),
                   datetime.strptime("02-05-2024 09:45", "%d-%m-%Y %H:%M"))
donante4.cargarOrgano(organoHigado)  
donante4.cargarOrgano(organoPancreas)  
donante4.cargarOrgano(organoPulmon)



#Receptores 
receptor1 = Receptor(
    "Lucía", "2345763388", "04-11-2000", "F", "1122334455", "A+", hospital1,
    "corazon",  # Corazón
    "Inestable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Paro cardíaco"
)

receptor2 = Receptor(
    "Claudio", "335555966", "09-06-1999", "M", "1155566685", "A+", hospital2,
    "pulmon",  # Pulmón
    "Estable", datetime.strptime("2025-01-05", "%Y-%m-%d"), 2, "Neumonía"
)


receptor3 = Receptor(
    "Susana", "3145768988", "04-11-2001", "F", "1122334455", "AB+", hospital3,
    "huesos",  # Pulmón
    "Estable", datetime.strptime("2025-02-05", "%Y-%m-%d"), 2, "Neumonía"
)

receptor4 = Receptor(
    "Julieta", "33543366", "09-06-1990", "M", "1155566685", "B+",hospital4 ,
    "riñon",  # Piel
    "Estable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Quemaduras"
)

#vehiculos
ambulancia1=Auto( 120)
helicoptero1=Helicoptero( 300)
avion1 = Avion(600)

ambulancia2=Auto(200)
helicoptero2=Helicoptero(500)
avion2= Avion(100)

ambulancia3=Auto(400)
helicoptero3=Helicoptero(230)
avion3=Avion(500)

ambulancia4=Auto(600)
helicoptero4=Helicoptero(200)
avion4=Avion(100)


hospital1.agregar_receptor(receptor1)
hospital2.agregar_receptor(receptor2)
hospital3.agregar_receptor(receptor3)
hospital4.agregar_receptor(receptor4)
#caso que donantes estan en distintos hospitales o mismo hospital que receptor
hospital1.agregar_donantes(donante1)
hospital2.agregar_donantes(donante2)
hospital3.agregar_donantes(donante3)
hospital4.agregar_donantes(donante4)


#agrego vehiculos a los hospitales
hospital1.agregar_vehiculos(ambulancia1)
hospital1.agregar_vehiculos(helicoptero1)
hospital1.agregar_vehiculos(helicoptero4)
hospital2.agregar_vehiculos(avion1)
hospital2.agregar_vehiculos(avion2)
hospital2.agregar_vehiculos(helicoptero3)
hospital3.agregar_vehiculos(helicoptero2)
hospital3.agregar_vehiculos(ambulancia2)
hospital3.agregar_vehiculos(avion4)
hospital4.agregar_vehiculos(ambulancia4)
hospital4.agregar_vehiculos(ambulancia3)
hospital4.agregar_vehiculos(avion3)


#Agrego cirujanos a los hospitales
hospital1.agregar_cirujano(cirujano1)
hospital2.agregar_cirujano(cirujano2)
hospital3.agregar_cirujano(cirujano3)
hospital3.agregar_cirujano(cirujano4)
hospital4.agregar_cirujano(cirujano5)


#agrego la lista de hospitales cada hospital
hospitales=[]
hospitales.append(hospital1)
hospitales.append(hospital2)
hospitales.append(hospital3)
hospitales.append(hospital4)


#me imprime todos 
for hospital in hospitales:
    print("Cirujanos del Hospital:"+hospital.nombre)
    for cirujano in hospital.cirujanos:
        print (cirujano)
        print(f"_____")
    print("Pacientes del Hospital:"+hospital.nombre)
    for paciente in hospital.pacientes:
        print (paciente)
        print(" ")



#registra donantes y pacientes
incucai = INCUCAI()

incucai.registrarPaciente(receptor1)
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(donante3)
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(receptor3)
incucai.registrarPaciente(receptor4)
incucai.registrarPaciente(donante1)
incucai.registrarPaciente(donante2)
incucai.registrarPaciente(donante3)
incucai.registrarPaciente(donante4)
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(receptor1)

#