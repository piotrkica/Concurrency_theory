package agh.cs.lab2.zad2;

class BadBinSemaphore {
    public volatile boolean state = true;

    public BadBinSemaphore() {}

    public synchronized void P(){
        if (!state) {
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