package org.example.Processing;

public abstract class Tarea implements Comparable<Tarea>, Runnable {
    protected int pedido;
    protected int isUrgente;

    public Tarea(int pedido, boolean isUrgente) {
        this.pedido = pedido;
        this.isUrgente = isUrgente ? 0 : 1;
    }

    @Override
    public int compareTo(Tarea other) {
        return Integer.compare(this.isUrgente, other.isUrgente);
    }
}