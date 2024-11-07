from nodo import Nodo



class ColaPrioridad:
    def __init__(self):
        self.head = None  # La cabeza de la lista enlazada, que representa el paciente con mayor prioridad

    def insertar(self, paciente):
        nuevo_nodo = Nodo(paciente)

        # Si la lista está vacía o el paciente tiene la prioridad más alta, se coloca al inicio
        if self.head is None or self.head.dato.prioridad < paciente.prioridad:
            nuevo_nodo.siguiente = self.head
            self.head = nuevo_nodo
        else:
            # Recorremos la lista para encontrar la posición correcta
            actual = self.head
            while actual.siguiente is not None and actual.siguiente.dato.prioridad >= paciente.prioridad:
                actual = actual.siguiente

            # Insertamos el nuevo nodo en la posición encontrada
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def atender(self):
        # Atiende (remueve) al paciente con mayor prioridad
        if self.head is None:
            print("No hay pacientes en espera.")
            return None

        paciente_a_atender = self.head.dato
        self.head = self.head.siguiente  # Avanzamos la cabeza al siguiente nodo
        print(f"Atendiendo a: {paciente_a_atender}")
        return paciente_a_atender

    def mostrar(self):
        # Muestra todos los pacientes en la cola de prioridad
        if self.head is None:
            print("La cola de pacientes está vacía.")
            return

        print("Pacientes en la cola de prioridad:")
        actual = self.head
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente
