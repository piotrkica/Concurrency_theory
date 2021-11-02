package agh.cs.lab2.zad3;

class BinSemaphore {
    public volatile boolean state = true;

    public BinSemaphore() {}

    public synchronized void P(){
        while (!state) {
            try {
                this.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        state = false;
        this.notify();
    }

    public synchronized void V() {
        state = true;
        this.notify();
    }
}