 
from donantes import *
from centro_de_salud import *
from datetime import datetime
from organo import organo

cirujano1 = cirujano( "Adrian","cardiovascular",True,0,"12345678","1980-01-01","masculino","1122334455","A+","Hospital Italiano", "[Corazon]")
cirujano2 = cirujano( "Juan","Pulmonar",True,0,"48545678","1975-06-11","masculino","114434455","B+","Hospital Aleman", "[Pulmones]")
lista__de_cirujanos=[]
lista__de_cirujanos.agregar_cirujano(cirujano1)

persona1 = persona("Adriana", "23060432", "02-06-1978", "F", "2494534523", "A+", "Aleman")
receptor1 = receptor("Lucía","2345768988","04-11-2000","F","1122334455","A+","Hospital Italiano","Corazón","Estable","2025-05-05", "Alta","Paro cardíaco")
organo1 = organo("Corazon")  
organo1.fecha_ablacion(datetime.now()) 

auto1 = auto(120)
avion1 = avion(800)
helicoptero1=helicoptero(500)

lista_vehiculos_Hospital_Italiano=[]
lista_vehiculos_Hospital_Italiano.agregar_vehiculos(auto1)
hospital1=centro_de_salud("Hospital Italiano", "AV Italia 145", "CABA", "Buenos Aires", "84515262385")
#hospital1.asignar_transporte("Buenos Aires", "CABA", 10, 0.5, "Av Italia 145")
print(f"Paciente {receptor1.nombre} Se en cuentra{ receptor1.estado}")
print(cirujano1.operacion())
print(cirujano1) 
print(organo1)##Corre
#print(f"Vehiculo: Auto Velocidad: {auto1.velocidad}km/h.  Distancia Recorrida: {auto1.distancia} kms")
#print(f"Vehiculo: Avion  Velocidad: {avion1.velocidad}km/h. Distancia Recorrida: {avion1.distancia} kms")
###