import org.example.Pedido.Pedido;
import org.example.Processing.ProcesadorPedidos;
import org.junit.Test;

import java.util.concurrent.atomic.AtomicInteger;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ProcesadorPedidosTest {

    @Test
    public void testProcesarPedido() {
        ProcesadorPedidos procesador = new ProcesadorPedidos();
        AtomicInteger contador = new AtomicInteger();

        // Crear una clase anónima que incrementa el contador
        class TestTask implements Runnable {
            @Override
            public void run() {
                contador.incrementAndGet();
            }
        }

        // Crear un Pedido
        Pedido pedidoNoUrgente = new Pedido(1, false);
        Pedido pedidoUrgente = new Pedido(2, true);

        // Reemplazar las tareas originales con tareas de prueba
        procesador.procesarPedido(new Pedido(1, false) {

            public Runnable crearProcesamientoPago() {
                return new TestTask();
            }


            public Runnable crearEmpaquetadoPedidos() {
                return new TestTask();
            }

            public Runnable crearEnvio() {
                return new TestTask();
            }
        });

        // Simular otro pedido urgente
        procesador.procesarPedido(new Pedido(2, true) {

            public Runnable crearProcesamientoPago() {
                return new TestTask();
            }


            public Runnable crearEmpaquetadoPedidos() {
                return new TestTask();
            }

            public Runnable crearEnvio() {
                return new TestTask();
            }
        });

        // Esperar a que se terminen las tareas
        procesador.shutdown();

        // Verificar que se procesaron 6 tareas en total (3 por pedido)
        assertEquals(6, contador.get());
    }
}


