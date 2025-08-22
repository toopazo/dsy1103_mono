import time
import datetime
import random

from app.mvc_controlador import Controlador


class Vista:
    def __init__(self):
        """
        Levantar la pag web
        """
        self.controlador = Controlador()
        self.whoami = Vista.__name__

    def main(self):
        """
        Gestionar trafico de la pag web y comunicarse con la lógica del negocio
        """

        num_tries = random.randint(5, 10)
        for _ in range(num_tries):
            period = random.randint(0, 2)
            time.sleep(period)
            print(
                f"[{self.whoami}] Simulando el inicio de una petición al controlador: {datetime.datetime.now().isoformat()}"
            )
            self.controlador.main()

        return "OK"