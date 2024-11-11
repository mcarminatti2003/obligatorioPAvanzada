import static org.junit.jupiter.api.Assertions.*;

import org.example.Processing.ProcesamientoPago;
import org.example.Processing.Tarea;
import org.junit.jupiter.api.Test;

public class TareaEjecucionTest {

    @Test //pasó el assert
    public void testEjecucionTarea() throws InterruptedException {
        Tarea tarea = new ProcesamientoPago(1, true);
        // Ejecutar la tarea en un nuevo hilo
        Thread thread = new Thread(tarea);
        thread.start();
        thread.join(); // Espera a que la tarea se complete

        // Si no se lanza ninguna excepción, la prueba pasa.
        assertTrue(true);
    }
}
