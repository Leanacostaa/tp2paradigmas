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



codigo en php(este codigo vamos a usar para enlazar) 
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
}

class Turnero {
    private $cola = [];

    public function solicitar_turno(Paciente $paciente) {
        $this->cola[] = $paciente;
        // Ordena por urgencia (menor número = mayor prioridad)
        usort($this->cola, function($a, $b) {
            return $a->urgencia <=> $b->urgencia;
        });
    }

    public function llamar_siguiente() {
        if (empty($this->cola)) {
            echo "No hay pacientes en espera.\n";
        } else {
            $paciente = array_shift($this->cola);
            echo "Llamando a: {$paciente->nombre} (Urgencia: {$paciente->urgencia})\n";
        }
    }
}

// Uso del sistema
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
$turnero->llamar_siguiente();  // No hay pacientes_
