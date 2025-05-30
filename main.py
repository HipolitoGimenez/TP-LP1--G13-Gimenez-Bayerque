
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


#Personas/ donantes
donante1 = Donante("Adriana", "23060432", "02-06-1978", "F", "2494534523", "A+", "Italiano", "02-06-2010")
donante1.cargarOrgano(organo1)
donante1.cargarOrgano(organo2)
donante1.cargarOrgano(organo3)
donante1.cargarOrgano(organo4)
donante2 = Donante("Juan", "25678456", "12-01-1990", "M", "15252523", "B+", "Aleman", "12-01-2025")
donante2.cargarOrgano(organo6)
donante2.cargarOrgano(organo7)
donante2.cargarOrgano(organo8)
donante2.cargarOrgano(organo9)
donante3 = Donante("Marta", "23069832", "02-06-1979", "F", "24921234523", "A-", "Italiano", "02-04-2021")
donante3.cargarOrgano(organo10)
donante3.cargarOrgano(organo11)
donante3.cargarOrgano(organo12)
donante3.cargarOrgano(organo13)
donante4 = Donante("Beatriz", "25258425", "12-01-1991", "F", "155452523", "B-", "Aleman", "02-05-2024")
donante4.cargarOrgano(organo14)
donante4.cargarOrgano(organo15)
donante4.cargarOrgano(organo16)
donante4.cargarOrgano(organo17)
donante5 = Donante("Carlos", "30060432", "02-06-1985", "M", "2494224523", "AB+", "Italiano","02-03-2025")
donante5.cargarOrgano(organo18)
donante5.cargarOrgano(organo19)
donante5.cargarOrgano(organo20)
donante5.cargarOrgano(organo21)
donante6 = Donante("Romina", "29738456", "12-01-1981", "F", "15252663", "AB-", "Aleman", "12-01-2022")
donante6.cargarOrgano(organo21)
donante6.cargarOrgano(organo22)
donante6.cargarOrgano(organo23)
donante6.cargarOrgano(organo24)
donante7 = Donante("Maricel", "23080232", "02-06-1966", "F", "2492234523", "O+", "Italiano", "02-06-2010")
donante7.cargarOrgano(organo25)
donante7.cargarOrgano(organo26)
donante7.cargarOrgano(organo27)
donante7.cargarOrgano(organo28)
donante8 = Donante("Pedro", "25256056", "12-01-1975", "M", "15255523", "O-", "Aleman", "02-06-2008")
donante8.cargarOrgano(organo29)
donante8.cargarOrgano(organo30)
donante8.cargarOrgano(organo31)
donante8.cargarOrgano(organo32)
donante9 = Donante("Roxana", "23060499", "02-11-1978", "F", "2494566523", "AB+", "Italiano", "02-01-2005")
donante9.cargarOrgano(organo33)
donante9.cargarOrgano(organo34)
donante9.cargarOrgano(organo35)
donante9.cargarOrgano(organo36)

#Receptores
receptor1 = Receptor("Lucía","2345763388","04-11-2000","F","1122334455","A+","Hospital Italiano","Corazón","Inestable","2025-05-05", 1,"Paro cardíaco")
receptor2 = Receptor("Claudio","335555966","09-06-1999","M","1155566685","B+","Hospital Aleman","Pulmon","Estable","2025-01-05", "Alta","Neumonia")
receptor3 = Receptor("Susana","3145768988","04-11-2001","F","1122334455","AB+","Hospital Italiano","Pulmon","Estable","2025-02-05", "Alta","Neumonia")
receptor4 = Receptor("Claudio","33548866","09-06-1997","M","1155566685","B-","Hospital Italiano","Pulmon","Estable","2025-03-05", "Alta","Neumonia")
receptor5 = Receptor("Lorena","2345768922","04-11-2005","F","1122334455","A-","Hospital Italiano","Pulmon","Estable","2025-04-05", "Alta","Neumonia")
receptor6 = Receptor("Julieta","33543366","09-06-1990","M","1155566685","B+","Hospital Italiano","Piel","Estable","2025-05-05", "Alta","Quemaduras")
receptor7 = Receptor("Martin","2345768977","04-11-2009","F","1122334455","AB-","Hospital Italiano","Riñón","Inestable","2025-06-05", 1,"Insuficiencia renal")
receptor8 = Receptor("Jose","38845966","09-06-1999","M","1155566685","B+","Hospital Aleman","Pulmon","Inestable","2025-05-15", 1,"Neumonia")
receptor9 = Receptor("Edgar","2345766988","04-11-2007","F","1122334455","O+","Hospital Aleman","Corazón","Estable","2025-05-25", "Alta","Insuficiencia cardiaca")
receptor10 = Receptor("Marianela","33225966","09-06-1988","M","1155566685","O-","Hospital Aleman","Hígado","Inestable","2025-05-12", 1,"Cirrosis")
receptor11 = Receptor("Luciana","2345764488","04-11-2010","F","1122334455","A+","Hospital Aleman","Hígado","Inestable","2025-04-14", 1,"Cirrosis")
receptor12 = Receptor("Josefina","33541166","09-06-1972","M","1155566685","AB+","Hospital Aleman","Pulmon","Estable","2025-04-11", "Alta","Neumonia")
receptor13 = Receptor("Marcelo","2995768988","04-11-2003","F","1122334455","AB-","Hospital Aleman","Páncreas","Inestable","2025-12-29", 1,"Pancreatitis")
receptor14 = Receptor("Alejandro","33533966","09-06-1995","M","1155566685","A-","Hospital Aleman","Páncreas","Estable","2025-12-02", "Alta","Pancreatitis")
receptor15 = Receptor("Rodrigo","2345769988","04-11-2008","F","1122334455","A+","Hospital Italiano","Páncreas","Estable","2025-06-27", "Alta","Pancreatitis")
receptor16 = Receptor("Monica","33225966","09-06-1999","M","1155566685","B-","Hospital Aleman","Pulmon","Inestable","2025-02-28", 1,"Neumonia")
receptor17 = Receptor("Cintia","2345773988","04-11-2000","F","1122334455","AB+","Hospital Italiano","Intestinos","Estable","2025-07-26", "Alta","Obstruccion intestinal")
receptor18 = Receptor("Alan","33545496","09-06-1974","M","1155566685","B-","Hospital Aleman","Pulmon","Intestinos","2025-05-30", "Alta","Neumonia")
receptor19 = Receptor("Justina","2345168988","09-12-2009","F","1122334455","AB+","Hospital Italiano","Huesos","Inestable","2025-01-31", 1,"Fractura")
receptor20 = Receptor("Patricia","33529966","09-06-1968","M","1155566685","AB-","Hospital Aleman","Huesos","Inestable","2025-10-12", 1,"Pulverizacion osea")

#Organos
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





