class Paciente:
    def __init__(self, nombre:str, descripcion_consulta:str)->None:
        self.nombre:str = nombre
        self.descripcion_consulta:str = descripcion_consulta
        self.prioridad:int = self.calcular_prioridad() 

    def calcular_prioridad(self)->int:
        if any(word in self.descripcion_consulta.lower() for word in ["dolor agudo", "fractura", "ataque"]):
            return 5
        elif any(word in self.descripcion_consulta.lower() for word in ["fiebre", "tos"]):
            return 3
        elif any(word in self.descripcion_consulta.lower() for word in ["revisión", "control"]):
            return 1
        return 1  

    def __str__(self)->str:
        return f"Paciente({self.nombre}, Prioridad: {self.prioridad}, Consulta: {self.descripcion_consulta})"
