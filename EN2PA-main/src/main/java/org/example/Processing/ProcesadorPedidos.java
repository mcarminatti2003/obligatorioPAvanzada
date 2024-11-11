package org.example.Processing;

import org.example.Pedido.Pedido;

import java.util.concurrent.*;

public class ProcesadorPedidos {
    private final ExecutorService executor;

    public ProcesadorPedidos() {
        PriorityBlockingQueue<Runnable> queue = new PriorityBlockingQueue<>();
        executor = new ThreadPoolExecutor(1, 300, 0L, TimeUnit.MILLISECONDS, new PriorityBlockingQueue<Runnable>());
    }



    public void procesarPedido(Pedido pedido) {
        executor.execute(new ProcesamientoPago(pedido.getId(), pedido.isUrgente()));
        executor.execute(new EmpaquetadoPedidos(pedido.getId(), pedido.isUrgente()));
        executor.execute(new Envio(pedido.getId(), pedido.isUrgente()));
    }

    public void shutdown() {
        executor.shutdown();
        try {
            if (!executor.awaitTermination(60, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }
}
