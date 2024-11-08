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


    def agrupar_por_prioridad(self) -> dict:
        lotes = {}
        actual = self.head
        while actual is not None:
            prioridad = actual.dato.prioridad
            if prioridad not in lotes:
                lotes[prioridad] = []
            lotes[prioridad].append(actual.dato)
            actual = actual.siguiente
        return lotes

    def atender_lote_mayor(self) -> None:
        lotes = self.agrupar_por_prioridad()
        if not lotes:
            print("No hay pacientes para agrupar.")
            return

        # Calcular el promedio de pacientes por lote
        total_pacientes = sum(len(lote) for lote in lotes.values())
        promedio = total_pacientes // len(lotes)

        # Buscar el lote con mayor cantidad de pacientes
        lote_mayor = max(lotes.values(), key=len)

        print(f"\nAtendiendo pacientes del lote con más pacientes hasta alcanzar el promedio ({promedio} pacientes):")
        for _ in range(min(promedio, len(lote_mayor))):
            paciente = lote_mayor.pop(0)
            print(f"Atendiendo a: {paciente}")
