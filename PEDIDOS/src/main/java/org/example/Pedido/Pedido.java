package org.example.Pedido;

public class Pedido {
    private int id;
    private boolean urgente;

    public Pedido(int id, boolean urgente) {
        this.id = id;
        this.urgente = urgente;
    }

    public boolean isUrgente() {

        return urgente;
    }
    public int getId() {
        return id;
    }
}
