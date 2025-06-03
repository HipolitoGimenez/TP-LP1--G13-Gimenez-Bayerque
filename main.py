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
hospital2=CentroDeSalud("Hospital Aleman", "AV Italia 200", "CABA", "Buenos Aires", "48545262385")
#Centro de salud distinto partido
hospital3=CentroDeSalud("Hospital Posadas","AV Rivadabia 234","Moron","Buenos Aires","345676543")
#Centro de salud distinta provincia y partido y me sirve para cirujano no especializado tambien
hospital4=CentroDeSalud("Hospital Central","Av España 23","Capital","Cordoba","7653456787")
#Centro de salud mismo receptor y donante
hospital5 = CentroDeSalud("Hospital Regional", "Calle San Martín 1025", "Godoy Cruz", "Mendoza", "2614345678")
hospital6 = CentroDeSalud("Hospital Uruguay", "Boulevard Oroño 1500", "Rosario", "Santa Fe", "3416789012")
hospital7 = CentroDeSalud("Hospital San Juan de Dios", "Av. San Martín 456", "La Plata", "Buenos Aires", "2214567890")
hospital8 = CentroDeSalud("Hospital El Cruce","Camino General Belgrano 5400","Florencio Varela","Buenos Aires","1144556677")
hospital9 = CentroDeSalud("Hospital Ramón Carrillo","Ruta 3 Km 1100","San Luis","San Luis","2664001234")
hospital10 = CentroDeSalud("Hospital de Clínicas","Av. Córdoba 2351","Recoleta","CABA","1147891234")




#Cirujanos hospital1 Italiano
cirujanoG5 = Cirujano(
    "Adrian",                     
    "gastroenterologo",             
    True,                         
    0,                            
    "12345678",                   
    "1975-06-12",                 
    "M",                          
    "1134567890",                 
    "A+",                         
    "Hospital Italiano",         
    ["intestino", "riñon", "higado", "pancreas"]                   
)
cirujanoC3 = Cirujano(
    "Fausto",             # nombre
    "cardiovascular",                     # especialidad
    True,                           # disponible
    0,                              # operaciones realizadas hoy
    "40332011",                     # DNI
    "1972-04-05",                   # fecha de nacimiento
    "M",                            # sexo
    "1165427090",                   # teléfono
    "A+",                           # tipo de sangre
    "Hospital Italiano",      # centro de salud
    ["corazon"]                      # órganos compatibles
)

cirujanoPL2 = Cirujano(
    "Gaston",
    "plastico",
    True,
    0,
    "334455672",
    "1978-09-05",
    "M",
    "1122333455",
    "B+",
    "Hospital Italiano",
    ["corneas", "piel"]
)

#cirujanos hospital2 Aleman
cirujanoPU1 = Cirujano(
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
    ["pulmon"]
)
cirujanoC4=Cirujano(
    "Juana",
    "cardiovascular",
    True,
    0,
    "48542678",
    "1982-07-30",
    "F",
    "1145678901",
    "O+",
    "Hospital Aleman",
    ["corazon"]
)
cirujanoPL3=Cirujano(
    "Justo",
    "plastico",
    True,
    0,
    "48545698",
    "1982-09-20",
    "M",
    "1142678901",
    "AB+",
    "Hospital Aleman",
    ["corneas","piel"]
)

#cirujano hospital3 Hospital Posadas
cirujanoPL1 = Cirujano(
    "Estela",
    "plastico",
    True,
    0,
    "31345678",
    "1978-04-22",
    "F",
    "1156789012",
    "AB-",
    "Hospital Posadas",
    ["corneas", "piel"]
)

cirujanoT = Cirujano(
    "Maria",
    "traumatologo",
    True,
    0,
    "22545678",
    "1985-11-05",
    "F",
    "1167890123",
    "O+",
    "Hospital Posadas",
    ["huesos"]
)

cirujanoPU4=Cirujano(
    "Marcos",
    "pulmonar",
    True,
    0,
    "22555678",
    "1985-11-05",
    "M",
    "1167190123",
    "O+",
    "Hospital Posadas",
    ["pulmones"]
)

cirujanoG4=Cirujano(
    "Mario",
    "gastroenterologo",
    True,
    0,
    "22545678",
    "1985-11-05",
    "M",
    "1167890123",
    "O-",
    "Hospital Posadas",
    ["intestino", "riñon", "higado", "pancreas"]
)
cirujanoC1=Cirujano(
    "Mariana",
    "cardiovascular",
    True,
    0,
    "22545670",
    "1985-01-05",
    "F",
    "1167890323",
    "O-",
    "Hospital Posadas",
    ["corazon"]
)

