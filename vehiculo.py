from datetime import datetime

class Vehiculo:

    def __init__(self, tipo: str, patente: str) -> None:
        self.tipo = tipo
        self.patente = patente
        self.hora_ingreso = datetime.now()

    def __str__(self) -> str:
        return self.patente

    def __len__(self) -> int:
        hora_actual = datetime.now()
        diferencia = hora_actual - self.hora_ingreso
        return diferencia.total_seconds() // 60