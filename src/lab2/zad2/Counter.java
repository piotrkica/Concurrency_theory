package lab2.zad2;

public class Counter {
    public int counter = 0;

    public void add(int val){
        counter += val;
    }
}

class ThreadAdd extends Thread
{
    private final int val;
    private final Counter counter;
    private final static BadBinSemaphore sem = new BadBinSemaphore();

    ThreadAdd(int value, Counter obj) {
        val = value;
        counter = obj;
    }

    public void run() {
        for (long i = 0; i < 10e5; i++) {
            sem.P();
            counter.add(val);
            sem.V();
        }
    }
}

