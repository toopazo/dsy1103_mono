import random

from app.perfiles import (
    AdministradorSistema,
    GerenteSucursal,
    EmpleadoVentas,
    Logística,
)


class Modelo:
    def __init__(self):
        """
        Conectarse a la BD
        """
        self.perfiles = [
            AdministradorSistema(),
            GerenteSucursal(),
            EmpleadoVentas(),
            Logística(),
        ]
        self.whoami = Modelo.__name__

        self.max_count = random.randint(5, 10)
        self.counter = 0

    def main(self):
        """
        Realizar validación de los datos escritos a la BD y de la lectura de los datos
        """
        print(f"[{self.whoami}] Validando datos escritos a la BD y traspasando los datos solicitados")

        self.counter += 1
        if self.counter > self.max_count:
            raise Exception("Límite de peticiones alcanzado")
