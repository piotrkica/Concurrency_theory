package agh.cs.lab3.zad1.zaglodzenie;

public class Table {
    private final Fork[] forks;
    private final int fork_no;

    public Table(int n){
        forks = new Fork[n];
        for (int i = 0; i < n; i++){
            forks[i] = new Fork(i);
        }
        fork_no = n;
    }

    public Fork getLeftFork(int id) {
        return forks[id];
    }

    public Fork getRightFork(int id) {
        return  forks[(id + 1) % fork_no];
    }


}
