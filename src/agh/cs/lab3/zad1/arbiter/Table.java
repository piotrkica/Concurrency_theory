package agh.cs.lab3.zad1.arbiter;

import java.util.concurrent.Semaphore;

public class Table {
    private final Fork[] forks;
    private final int fork_no;
    public final Semaphore arbitratorSem;

    public Table(int n){
        forks = new Fork[n];
        for (int i = 0; i < n; i++){
            forks[i] = new Fork(i);
        }
        fork_no = n;
        arbitratorSem = new Semaphore(n - 1);
    }

    public Fork getLeftFork(int id) {
        return forks[id];
    }

    public Fork getRightFork(int id) {
        return forks[(id + 1) % fork_no];
    }

}
