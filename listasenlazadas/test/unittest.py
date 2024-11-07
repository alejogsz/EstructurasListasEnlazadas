import unittest
from typing import Optional
from listasenlazadas.colaprioridad import ColaPrioridad
from listasenlazadas.paciente import Paciente
from listasenlazadas.main import Main

class TestPaciente(unittest.TestCase):
    def test_calculo_prioridad_alta(self):
        paciente = Paciente("Juan", "dolor agudo en el pecho")
        self.assertEqual(paciente.prioridad, 5)

    def test_calculo_prioridad_media(self):
        paciente = Paciente("Ana", "tengo fiebre y tos")
        self.assertEqual(paciente.prioridad, 3)

    def test_calculo_prioridad_baja(self):
        paciente = Paciente("Luis", "control de rutina")
        self.assertEqual(paciente.prioridad, 1)

    def test_calculo_prioridad_default(self):
        paciente = Paciente("Pedro", "consulta general sin síntomas específicos")
        self.assertEqual(paciente.prioridad, 1)


class TestColaPrioridad(unittest.TestCase):
    def setUp(self) -> None:
        self.cola = ColaPrioridad()

    def test_insertar_paciente(self):
        paciente = Paciente("Carlos", "fractura en el brazo")
        self.cola.insertar(paciente)
        self.assertEqual(self.cola.head.dato.nombre, "Carlos")

    def test_atender_paciente(self):
        paciente1 = Paciente("Maria", "dolor agudo en la cabeza")
        paciente2 = Paciente("Andres", "fiebre leve")
        self.cola.insertar(paciente1)
        self.cola.insertar(paciente2)
        atendido = self.cola.atender()
        self.assertEqual(atendido.nombre, "Maria")
        self.assertEqual(self.cola.head.dato.nombre, "Andres")

    def test_orden_prioridad(self):
        paciente1 = Paciente("Carlos", "fractura en el brazo")
        paciente2 = Paciente("Luis", "control de rutina")
        paciente3 = Paciente("Ana", "fiebre alta")
        self.cola.insertar(paciente2)
        self.cola.insertar(paciente3)
        self.cola.insertar(paciente1)
        self.assertEqual(self.cola.head.dato.nombre, "Carlos")
        self.assertEqual(self.cola.head.siguiente.dato.nombre, "Ana")
        self.assertEqual(self.cola.head.siguiente.siguiente.dato.nombre, "Luis")

    def test_mostrar_cola_vacia(self):
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cola.mostrar()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "La cola de pacientes está vacía.")

    def test_mostrar_cola_con_pacientes(self):
        paciente1 = Paciente("Carlos", "fractura en el brazo")
        paciente2 = Paciente("Luis", "control de rutina")
        self.cola.insertar(paciente1)
        self.cola.insertar(paciente2)
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.cola.mostrar()
        sys.stdout = sys.__stdout__
        self.assertIn("Paciente(Carlos", captured_output.getvalue())
        self.assertIn("Paciente(Luis", captured_output.getvalue())


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.main = Main()

    def test_menu_opciones_validas(self):
        paciente = Paciente("Carlos", "fractura en el brazo")
        self.main.cola.insertar(paciente)
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.main.cola.mostrar()
        sys.stdout = sys.__stdout__
        self.assertIn("Carlos", captured_output.getvalue())

    def test_atender_paciente_main(self):
        paciente = Paciente("Maria", "dolor agudo en la cabeza")
        self.main.cola.insertar(paciente)
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.main.cola.atender()
        sys.stdout = sys.__stdout__
        self.assertIn("Atendiendo a: Paciente(Maria", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
