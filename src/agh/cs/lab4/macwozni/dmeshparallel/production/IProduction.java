package agh.cs.lab4.macwozni.dmeshparallel.production;

import agh.cs.lab4.macwozni.dmeshparallel.parallelism.MyLock;

public interface IProduction<P> {

    public P apply(P _p);

    public void join() throws InterruptedException;

    public void start();

    public void injectRefs(MyLock _lock);

    public P getObj();
}
