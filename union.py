
from estacionamiento import *
from vehiculo import *
import datetime

lista_estacionamientos = []

def estacionamiento_leer(path) -> list[Estacionamiento]:
    pass


def estacionamiento_guardar(path) -> None:
    pass


def existe_estacionamiento(nombre: str, estacionamientos: list) -> bool:
    for estacionamiento in estacionamientos:
        if estacionamiento.nombre == nombre:
            return True
    return False

def menu(estacionamientos: list) -> int:
    print("\n  ***  Seleccioná un estacionamiento: \n")
    for i, estacionamiento in enumerate(estacionamientos):
        print(f"\n {i + 1}. {estacionamiento.nombre} \n ESPACIO PARA MOTOS: {estacionamiento.cant_parcelas_motos} \n ESPACIO PARA AUTOS: {estacionamiento.cant_parcelas_autos}")
    while True:
            opcion = int(input("\n ***Ingresá una opción*** [0 PARA SALIR]:     "))
            if 1 <= opcion <= len(estacionamientos):
                return opcion - 1
            elif opcion == 0:
                print("\n Saliendo...")
                return None
            else:
                print("\n Opción inválida. Intentá otra vez: ")

def submenu(vehiculos: list) -> int:
    if not vehiculos:
        print("No hay vehículos registrados. \n")
        return None

    print("\n ***  Listado de vehículos  *** \n")
    for i, vehiculo in enumerate(vehiculos):
        print(f"\n {i + 1}. VEHICULO: {vehiculo.tipo} \n PATENTE: {vehiculo.patente} \n HORA DE INGRESO: {vehiculo.hora_ingreso}")
    
    while True:
        opcion = int(input("\n *** Elegí el vehículo que querés sacar*** [0 PARA SALIR]:     \n"))
        if 1 <= opcion <= len(vehiculos):
            return opcion - 1
        elif opcion == 0:
            print("\n Saliendo...")
            return None
        else:
            print("\n Opción inválida. Intentá otra vez: ")

def alta_vehiculo(estacionamientos: list) -> bool:
    while True:
        opcion = menu(estacionamientos)
        estacionamiento_elegido = estacionamientos[opcion]

        tipo = input("\n Qué tipo de vehículo es? (MOTO - AUTO):  ").upper()
        patente = input("\n Ingresá la patente (TODO JUNTO, SIN ESPACIOS NI GUIONES):   ")

        nuevo_vehiculo = Vehiculo(tipo, patente)
    
        if tipo == "AUTO":
            if len(estacionamiento_elegido.autos) < estacionamiento_elegido.cant_parcelas_autos:
                estacionamiento_elegido.autos.append(nuevo_vehiculo)
                print("\n ***AUTO ingresado exitosamente***")
                estacionamiento_elegido.cant_parcelas_autos = estacionamiento_elegido.cant_parcelas_autos - 1
            else:
                print("\n Lo lamentamos. No hay parcelas para autos disponibles...")

        elif tipo == "MOTO":
            if len(estacionamiento_elegido.motos) < estacionamiento_elegido.cant_parcelas_motos:

                estacionamiento_elegido.motos.append(nuevo_vehiculo)
                print("\n ***MOTO ingresada exitosamente***")
                estacionamiento_elegido.cant_parcelas_motos = estacionamiento_elegido.cant_parcelas_motos - 1 
            else:
                print("\n Lo lamentamos. No hay parcelas para motos disponibles...")

        else:
            print("\n No entendí... Reingresá: ")
        seguir = input("\n ¿Seguimos? [1] Para sí [0] Para no:  ")
        if seguir == "0":
            break
    return True

def alta_estacionamiento(estacionamientos: list) -> Estacionamiento:

    while True:

        nombre = input("\n Ingresá el nombre del estacionamiento: ")
       
        while existe_estacionamiento(nombre, estacionamientos):
            print("\n Ya existe un estacionamiento con ese nombre. Intentá con otro: ")
            nombre = input("\n Ingresá el nombre del estacionamiento: ")

        cant_parcelas_autos = int(input("\n Ingresá la CANTIDAD de parcelas para AUTOS que existen en el estacionamiento: "))
        while cant_parcelas_autos <= 0:
            print("\n Error. No pueden ser menores a 0, reingrese: ")
            cant_parcelas_autos = int(input("\n [ERROR] Reingresá: "))
        
        cant_parcelas_motos = int(input("\n Ingresá la CANTIDAD de parcelas para MOTOS que existen en el estacionamiento: "))
        while cant_parcelas_motos <= 0:
            print("\n Error. No pueden ser menores a 0, reingrese: ")
            cant_parcelas_motos = int(input("\n [ERROR] Reingresá: "))

        coste_hora_auto = float(input("\n Ingresá el COSTE por HORA de AUTOS: "))
        while coste_hora_auto <= 0:
            print("\n Error. No puede ser menor a 0, reingrese: ")
            coste_hora_auto = float(input("\n [ERROR] Reingresá: "))

        coste_hora_moto = float(input("\n Ingresá el COSTE por HORA de MOTOS: "))
        while coste_hora_moto <= 0:
            print("\n Error. No puede ser menor a 0, reingrese: ")
            coste_hora_moto = float(input("\n [ERROR] Reingresá: "))

        nuevo_estacionamiento = Estacionamiento(nombre, cant_parcelas_autos, cant_parcelas_motos, coste_hora_auto, coste_hora_moto)
        estacionamientos.append(nuevo_estacionamiento)
        
        opcion = input("\n ¿Desea dar de alta a otro estacionamiento? [1] para seguir [0] para salir:  ")
        if opcion == "0":
            break
        else:
            continue

