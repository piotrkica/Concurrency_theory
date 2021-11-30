package lab1;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        ThreadAdd thread1 = new ThreadAdd(1, counter);
        ThreadAdd thread2 = new ThreadAdd(-1, counter);

        long startTime = System.currentTimeMillis();
        thread1.start();
        thread2.start();
        thread1.join();
        thread2.join();
        long estimatedTime = System.currentTimeMillis() - startTime;

        System.out.println("Counter = " + counter.counter);
        System.out.println("Exec time = " + estimatedTime/1000.0);

    }
}

