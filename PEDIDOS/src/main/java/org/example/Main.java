package org.example;

import org.example.Pedido.Pedido;
import org.example.Processing.ProcesadorPedidos;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread.sleep(5000); //Para activar jconsole
        ProcesadorPedidos procesador = new ProcesadorPedidos();

        // Crear y procesar 50 pedidos
        for (int i = 1; i <= 200; i++) {
            boolean esUrgente = (i % 5 == 0); // Cada quinto pedido es urgente
            Pedido pedido = new Pedido(i, esUrgente);
            procesador.procesarPedido(pedido);
        }

        // Cerrar el sistema
        procesador.shutdown();
    }
}
