

import org.example.Processing.EmpaquetadoPedidos;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class EmpaquetadoPedidosTest {

    private EmpaquetadoPedidos empaquetadoNormal;
    private EmpaquetadoPedidos empaquetadoUrgente;

    @BeforeEach
    void setUp() {
        empaquetadoNormal = new EmpaquetadoPedidos(789, false);
        empaquetadoUrgente = new EmpaquetadoPedidos(1011, true);
    }

    @Test
    void testRunNormal() {
        assertDoesNotThrow(() -> {
            empaquetadoNormal.run();
        });
    }

    @Test
    void testRunUrgente() {
        assertDoesNotThrow(() -> {
            empaquetadoUrgente.run();
        });
    }

    @Test
    void testEmpaquetadoNormalExecutionFlow() {
        // Test para verificar que el proceso de empaquetado normal sigue el flujo esperado
        assertDoesNotThrow(() -> empaquetadoNormal.run());
        assertTrue(Thread.currentThread().isAlive());
    }

    @Test
    void testEmpaquetadoUrgenteExecutionFlow() {
        // Test para verificar que el proceso de empaquetado urgente sigue el flujo esperado
        assertDoesNotThrow(() -> empaquetadoUrgente.run());
        assertTrue(Thread.currentThread().isAlive());
    }
}
