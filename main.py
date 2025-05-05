from sistema_turnos import Turnero, Paciente

turnero = Turnero()

p1 = Paciente("Ana", "123", 2)
p2 = Paciente("Juan", "456", 1)
p3 = Paciente("Luis", "789", 3)

turnero.solicitar_turno(p1)
turnero.solicitar_turno(p2)
turnero.solicitar_turno(p3)

turnero.llamar_siguiente()  # Debería llamar a Juan (urgencia 1)
turnero.llamar_siguiente()  # Ana (urgencia 2)
turnero.llamar_siguiente()  # Luis (urgencia 3)
turnero.llamar_siguiente()  # No hay pacientes en espera
