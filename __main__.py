from union import *
path_estacionamientos = 'db_estacionamientos.json'
ESTACIONAMIENTOS = estacionamiento_leer(path_estacionamientos)
"""
[MENU]
[1] Nuevo estacionamiento
[2] Ingreso de vehículo
[3] Egreso de vehículo
[4] Modificar costes por hora de vehiculos
[5] Listar vehículos estacionados (map)
[6] Listar vehículos ordenados por patente (descendente)
[7] Recaudación total de todos los estacionamientos (reduce)
[8] Listar vehiculos filtrados por cantidad de minutos estacionados que superen los 60 min (filter)
[9] Guardar archivo 'db_estacionamientos.csv'
[10] Ver log de ingreso
"""