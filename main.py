class Asiento:
    def __init__(self, color: str, precio: int, registro: int):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color: str):
        # Se verifica que el color sea uno de los colores permitidos
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color

class Motor:
    def __init__(self, numeroCilindros: int, tipo: str, registro: int):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro: int):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo: str):
        # Comprobar que el valor ingresado sea "electrico" o "gasolina"
        if nuevo_tipo == "electrico" or nuevo_tipo == "gasolina":
            self.tipo = nuevo_tipo

class Auto:
    cantidad_creados = 0

    def __init__(self, modelo: str, precio: int, asientos: list, marca: str, motor, registro: int):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidad_creados += 1

    def cantidadAsientos(self):
        i = 0
        for asiento in self.asientos:
            if i != None and isinstance(asiento, Asiento):
                i += 1
        return i

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento != self.registro != self.motor.registro:
                return "Las piezas no son originales"


        return "Auto original"
