package org.example.Processing;

import org.example.Pedido.Pedido;

public class Envio extends Tarea {

    public Envio(int pedido, boolean isUrgente) {
        super(pedido, isUrgente);
    }



    @Override
    public void run() {
        try {
            System.out.println(this.pedido + " Envio en ejecucion :" + this.isUrgente);
            Thread.sleep(20);
            System.out.println(this.pedido + " Envio completed :" + this.isUrgente);
        }catch (InterruptedException interruptedException){
            Thread.currentThread().interrupt();
            throw new RuntimeException(interruptedException);
        }
    }
}