#cirujanos de hospital4 hospital Central
cirujanoT1 = Cirujano(
    "Luz",
    "traumatologo",
    True,
    0,
    "33545678",
    "1981-02-18",
    "F",
    "1178901234",
    "A-",
    "Hospital Central",
    ["huesos"]
)

#cirujanos de hospital5 hospital Regional
cirujanoG1 = Cirujano(
    "Martín",
    "gastroenterologo",
    True,
    0,
    "33445566",
    "1978-09-05",
    "M",
    "1122334455",
    "AB+",
    "Hospital Regional",
    ["intestino", "riñon", "higado", "pancreas"]
)
cirujanoG6 = Cirujano(
    "Marcos",
    "gastroenterologo",
    True,
    0,
    "33445466",
    "1978-09-15",
    "M",
    "1122334455",
    "B-",
    "Hospital Regional",
    ["intestino", "riñon", "higado", "pancreas"]
)

#cirujanos de hospital6 hospital Uruguay
cirujanoG2 = Cirujano(
    "Hipolito",
    "gastroenterologo",
    True,
    0,
    "33445566",
    "1978-09-05",
    "M",
    "1122334455",
    "B+",
    "Hospital Uruguay",
    ["intestino", "riñon", "higado", "pancreas"]
)
cirujanoC5= Cirujano(
    "Horasio",
    "cardiovascular",
    True,
    0,
    "33445566",
    "1978-09-05",
    "M",
    "1122334455",
    "B+",
    "Hospital Uruguay",
    ["corazon"]
)

#cirujanos de hospital7 Hospital San Juan
cirujanoG3 = Cirujano(
    "Gabriela",                     
    "gastroenterologo",             
    False,                          
    1,                              
    "55667788",                     
    "1980-03-22",                   
    "F",                            
    "1176543210",                   
    "O+",                           
    "Hospital San Juan",           
    ["intestino", "riñon", "higado", "pancreas"]  
)

#cirujanos hospital8 Hospital el Cruce
cirujanoG7 = Cirujano(
    "Gabriel",                     
    "gastroenterologo",             
    True,                          
    0,                              
    "55667788",                     
    "1980-03-22",                   
    "M",                            
    "1176543210",                   
    "A+",                           
    "Hospital el Cruce",           
    ["intestino", "riñon", "higado", "pancreas"]  
)

#cirujanos hospital9 Hospital Ramon Carillo
cirujanoPU2 = Cirujano(
    "Federico",             # nombre
    "pulmonar",                     # especialidad
    True,                           # disponible
    0,                              # operaciones realizadas hoy
    "40332211",                     # DNI
    "1977-04-05",                   # fecha de nacimiento
    "M",                            # sexo
    "1165437890",                   # teléfono
    "B-",                           # tipo de sangre
    "Hospital Ramón Carrillo",      # centro de salud
    ["pulmon"]                      # órganos compatibles
)

