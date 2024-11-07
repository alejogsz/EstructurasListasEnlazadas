class Paciente:
    def __init__(self, nombre, descripcion_consulta):
        self.nombre = nombre
        self.descripcion_consulta = descripcion_consulta
        self.prioridad = self.calcular_prioridad()  # Calculamos la prioridad cuando se crea el paciente

    def calcular_prioridad(self):
        # Asigna prioridad según palabras clave en la descripción
        if any(word in self.descripcion_consulta.lower() for word in ["dolor agudo", "fractura", "ataque"]):
            return 5
        elif any(word in self.descripcion_consulta.lower() for word in ["fiebre", "tos"]):
            return 3
        elif any(word in self.descripcion_consulta.lower() for word in ["revisión", "control"]):
            return 1
        return 1  # Prioridad por defecto si no se encuentra palabra clave

    def __str__(self):
        return f"Paciente({self.nombre}, Prioridad: {self.prioridad}, Consulta: {self.descripcion_consulta})"
