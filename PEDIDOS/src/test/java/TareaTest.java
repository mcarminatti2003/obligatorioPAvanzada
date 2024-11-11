import org.example.Processing.EmpaquetadoPedidos;
import org.example.Processing.ProcesamientoPago;
import org.example.Processing.Tarea;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class TareaTest {

    @Test
    public void testCompararTareasUrgentes() {
        Tarea tarea1 = new ProcesamientoPago(1, true);
        Tarea tarea2 = new ProcesamientoPago(2, false);
        assertTrue(tarea1.compareTo(tarea2) < 0); // tarea1 es urgente, debe ser menor que tarea2
    }

    @Test
    public void testCompararTareasNoUrgentes() {
        Tarea tarea1 = new EmpaquetadoPedidos(1, false);
        Tarea tarea2 = new EmpaquetadoPedidos(2, false);
        assertEquals(0, tarea1.compareTo(tarea2)); // Ambas no son urgentes, deben ser iguales
    }
}
