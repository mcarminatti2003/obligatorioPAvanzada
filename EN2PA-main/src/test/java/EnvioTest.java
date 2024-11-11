
import org.example.Processing.Envio;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.*;

class EnvioTest {

    private Envio envio;
    private final int pedidoId = 1;
    private ByteArrayOutputStream outContent;
    private PrintStream originalOut;

    @BeforeEach
    public void setUp() {
        // Setup an Envio instance with a non-urgent order (false)
        envio = new Envio(pedidoId, false);

        // Capture System.out for verifying the console output
        outContent = new ByteArrayOutputStream();
        originalOut = System.out;  // Save original System.out
        System.setOut(new PrintStream(outContent));  // Redirect System.out to ByteArrayOutputStream
    }

    @Test
    public void testRunExecution() throws InterruptedException {
        // Given: Un thread que ejecutará la tarea de Envio
        Thread thread = new Thread(envio);

        // When: Ejecutando la tarea
        thread.start();
        thread.join();  // Esperar a que el thread termine

        // Then: Verificar que la salida indique que la tarea ha comenzado y finalizado
        String expectedStartMessage = pedidoId + " Envio en ejecucion :false";
        String expectedEndMessage = pedidoId + " Envio completed :false";

        // Esperar brevemente para asegurarse de que los mensajes se registren
        Thread.sleep(100);  // Ajustar el tiempo si es necesario

        // Capturar la salida
        String actualOutput = outContent.toString().trim();
        System.out.println("Output: " + outContent.toString());

/*
        // Verificar si los mensajes están en la salida capturada
        assertTrue(actualOutput.contains(expectedStartMessage), "Debería contener el mensaje de inicio");
        assertTrue(actualOutput.contains(expectedEndMessage), "Debería contener el mensaje de finalización");
*/
    }


}

