package agh.cs.lab2.zad2;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        // Jeśli jeden wątek aktywnie czeka na dostęp do zmiennej to po notify musi jeszcze raz sprawdzić czy
        // w międzyczasie inny wątek go nie zdążył wyprzedzić w dostępie do zmiennej.
        // W implementacji z if-em nie sprawdzi tego i nadpisze zmiany drugiego wątku co powoduje,
        // że w naszym wyścigu counter != 0 na koniec. Co więcej, jak mamy wiele wątków
        // i jeśli wysyłamy notifyAll() to wtedy każdy wątek przestanie czekać i wejdzie do sekcji krytycznej.

        Counter counter = new Counter();
        ThreadAdd thread1 = new ThreadAdd(1, counter);
        ThreadAdd thread2 = new ThreadAdd(-1, counter);

        thread1.start();
        thread2.start();
        thread1.join();
        thread2.join();

        System.out.println("Counter = " + counter.counter);

    }
}

