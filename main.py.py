 
from donantes import *
from centro_de_salud import *
from datetime import datetime
from organo import organo
from cirujano import cirujano
from receptor import receptor
from vehiculo import vehiculo
from helicoptero import helicoptero
from auto import auto
from avion import avion

#Cirujanos
cirujano1 = cirujano( "Adrian","cardiovascular",True,0,"12345678","1980-01-01","masculino","1122334455","A+","Hospital Italiano", "[Corazon]")
cirujano2 = cirujano( "Juan","Pulmonar",True,0,"48545678","1975-06-11","masculino","114434455","B+","Hospital Aleman", "[Pulmones]")


#Personas/ donantes
persona1 = persona("Adriana", "23060432", "02-06-1978", "F", "2494534523", "A+", "Italiano")
persona2 = persona("Juan", "25258456", "12-01-1994", "M", "15252523", "B+", "Aleman")

#Receprores
receptor1 = receptor("Lucía","2345768988","04-11-2000","F","1122334455","A+","Hospital Italiano","Corazón","Estable","2025-05-05", "Alta","Paro cardíaco")
receptor2= receptor("Claudio","33545966","09-06-1999","M","1155566685","B+","Hospital Aleman","Pulmon","Estable","2025-05-05", "Alta","Neumonia")

#Organos
organo1 = organo("Corazon")  
organo1.fecha_ablacion(datetime.now()) 
organo2 = organo("Pulmon")  
organo1.fecha_ablacion(datetime.now()) 

#Centros de salud
hospital1=centro_de_salud("Hospital Italiano", "AV Italia 145", "CABA", "Buenos Aires", "84515262385")
hospital2=centro_de_salud("Hospital Aleman", "AV Italia 145", "CABA", "Buenos Aires", "48545262385")

ambulancia1=auto( 120)
helicoptero1=helicoptero( 300)
avion2 = avion(600)


#Agrego los vehiculos
#hospital1.agregar_vehiculos(ambulancia1)
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
print(f"Paciente {receptor1.nombre} Se en cuentra{ receptor1.estado}")
print(cirujano1.operacion())
print(cirujano1) 
print("Se encuentra disponible {cirujano1.}")
print(organo1)##Corre


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