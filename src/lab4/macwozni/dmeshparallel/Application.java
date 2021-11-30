package lab4.macwozni.dmeshparallel;

import lab4.macwozni.dmeshparallel.parallelism.ConcurentBlockRunner;

// source https://github.com/macwozni/1DMeshParallel

class Application {

    public static void main(String args[]) {

        int n = 10;
        Executor e = new Executor(new ConcurentBlockRunner(), n);
        e.start();
    }
}
