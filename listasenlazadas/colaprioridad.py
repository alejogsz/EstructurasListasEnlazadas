from nodo import Nodo
from paciente import Paciente 


class ColaPrioridad:
    def __init__(self)->None:
        self.head:Nodo = None  

    def insertar(self, paciente:Paciente)->None:
        nuevo_nodo:Nodo = Nodo(paciente)

        if self.head is None or self.head.dato.prioridad < paciente.prioridad:
            nuevo_nodo.siguiente = self.head
            self.head:Nodo = nuevo_nodo
        else:

            actual:Nodo = self.head
            while actual.siguiente is not None and actual.siguiente.dato.prioridad >= paciente.prioridad:
                actual = actual.siguiente

            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def atender(self)->str:
        if self.head is None:
            print("No hay pacientes en espera.")
            return None

        paciente_a_atender = self.head.dato
        self.head = self.head.siguiente 
        print(f"Atendiendo a: {paciente_a_atender}")
        return paciente_a_atender

    def mostrar(self)->str:
        if self.head is None:
            print("La cola de pacientes está vacía.")
            return

        print("Pacientes en la cola de prioridad:")
        actual = self.head
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente
