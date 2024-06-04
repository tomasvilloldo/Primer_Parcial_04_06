class Estacionamiento:

    recaudacion = 0

    def __init__(self, nombre: str, cant_parcelas_autos: int, cant_parcelas_motos: int, coste_hora_auto:
    float, coste_hora_moto: float) -> None:
        self.nombre = nombre
        self.cant_parcelas_autos = cant_parcelas_autos
        self.cant_parcelas_motos = cant_parcelas_motos
        self.coste_hora_auto = coste_hora_auto
        self.coste_hora_moto = coste_hora_moto
        self.recaudacion = 0
        self.autos = []
        self.motos = []
        


    def __str__(self) -> str:
# Mostrara toda la informacion del estacionamiento. [CANT MOTOS] [CANT AUTOS] [RECAUDACION DEL DIA].
        return "[CANT. MOTOS]:" + {self.cant_parcelas_motos} + "[CANT. AUTOS]:" + {self.cant_parcelas_autos} + "[RECAUDACIÓN DEL DIA]:" + {self.recaudacion}


    def __len__(self) -> int:
# Devuelve la recaudacion con el formato float, con dos numero despues de la coma.
        pass