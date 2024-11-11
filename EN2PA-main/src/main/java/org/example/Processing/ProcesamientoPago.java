package org.example.Processing;


public class ProcesamientoPago extends Tarea {

    public ProcesamientoPago(int pedido, boolean isUrgente) {
        super(pedido, isUrgente);
    }



    @Override
    public void run() {
        try {
            System.out.println(this.pedido + " Pago en ejecucion :" + this.isUrgente);
            Thread.sleep(20);
            System.out.println(this.pedido + " Pago completed :" + this.isUrgente);
        }catch (InterruptedException interruptedException){
            Thread.currentThread().interrupt();
            throw new RuntimeException(interruptedException);
        }
    }

}
