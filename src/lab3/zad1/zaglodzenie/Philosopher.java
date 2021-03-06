package lab3.zad1.zaglodzenie;

public class Philosopher extends Thread{
    private final int id;
    private final Table table;
    private final int totalMeals;
    public long totalWaitTime = 0;

    public Philosopher(int id, Table table, int totalMeals){
        this.id = id;
        this.table = table;
        this.totalMeals = totalMeals;
    }

    public void run() {
        int i = 0;
        Fork leftFork = table.getLeftFork(id);
        Fork rightFork = table.getRightFork(id);
        for (int meals = 0; meals < totalMeals; meals++) {  //while(true)
            long startTime = System.currentTimeMillis();
            while (true) {
                try {
                    leftFork.sem.acquire();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                if (rightFork.sem.tryAcquire()){
                        System.out.println("Filozof ID=" + id + ": Mam widelce " + leftFork.id + " i " + rightFork.id);
                        break;
                }
                else{
                    leftFork.sem.release();
                }
            }
            totalWaitTime += System.currentTimeMillis() - startTime;
            try {
                System.out.println("Filozof ID=" + id + ": Jem po raz " + i);
                i++;
                sleep(100);
                System.out.println("Filozof ID=" + id + ": Ale pojadłem, odkładam widelce");
                leftFork.sem.release();
                rightFork.sem.release();
                sleep(0);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
