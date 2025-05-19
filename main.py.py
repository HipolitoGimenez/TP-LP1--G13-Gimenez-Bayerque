 
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
from INCUCAI import INCUCAI


incu=INCUCAI()

#Cirujanos
cirujano1 = cirujano( "Adrian","cardiovascular",True,0,"12345678","1980-01-01","masculino","1122334455","A+","Hospital Italiano", "[Corazon]")
cirujano2 = cirujano( "Juan","Pulmonar",False,0,"48545678","1975-06-11","masculino","114434455","B+","Hospital Aleman", "[Pulmones]")



#donantes

donante1=donante("Esteban", "25418789", "22-10-1980", "M", "5424534523", "A+", "Hospital Italiano", "CABA", "Buenos Aires", "2025-05-05", "2025-05-05")
donante2=donante("Maria", "05418789", "29-02-1950", "F", "115434523", "B+", "Hospital Aleman", "CABA", "Buenos Aires","2025-05-10", "2025-05-05")

#Receprores
receptor1 = receptor("Lucía","2345768988","04-11-2000","F","1122334455","A+","Hospital Italiano", "CABA", "Buenos Aires","Corazón","Estable","2025-05-05", "Alta","Paro cardíaco")
receptor2= receptor("Claudio","33545966","09-06-1999","M","1155566685","B+","Hospital Aleman", "CABA", "Buenos Aires","Pulmon","Estable","2025-05-05", "Alta","Neumonia")

incu.registrar_receptores(receptor1)
incu.registrar_receptores(receptor2)

incu.registrar_donantes(donante1)
incu.registrar_donantes(donante2)


print("Receptores del INCUCAI:")
for rec in incu.lista_receptores:
    print(f"- {rec}")

print("Donantes del INCUCAI:")
for don in incu.lista_donates:
    print(f"- {don}")

#Organos
organo1 = organo("Corazon")  
organo1.fecha_ablacion(datetime.now()) 
organo2 = organo("Pulmon")  
organo2.fecha_ablacion(datetime.now()) 

#Centros de salud
hospital1=centro_de_salud("Hospital Italiano", "AV Italia 145", "CABA", "Buenos Aires", "84515262385")
hospital2=centro_de_salud("Hospital Aleman", "AV Italia 145", "CABA", "Buenos Aires", "48545262385")

#Agrego los vehiculos
ambulancia1=auto(120)
helicoptero1=helicoptero(300)
avion2 = avion(600)

#hospital1.agregar_vehiculos(ambulancia1)
hospital1.agregar_vehiculos(helicoptero1)
hospital2.agregar_vehiculos(avion2)

#Agrego cirujanos a los hospitales
hospital1.agregar_cirujano(cirujano1)
hospital2.agregar_cirujano(cirujano2)

print("Cirujanos del Hospital Italiano:")
for c in hospital1.cirujanos:
     print(f"- {c}")

print("Cirujanos del Hospital Aleman:")
for a in hospital1.cirujanos:
     print(f"- {a}")

hospital1.agregar_vehiculos(ambulancia1)
hospital2.agregar_vehiculos(helicoptero1)

print(f"Paciente {receptor1.nombre} Se encuentra { receptor1.estado}. ")
print(cirujano2.operacion())
print(f"Se encuentra disponible {cirujano1.nombre}. Especialidad: {cirujano1.especialidad}")
print(organo1)##Corre
print(organo2)


#cirujano_asignado = hospital1.asignar_cirujano(receptor1.organo_necesario)
#if cirujano_asignado:
 #   print(f"El cirujano : {cirujano_asignado.} fue asignado a {recep}")
#else:
 #   print("No se pudo asignar un cirujano.")

# Asignar cirujano al órgano necesario del receptor
#cirujano_asignado = hospital1.(receptor1.organo_necesario)


#print(f"Vehiculo: Auto Velocidad: {auto1.velocidad}km/h.  Distancia Recorrida: {auto1.distancia} kms")
#print(f"Vehiculo: Avion  Velocidad: {avion1.velocidad}km/h. Distancia Recorrida: {avion1.distancia} kms")
###