def calcular_coste(hora_ingreso, hora_salida, coste_hora):
    minutos_estacionados = (hora_salida - hora_ingreso).total_seconds() / 60
    coste_minuto = coste_hora / 60
    return minutos_estacionados * coste_minuto

def egresar_vehiculo(estacionamientos: list):

    while True:
        opcion = menu(estacionamientos)
        if opcion is None:
            break

        estacionamiento_elegido = estacionamientos[opcion]

        vehiculos = estacionamiento_elegido.autos + estacionamiento_elegido.motos
        vehiculo_elegido = submenu(vehiculos)

        if vehiculo_elegido is not None:
            
            vehiculo = vehiculos.pop(vehiculo_elegido)
            hora_salida = datetime.datetime.now()

            if vehiculo.tipo == "AUTO":
                
                coste = calcular_coste(vehiculo.hora_ingreso, hora_salida, estacionamiento_elegido.coste_hora_auto)
                estacionamiento_elegido.autos.remove(vehiculo)
                estacionamiento_elegido.cant_parcelas_autos += 1

            elif vehiculo.tipo == "MOTO":
                
                coste = calcular_coste(vehiculo.hora_ingreso, hora_salida, estacionamiento_elegido.coste_hora_moto)
                estacionamiento_elegido.motos.remove(vehiculo)
                estacionamiento_elegido.cant_parcelas_motos += 1

            coste_formateado = round(coste, 2)  
            print(f"\n Vehículo {vehiculo.tipo} con patente {vehiculo.patente} ha salido. \n Coste: ${coste_formateado}")

        opcion = input("\n¿Desea egresar otro vehículo? [1] para seguir [0] para salir: ")
        if opcion == "0":
            break

def modificar_costes(estacionamientos: list):

    print("\n ***  ACTUALIZACIÓN DE TARIFAS  *** \n")

    opcion = menu(estacionamientos)

    if opcion == None:
        return None
    
    estacionamiento_seleccionado = estacionamientos[opcion]

    print(f"\n Costo actual por hora para AUTOS: ${estacionamiento_seleccionado.coste_hora_auto}")
    nuevo_coste_estacionamiento = float(input("\n Ingresá el nuevo coste por hora para AUTOS:   "))
    estacionamiento_seleccionado.coste_hora_autos = nuevo_coste_estacionamiento

    print(f"\n Costo actual por hora para MOTOS: ${estacionamiento_seleccionado.coste_hora_moto}")
    nuevo_coste_estacionamiento = float(input("\n Ingresá el nuevo coste por hora para MOTOS:  "))
    estacionamiento_seleccionado.coste_hora_motos = nuevo_coste_estacionamiento

    print("\n ¡LISTO! Los costos han sido actualizados exitosamente ;D \n")

def listar_vehiculos(estacionamiento):
    vehiculos_estacionados = estacionamiento.autos + estacionamiento.motos
    return vehiculos_estacionados

def mapeo_punto5(estacionamientos: list):

    vehiculos_estacionados = map(listar_vehiculos, estacionamientos)

    for i, vehiculos_estacionados in enumerate(vehiculos_estacionados):
        print(f"\n ***  Estacionamiento {i+1}  ***\n")
        for vehiculo in vehiculos_estacionados:
            print(f"\n -TIPO DE VEHICULO: {vehiculo.tipo}, \n -PATENTE DEL VEHICULO: {vehiculo.patente}, \n -HORA DE INGRESO DEL VEHICULO: {vehiculo.hora_ingreso}\n")

def ordenar_patentes(estacionamientos: list):
    for i, estacionamiento in enumerate(estacionamientos):
        vehiculos = estacionamiento.autos + estacionamiento.motos
        patentes = []
        for vehiculo in vehiculos:
            patentes.append(vehiculo.patente)
        patentes_ordenadas = sorted(patentes, reverse=True)
        print(f"\n *** Estacionamiento {i+1} \n Patentes ordenadas (descendentemente): \n")
        for patente in patentes_ordenadas:
            print(f" \n *** TIPO DE VEHÍCULO: {vehiculo.tipo} \n *** PATENTE: {patente}")

alta_estacionamiento(lista_estacionamientos)
alta_vehiculo(lista_estacionamientos)
#egresar_vehiculo(lista_estacionamientos)
#modificar_costes(lista_estacionamientos)
#mapeo_punto5(lista_estacionamientos)
ordenar_patentes(lista_estacionamientos)

def grabar_log(path: str, msj: str):
#Formato: [Patente: XXX-NNN] [Hora ingreso: DD-MM-YYYY HH:MM] [Hora egreso: DD-MM-YYYY HH:MM] [Importe]
    pass




# MAIN
def punto_1() -> bool:
    pass



def punto_2() -> bool:
    pass


def punto_3() -> bool:
    pass



def punto_4() -> bool:
    pass



def punto_5() -> bool:
    pass



def punto_6() -> bool:
    pass



def punto_7() -> bool:
    pass



def punto_8() -> bool:
    pass



def punto_9() -> bool:
    pass



def punto_10() -> bool:
    pass
