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




codigo en php ( para enlazarlo) 
<?php

class Paciente {
    public $nombre;
    public $dni;
    public $urgencia;

    public function __construct($nombre, $dni, $urgencia) {
        $this->nombre = $nombre;
        $this->dni = $dni;
        $this->urgencia = $urgencia;
    }

    public function __toString() {
        return "{$this->nombre} (DNI: {$this->dni}) - Urgencia: {$this->urgencia}";
    }
}

class Turnero {
    private $cola_turnos = [];       // Cola de prioridad (array de arrays: [urgencia, contador, paciente])
    private $entry_finder = [];      // Mapear DNI a entrada
    private $contador = 0;

    public function solicitar_turno(Paciente $paciente) {
        if (isset($this->entry_finder[$paciente->dni])) {
            echo "Este paciente ya tiene un turno.\n";
            return;
        }

        $entrada = [
            'urgencia' => $paciente->urgencia,
            'contador' => $this->contador++,
            'paciente' => $paciente
        ];

        $this->cola_turnos[] = $entrada;
        $this->entry_finder[$paciente->dni] = $entrada;

        echo "Turno asignado a {$paciente->nombre} con prioridad {$paciente->urgencia}\n";
    }

    public function llamar_siguiente() {
        if (empty($this->cola_turnos)) {
            echo "No hay pacientes en espera.\n";
            return null;
        }

        // Ordenar por urgencia y contador
        usort($this->cola_turnos, function ($a, $b) {
            if ($a['urgencia'] === $b['urgencia']) {
                return $a['contador'] <=> $b['contador'];
            }
            return $a['urgencia'] <=> $b['urgencia'];
        });

        foreach ($this->cola_turnos as $i => $entrada) {
            $paciente = $entrada['paciente'];
            if (isset($this->entry_finder[$paciente->dni])) {
                unset($this->entry_finder[$paciente->dni]);
                array_splice($this->cola_turnos, $i, 1); // Eliminar del array
                echo "Llamando a: $paciente\n";
                return $paciente;
            }
        }

        echo "No hay pacientes en espera.\n";
        return null;
    }
}

// Ejemplo de uso
$turnero = new Turnero();

$p1 = new Paciente("Ana", "123", 2);
$p2 = new Paciente("Juan", "456", 1);
$p3 = new Paciente("Luis", "789", 3);

$turnero->solicitar_turno($p1);
$turnero->solicitar_turno($p2);
$turnero->solicitar_turno($p3);

$turnero->llamar_siguiente();  // Juan
$turnero->llamar_siguiente();  // Ana
$turnero->llamar_siguiente();  // Luis
$turnero->llamar_siguiente();  // No hay pacientes

?>
