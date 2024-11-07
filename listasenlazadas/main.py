from colaprioridad import ColaPrioridad
from paciente import Paciente

class Main:
    def __init__(self)->None:
        self.cola = ColaPrioridad()

    def mostrar_menu(self)->None:
        print("\n--- Sistema de Gestión de Clínica ---")
        print("1. Agregar paciente")
        print("2. Atender paciente")
        print("3. Mostrar cola de pacientes")
        print("4. Salir")

    def ejecutar(self)->None:
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del paciente: ")
                descripcion = input("Ingrese la descripción de la consulta: ")
                paciente = Paciente(nombre, descripcion)
                self.cola.insertar(paciente)
                print(f"Paciente {nombre} agregado con prioridad {paciente.prioridad}.")
            
            elif opcion == "2":
                self.cola.atender()
            
            elif opcion == "3":
                self.cola.mostrar()
            
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            
            else:
                print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    sistema = Main()
    sistema.ejecutar()

