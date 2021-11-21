package agh.cs.lab4.macwozni.dmeshparallel.parallelism;

import agh.cs.lab4.macwozni.dmeshparallel.production.IProduction;

public interface BlockRunner {

    //starts all threads
    public void startAll();

    //adds a thread to poll
    public void addThread(IProduction pThread);
}
