import org.example.Pedido.Pedido;
import org.junit.Test;

import static org.junit.jupiter.api.Assertions.*;

public class PedidoTest {
    @Test //pasó
    public void testCrearPedido() {
        Pedido pedido = new Pedido(1, true);
        assertEquals(1, pedido.getId());
        assertTrue(pedido.isUrgente());
    }

    @Test //pasó
    public void testNoUrgente() {
        Pedido pedido = new Pedido(2, false);
        assertEquals(2, pedido.getId());
        assertFalse(pedido.isUrgente());
    }
}
