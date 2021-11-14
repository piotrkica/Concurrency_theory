package agh.cs.lab3.zad1.arbiter;

import java.util.concurrent.Semaphore;

public class Fork {
    public int id;
    public Semaphore sem = new Semaphore(1);

    public Fork(int id) {
        this.id = id;
    }
}
