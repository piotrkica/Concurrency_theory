package agh.cs.lab4.macwozni.dmeshparallel.parallelism;

import agh.cs.lab4.macwozni.dmeshparallel.production.IProduction;

public class SerialBlockRunner extends AbstractBlockRunner {

    private final MyLock lock = new MyLock();

    @Override
    void runOne(IProduction _pOne) {
        _pOne.injectRefs(lock);
        _pOne.start();
        lock.unlock();
    }

    @Override
    void wakeAll() {
        //do nothing
    }

}
