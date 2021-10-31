package agh.cs.lab1;

public class Counter {
    public int counter = 0;

    public void add(int val){
        counter += val;
    }

}

class ThreadAdd extends Thread {
    private final int val;
    private final Counter counter;

    ThreadAdd(int value, Counter obj) {
        val = value;
        counter = obj;
    }


    public void run() {
//        synchronized(counter) {
            for (long i = 0; i < 10e8; i++) {
                counter.add(val);
            }
//        }
    }
}

