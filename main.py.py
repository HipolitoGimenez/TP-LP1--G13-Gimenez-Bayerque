from persona import persona 
from receptor import receptor
from donantes import donante
from organo import organo
from cirujano import cirujano
from vehiculo import vehiculo
from auto import auto
from avion import avion
from datetime import datetime

cirujano1 = cirujano( "Adrian","cardiovascular",True,0,"12345678","1980-01-01","masculino","1122334455","A+","Hospital Italiano")# modifique cardivascular true y 0 estaba a lo ultimo y lo pase adelante por el orden
persona1 = persona("Adriana", "23060432", "02-06-1978", "F", "2494534523", "A+", "Aleman")
receptor1 = receptor("Lucía","2345768988","04-11-2000","F","1122334455","A+","Hospital Italiano","Corazón","Estable","2025-05-05", "Alta","Paro cardíaco")
organo1 = organo("Corazon")  
organo1.fecha_ablacion(datetime.now()) 
auto1 = auto(120, "Distancia(?)", []) 
avion1 = avion(800, 1500, [])
print(f"Paciente {receptor1.nombre} Se en cuentra{ receptor1.estado}")
print(cirujano1.operacion())
print(cirujano1) 
print(organo1)##Corre
print(f"Vehiculo: Auto Velocidad: {auto1.velocidad}km/h.  Distancia Recorrida: {auto1.distancia} kms")
print(f"Vehiculo: Avion  Velocidad: {avion1.velocidad}km/h. Distancia Recorrida: {avion1.distancia} kms")
