

import org.example.Processing.ProcesamientoPago;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ProcesamientoPagoTest {

    private ProcesamientoPago procesamientoPagoNormal;
    private ProcesamientoPago procesamientoPagoUrgente;

    @BeforeEach
    void setUp() {
        procesamientoPagoNormal = new ProcesamientoPago(1, false);
        procesamientoPagoUrgente = new ProcesamientoPago(2, true);
    }

    @Test
    void testRunNormal() {
        assertDoesNotThrow(() -> {
            procesamientoPagoNormal.run();
        });
    }

    @Test
    void testRunUrgente() {
        assertDoesNotThrow(() -> {
            procesamientoPagoUrgente.run();
        });
    }

    @Test
    void testPagoNormalExecutionFlow() {
        assertDoesNotThrow(() -> procesamientoPagoNormal.run());
        assertTrue(Thread.currentThread().isAlive());
    }

    @Test
    void testPagoUrgenteExecutionFlow() {
        assertDoesNotThrow(() -> procesamientoPagoUrgente.run());
        assertTrue(Thread.currentThread().isAlive());
    }
}
