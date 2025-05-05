from persona import persona 
from receptor import receptor
from donantes import donante
from organo import organo
from cirujano import cirujanos
from datetime import datetime

cirujano1 = cirujanos( 
    "Adrian",
    "12345678",
    "1980-01-01",
    "masculino",
    "1122334455",
    "A+",
    "Hospital Italiano",
    "cardiovascular",
    True,
    0
    )

persona1 = [persona("Adrian","23060432","02-06-1978","F","2494534523","A+","Aleman")]
receptor1 = receptor(
    "Lucía",               # nombre
    "2345768988",          # DNI
    "04-11-2000",          # fecha de nacimiento
    "F",                   # sexo
    "1122334455",          # teléfono
    "A+",                  # tipo de sangre
    "Italiano",            # centro de salud
    "Corazón",             # órgano necesario
    "Estable",             # estado
    "2025-05-05",          # fecha de ingreso
    "Alta",                # prioridad
    "Paro cardíaco"        # patología
)

'''organo1=[organo("Corazon")]
organo.fecha_ablacion(datetime.now())'''

print(cirujanos.operacion(cirujano1))
