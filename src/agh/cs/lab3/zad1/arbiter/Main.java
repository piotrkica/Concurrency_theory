package agh.cs.lab3.zad1.arbiter;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        int N = 5;
        int totalMeals = 30;
        long[] waitTimes = new long[N];

        Table table = new Table(N);

        Philosopher[] phils = new Philosopher[N];
        for (int id = 0; id < N; id++)
            phils[id] = new Philosopher(id, table, totalMeals);

        for (int id = 0; id < N; id++)
            phils[id].start();

        for (int id = 0; id < N; id++)
            phils[id].join();

        for (int id = 0; id < N; id++)
            waitTimes[id] += phils[id].totalWaitTime;


        for (int id = 0; id < N; id++)
            System.out.println("Filozof ID=" + id + " czekał średnio " + waitTimes[id]/1.0/totalMeals);
    }
}

