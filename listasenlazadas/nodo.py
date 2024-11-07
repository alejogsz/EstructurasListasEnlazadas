from paciente import Paciente

class Nodo:
    def __init__(self, dato:Paciente)->None:
        self.dato:Paciente = dato  
        self.siguiente:Nodo = None
