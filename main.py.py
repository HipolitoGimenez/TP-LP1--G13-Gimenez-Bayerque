import datetime
import random
from donantes import *
from centro_de_salud import *
from organo import Organo
from cirujano import Cirujano
from receptor import Receptor
from vehiculo import Vehiculo
from helicoptero import Helicoptero
from auto import Auto
from avion import Avion
from centro_de_salud import CentroDeSalud
from persona import Persona
from INCUCAI import INCUCAI
from donantes import donantes


#Centros de salud
hospital1=CentroDeSalud("Hospital Italiano", "AV Italia 145", "CABA", "Buenos Aires", "84515262385")
hospital2=CentroDeSalud("Hospital Aleman", "AV Italia 145", "CABA", "Buenos Aires", "48545262385")
hospital3 = CentroDeSalud("Hospital Provincial de Córdoba", "Av. Vélez Sarsfield 1200", "Córdoba Capital", "Córdoba", "3514896523")
hospital4 = CentroDeSalud("Hospital José María Cullen", "Av. Freyre 2150", "Santa Fe", "Santa Fe", "3424578912")

#Cirujanos
cirujano1 = Cirujano( "Adrian","cardiovascular",True,0,"12345678", datetime.strptime("01-11-1980", "%d-%m-%Y"),"masculino","1122334455","A+","Hospital Italiano", "[Corazon]")
cirujano2 = Cirujano( "Juan","Pulmonar",True,0,"48545678", datetime.strptime("11-06-1975", "%d-%m-%Y"),"masculino","114434455","B+","Hospital Aleman", "[Pulmones]")
cirujano3 = Cirujano("Carla", "Hepática", True, 0, "56789456", datetime.strptime("22-02-1982", "%d-%m-%Y"), "femenino", "1166778899", "O+", "Hospital Provincial de Córdoba", "[Hígado]")
cirujano4 = Cirujano("Esteban", "Renal", True, 0, "47859632", datetime.strptime("03-12-1978", "%d-%m-%Y"), "masculino", "1155998877", "AB-", "Hospital José María Cullen", "[Riñón]")

# Donantes
#donante1 = donante("Adriana","23060432",fecha_de_nacimiento=datetime.strptime("02-06-1978", "%d-%m-%Y"),"F","2494534523","A+","hospital_italiano")
#donante2 =donante("Juan","25258456",fecha_de_nacimiento=datetime.strptime("12-01-1994", "%d-%m-%Y"),"M","15252523", "B+", "hospital_aleman", "Pulmón")

#Receprores
receptor1 = Receptor("Lucía","2345768988",datetime.strptime("04-11-2000", "%d-%m-%Y"),"F","1122334455","A+","Hospital Italiano","Corazón","Estable","2025-05-05", "Alta","Paro cardíaco")
receptor2= Receptor("Claudio","33545966", datetime.strptime("09-06-1999", "%d-%m-%Y"),"M","1155566685","B+","Hospital Aleman","Pulmon","Estable","2025-05-05", "Alta","Neumonia")
receptor3 = Receptor("María", "40234567", datetime.strptime("15-03-1985", "%d-%m-%Y"), "F", "1133445566", "O+", "Hospital Provincial de Córdoba", "Hígado", "Crítico", "2025-05-20", "Alta", "Cirrosis hepática")
receptor4 = Receptor("Jorge", "38999888", datetime.strptime("27-08-1972", "%d-%m-%Y"), "M", "1177889900", "AB-", "Hospital José María Cullen", "Riñón", "Estable", "2025-05-22", "Alta", "Insuficiencia renal")

#Organos
organo1 = Organo("Corazon")  
organo1.fecha_ablacion(datetime.now()) 
organo2 = Organo("Pulmon")  
organo2.fecha_ablacion(datetime.now()) 


#Agrego los vehiculos
ambulancia1=Auto(120)
helicoptero1=Helicoptero(300)
avion2 = Avion(600)

#hospital1.agregar_vehiculos(ambulancia1)
hospital1.agregar_vehiculos(helicoptero1)
hospital2.agregar_vehiculos(avion2)

#Agrego cirujanos a los hospitales
hospital1.agregar_cirujano(cirujano1)
hospital2.agregar_cirujano(cirujano1)

print("Cirujanos del Hospital Italiano:")
for c in hospital1.cirujanos:
     print(c)



#Agrego los vehiculos
#hospital1.agregar_vehiculos(ambulancia1)
hospital1.agregar_vehiculos(ambulancia1)
hospital2.agregar_vehiculos(helicoptero1)

#auto1 = auto(120)
#avion1 = avion(800)
#helicoptero1=helicoptero(500)
#lista_vehiculos_Hospital_Italiano=[]
print(f"Paciente {receptor1.nombre} Se en cuentra{ receptor1.estado}")
print(cirujano1.operacion())
print(cirujano1) 
print("Se encuentra disponible {cirujano1.}")
print(organo1)##Corre
#lista_donantes = [donante1, donante2]
lista_receptores = [receptor1, receptor2, receptor3, receptor4]

#print("=== LISTADO DE DONANTES ===")
#for d in lista_donantes:
#    print(d)
lista_receptores = [receptor1, receptor2, receptor3, receptor4]

print("=== LISTADO DE RECEPTORES ===")
for receptor in lista_receptores:
    print(receptor)


cirujano_asignado = hospital1.asignar_cirujano(receptor1.organo_necesario)
if cirujano_asignado:
    print(f"El cirujano : {cirujano_asignado.nombre} fue asignado a {receptor1.nombre}")
else:
    print("No se pudo asignar un cirujano.")

# Asignar cirujano al órgano necesario del receptor
#cirujano_asignado = hospital1.(receptor1.organo_necesario)


#print(f"Vehiculo: Auto Velocidad: {auto1.velocidad}km/h.  Distancia Recorrida: {auto1.distancia} kms")
#print(f"Vehiculo: Avion  Velocidad: {avion1.velocidad}km/h. Distancia Recorrida: {avion1.distancia} kms")
###

# agregar_receptor(self,nombre, DNI, fecha_de_nacimiento, sexo, telefono, tipo_de_sangre, centro_de_salud,organo_necesario,estado,fecha_de_ingreso,prioridad,patologia)
incucai = INCUCAI()
incucai.agregar_receptor(receptor1.nombre, receptor1.DNI, receptor1.fecha_de_nacimiento, receptor1.sexo, receptor1.telefono, receptor1.tipo_de_sangre, receptor1.centro_de_salud,receptor1.organo_necesario,receptor1.estado,receptor1.fecha_de_ingreso,receptor1.prioridad,receptor1.patologia)
incucai.agregar_receptor(receptor2.nombre, receptor2.DNI, receptor2.fecha_de_nacimiento, receptor2.sexo, receptor2.telefono, receptor2.tipo_de_sangre, receptor2.centro_de_salud,receptor2.organo_necesario,receptor2.estado,receptor2.fecha_de_ingreso,receptor2.prioridad,receptor2.patologia)


