package org.example.Processing;


import org.example.Pedido.Pedido;

public class EmpaquetadoPedidos extends Tarea {

    public EmpaquetadoPedidos(int pedido, boolean isUrgente) {
        super(pedido, isUrgente);
    }

    @Override
    public void run() {
        try {
            System.out.println(this.pedido + " Empaquetado en proceso:" + this.isUrgente);
            Thread.sleep(20);
            System.out.println(this.pedido + " Empaquetado completed :" + this.isUrgente);
        }catch (InterruptedException interruptedException){
            Thread.currentThread().interrupt();
            throw new RuntimeException(interruptedException);
        }
    }
}
