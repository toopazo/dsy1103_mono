from app.mvc_modelo import Modelo


class Controlador:
    def __init__(self):
        """
        Conectarse a la BD
        Conectarse a la vista
        """
        self.modelo = Modelo()
        self.whoami = Controlador.__name__

    def main(self):
        """
        Ejecutar la lógica del negocio
        """
        print(f"[{self.whoami}] Ejecutando la lógica del negocio")
        self.modelo.main()
