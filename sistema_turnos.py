import heapq
import itertools

# Contador para evitar comparación directa entre objetos con misma prioridad
contador = itertools.count()

class Paciente:
    def __init__(self, nombre, dni, urgencia):
        self.nombre = nombre
        self.dni = dni
        self.urgencia = urgencia  # 1 = crítico, 2 = urgente, 3 = común

    def __str__(self):
        return f"{self.nombre} (DNI: {self.dni}) - Urgencia: {self.urgencia}"

class Turnero:
    def __init__(self):
        self.cola_turnos = []  # Min-heap
        self.entry_finder = {}  # Mapear DNI al elemento en la heap

    def solicitar_turno(self, paciente):
        if paciente.dni in self.entry_finder:
            print("Este paciente ya tiene un turno.")
            return
        count = next(contador)
        entrada = (paciente.urgencia, count, paciente)
        self.entry_finder[paciente.dni] = entrada
        heapq.heappush(self.cola_turnos, entrada)
        print(f"Turno asignado a {paciente.nombre} con prioridad {paciente.urgencia}")

    def llamar_siguiente(self):
        while self.cola_turnos:
            _, _, paciente = heapq.heappop(self.cola_turnos)
            if paciente.dni in self.entry_finder:
                del self.entry_finder[paciente.dni]
                print(f"Llamando a: {paciente}")
                return paciente
        print("No hay pacientes en espera.")
        return None