#cirujanos hospital10 Hospital de clinicas
cirujanoPL4 = Cirujano(
    "Francisco",             # nombre
    "plastico",                     # especialidad
    True,                           # disponible
    0,                              # operaciones realizadas hoy
    "40332011",                     # DNI
    "1978-04-05",                   # fecha de nacimiento
    "M",                            # sexo
    "1165477890",                   # teléfono
    "B+",                           # tipo de sangre
    "Hospital de Clinicas",      # centro de salud
    ["corneas","piel"]                      # órganos compatibles
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
  

donante2 = Donante("Juan", "25678456", "12-01-1990", "M", "15252523", "B+", hospital3,
                   datetime.strptime("12-01-2025", "%d-%m-%Y"),
                   datetime.strptime("12-01-2025 13:00", "%d-%m-%Y %H:%M"))
donante2.cargarOrgano(organoPulmon)  


donante3 = Donante("Marta", "23069832", "02-06-1979", "F", "24921234523", "AB+", hospital4,
                   datetime.strptime("02-04-2021", "%d-%m-%Y"),
                   datetime.strptime("02-04-2021 10:30", "%d-%m-%Y %H:%M"))
  
donante3.cargarOrgano(organoHuesos)  


donante4 = Donante("Valeria", "25258425", "12-01-1991", "F", "155452523", "B-", hospital1,
                   datetime.strptime("02-05-2024", "%d-%m-%Y"),
                   datetime.strptime("02-05-2024 09:45", "%d-%m-%Y %H:%M"))  
donante4.cargarOrgano(organoRiñon)


donante5=Donante("Josefa","123456543","03-02-1999","F","1234453234","B+",hospital5,
                 datetime.strptime("02-05-2025","%d-%m-%Y"),
                 datetime.strptime("02-05-2025 12:37","%d-%m-%Y %H:%M"))
donante5.cargarOrgano(organoIntestinos)


donante6=Donante("Diego","123678543","03-02-1999","M","1234453324","O+",hospital2,
                 datetime.strptime("02-06-2025","%d-%m-%Y"),
                 datetime.strptime("02-06-2025 12:37","%d-%m-%Y %H:%M"))
donante6.cargarOrgano(organoPiel)


donante7=Donante("Bianca","23454321","08-12-2001","F","1234453324","A+", hospital10,
                 datetime.strptime("02-06-2025","%d-%m-%Y"),
                 datetime.strptime("02-06-2025 12:37","%d-%m-%Y %H:%M"))
donante7.cargarOrgano(organoCorneas)


donante8=Donante("Gonsalo","23454321","08-12-2006","M","1234453324","AB+", hospital3,
                 datetime.strptime("02-06-2025","%d-%m-%Y"),
                 datetime.strptime("02-06-2025 11:37","%d-%m-%Y %H:%M"))
donante8.cargarOrgano(organoPancreas)
donante8.cargarOrgano(organocorazon)


donante9=Donante("Tomas","23432123","09-12-2000","M","123456543","O-",hospital6,
                datetime.strptime("02-06-2025","%d-%m-%Y"),
                datetime.strptime("02-06-2025 10:37","%d-%m-%Y %H:%M"))
donante9.cargarOrgano(organoHigado)


donante10=Donante("Estela","234678123","09-12-2001","F","123457843","AB-",hospital9,
                datetime.strptime("02-06-2025","%d-%m-%Y"),
                datetime.strptime("02-06-2025 10:37","%d-%m-%Y %H:%M"))#la ablacion fue dos dias despues no se debe realizar
donante10.cargarOrgano(organoPulmon)



#Receptores 
receptor1 = Receptor(
    "Lucía", "2345763388", "04-11-1975", "F", "1122334455", "A+", hospital1,
    organocorazon,  
    "Estable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Paro cardíaco"
)

receptor2 = Receptor(
    "Claudio", "335555966", "09-06-1999", "M", "1155566685", "B+", hospital2,
    organoPulmon,  
    "Estable", datetime.strptime("2025-01-05", "%Y-%m-%d"), 2, "Neumonía"
)


receptor3 = Receptor(
    "Susana", "3145768988", "04-11-1980", "F", "1122334455", "AB+", hospital3,
    organoHuesos,  
    "Estable", datetime.strptime("2025-02-05", "%Y-%m-%d"), 2, "Osteosarcoma"
)

receptor4 = Receptor(
    "Julieta", "33543366", "09-06-1990", "F", "1155566685", "B-",hospital4 ,
    organoRiñon,  
    "Estable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Insuficiencia renal crónica termina"
)


receptor5 = Receptor(
    "Martina", "33543466", "09-12-2002", "F", "1155566635", "B+",hospital5 ,
    organoIntestinos,  
    "Estable", datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Sidrome de Intestino corto"
)

receptor6 = Receptor(
    "Roberto","40123456","1992-06-15","M","1167891234","O+",hospital4,
    organoPiel,
    "Estable", datetime.strptime("2025-05-20", "%Y-%m-%d" ), 3, "Quemaduras de tercer grado"
)

receptor7=Receptor(
    "Lucas","40156987","1992-12-08","M","1167891234","O+",hospital3,
    organoPiel,
    "Estable",datetime.strptime("2025-04-20","%Y-%m-%d" ),3,"Quemaduras de tercer grado"
)

receptor8 = Receptor(
    "Luciana", "2345789388", "2000-12-04", "F",  "1122309455", "A+",  hospital1,
    organoCorneas,  
    "Estable", 
    datetime.strptime("2025-05-05", "%Y-%m-%d"), 1, "Ceguera por queratopatía bullosa"
)

receptor9 = Receptor(
    "Rosario", "2788899911", "1995-03-12", "F", "1133445566", "A+", hospital10,
    organoCorneas,  
    "Estable", 
    datetime.strptime("2025-05-12", "%Y-%m-%d"),3, "Queratomalacia por deficiencia de vitamina A"
)

receptor10=Receptor(
    "Guido","34567264","2004-07-12","M","1123433215","AB+",hospital6,
    organocorazon,
    "Estable",
    datetime.strptime("2025-05-12", "%Y-%m-%d"),2, "Insuficiencia Cardiaca"
)

receptor11=Receptor(
    "Manuel","45678765","2001-09-21","M","1133445566","AB+",hospital7,
    organoPancreas,
    "Estable",
    datetime.strptime("2025-06-01", "%Y-%m-%d"),2, "Pancreatitis autoinmune avanzada"
)

receptor12=Receptor(
    "Valentino","45678765","1997-09-21","M","1133445566","O-",hospital8,
    organoHigado,
    "Estable",
    datetime.strptime("2025-06-01", "%Y-%m-%d"),2, "Hepatitis fulminante"
)

receptor13=Receptor("Marina","45678265","2000-09-21","M","1133445566","AB-",hospital10,
    organoPulmon,
    "Estable",
    datetime.strptime("2025-06-01", "%Y-%m-%d"),2, "Fibrosis"
)



#vehiculos
ambulancia1=Auto(120)
helicoptero1=Helicoptero(550)
avion1 = Avion(600)

ambulancia2=Auto(200)
helicoptero2=Helicoptero(500)
avion2= Avion(600)

ambulancia3=Auto(400)
helicoptero3=Helicoptero(400)
avion3=Avion(500)

ambulancia4=Auto(600)
helicoptero4=Helicoptero(450)
avion4=Avion(550)

ambulancia5=Auto(300)
ambulancia6=Auto(390)
avion5=Avion(500)

ambulancia7=Auto(300)
ambulancia8=Auto(390)
avion6=Avion(500)
avion7=Avion(500)
avion8=Avion(500)
avion9=Avion(500)
ambulancia9=Auto(390)
ambulancia10=Auto(390)
ambulancia11=Auto(390)
helicoptero5=Helicoptero(450)
helicoptero6=Helicoptero(450)
helicoptero7=Helicoptero(450)
avion10=Avion(1100)
helicoptero8=Helicoptero(451)
helicoptero9=Helicoptero(450)
ambulancia12=Auto(400)
avion11=Avion(500)


hospital1.agregar_receptor(receptor1)
hospital1.agregar_receptor(receptor8)

hospital2.agregar_receptor(receptor2)

hospital3.agregar_receptor(receptor3)
hospital3.agregar_receptor(receptor7)

hospital4.agregar_receptor(receptor4)
hospital4.agregar_receptor(receptor6)

hospital5.agregar_receptor(receptor5)

hospital6.agregar_receptor(receptor10)

hospital7.agregar_receptor(receptor11)

hospital8.agregar_receptor(receptor12)

hospital10.agregar_receptor(receptor13)
hospital10.agregar_receptor(receptor9)

#caso que donantes estan en distintos hospitales o mismo hospital que receptor
hospital1.agregar_donantes(donante4)

hospital2.agregar_donantes(donante1)
hospital2.agregar_donantes(donante6)

hospital3.agregar_donantes(donante2)
hospital3.agregar_donantes(donante8)

hospital4.agregar_donantes(donante3)

hospital5.agregar_donantes(donante5)

hospital6.agregar_donantes(donante9)

hospital9.agregar_donantes(donante10)

hospital10.agregar_donantes(donante7)



#agrego vehiculos a los hospitales
hospital1.agregar_vehiculos(ambulancia1)
hospital1.agregar_vehiculos(helicoptero1)
hospital1.agregar_vehiculos(helicoptero4)
hospital1.agregar_vehiculos(avion5)


hospital2.agregar_vehiculos(avion2)
hospital2.agregar_vehiculos(helicoptero3)
hospital2.agregar_vehiculos(ambulancia5)#hospital que uso en el primer caso debe utilizar la ambulancia 4 que es la de mayor velocidad
hospital2.agregar_vehiculos(ambulancia6)
hospital2.agregar_vehiculos(ambulancia4)

hospital3.agregar_vehiculos(helicoptero2)
hospital3.agregar_vehiculos(ambulancia2)
hospital3.agregar_vehiculos(avion4)

hospital4.agregar_vehiculos(ambulancia3)
hospital4.agregar_vehiculos(avion3)

hospital5.agregar_vehiculos(ambulancia5)
hospital5.agregar_vehiculos(ambulancia7)
hospital5.agregar_vehiculos(avion6)

hospital6.agregar_vehiculos(avion7)
hospital6.agregar_vehiculos(ambulancia8)
hospital6.agregar_vehiculos(helicoptero5)

hospital7.agregar_vehiculos(avion8)
hospital7.agregar_vehiculos(ambulancia9)
hospital7.agregar_vehiculos(helicoptero6)

hospital8.agregar_vehiculos(avion9)
hospital8.agregar_vehiculos(ambulancia10)
hospital8.agregar_vehiculos(helicoptero7)

hospital9.agregar_vehiculos(avion10)
hospital9.agregar_vehiculos(ambulancia11)
hospital9.agregar_vehiculos(helicoptero8)

hospital10.agregar_vehiculos(avion11)
hospital10.agregar_vehiculos(ambulancia12)
hospital10.agregar_vehiculos(helicoptero9)


#Agrego cirujanos a los hospitales
hospital1.agregar_cirujano(cirujanoG5)
hospital1.agregar_cirujano(cirujanoPL2)
hospital1.agregar_cirujano(cirujanoC3)

hospital2.agregar_cirujano(cirujanoC4)
hospital2.agregar_cirujano(cirujanoPU1)
hospital2.agregar_cirujano(cirujanoPL3)

hospital3.agregar_cirujano(cirujanoPU4)
hospital3.agregar_cirujano(cirujanoT)
hospital3.agregar_cirujano(cirujanoPL1)
hospital3.agregar_cirujano(cirujanoG4)
hospital3.agregar_cirujano(cirujanoC1)


hospital4.agregar_cirujano(cirujanoT1)

hospital5.agregar_cirujano(cirujanoG1)
hospital5.agregar_cirujano(cirujanoG6)

hospital6.agregar_cirujano(cirujanoC5)
hospital6.agregar_cirujano(cirujanoG2)


hospital7.agregar_cirujano(cirujanoG3)

hospital8.agregar_cirujano(cirujanoG7)

hospital9.agregar_cirujano(cirujanoPU2)

hospital10.agregar_cirujano(cirujanoPL4)


#agrego la lista de hospitales cada hospital
hospitales=[]
hospitales.append(hospital1)
hospitales.append(hospital2)
hospitales.append(hospital3)
hospitales.append(hospital4)
hospitales.append(hospital5)
hospitales.append(hospital6)
hospitales.append(hospital7)
hospitales.append(hospital8)
hospitales.append(hospital9)
hospitales.append(hospital10)


#me imprime todos 

for hospital in hospitales:
    print("Institucion:"+hospital.nombre)
    print("________")
    print(" ")
    print("Cirujanos :")

    for cirujano in hospital.cirujanos:
        print (cirujano)
    print(f"_____")
    print("Pacientes :")
    for paciente in hospital.pacientes:
        print (paciente)
    print(" ")



#registra donantes y pacientes
incucai = INCUCAI()
print("Comienzo de busqueda:")
#caso coincidencia receptor 1 y donante 2 con corazon mismo tipo de sangre misma provincia, utiliza el auto con mayor velocidad
incucai.registrarPaciente(receptor1)
incucai.registrarPaciente(donante1)

#caso coincidencia distintas provincias debe utilizar helicoptero. Donante 2 esta en hospital 3 y receptor dos en hospital dos
incucai.registrarPaciente(receptor2)
incucai.registrarPaciente(donante2)
"""
#caso coincidencia distinta provincia distinto partido debe utilizar avion. donante 3 esta en Cordoba capital hospital 4 y receptor 3 esta en Buenos aires Moron
incucai.registrarPaciente(receptor3)
incucai.registrarPaciente(donante3)
#caso coincidencia pero no hay cirujano especializado para realizar cirujia no hay ablacion
incucai.registrarPaciente(receptor4)
incucai.registrarPaciente(donante4)
#caso coincidencia en mismo centros deberia realizarse  ablacion sin trasnporte, no asignar vehiculo, no calcular tiempo de viaje
incucai.registrarPaciente(receptor5)
incucai.registrarPaciente(donante5)
#caso coincidencia un donante dos receptores misma prioridad, receptor7 ingreso antes se le debe hacer la operacion a el
incucai.registrarPaciente(receptor6)
incucai.registrarPaciente(receptor7)
incucai.registrarPaciente(donante6)
#caso coincidencia un donante dos receptores un cirujano se lo da al de mayor prioridad
incucai.registrarPaciente(receptor8)
incucai.registrarPaciente(receptor9)
incucai.registrarPaciente(donante7)
#caso un donante 3 organos se lo da a 3 receptores
incucai.registrarPaciente(donante8)
incucai.registrarPaciente(receptor10)
incucai.registrarPaciente(receptor11)
#caso un donante y un receptor pero ya el cirujano trabajo
incucai.registrarPaciente(donante9)
incucai.registrarPaciente(receptor12)
#ultimo caso hay ablacion pero llega fuera de tiempo

"""
