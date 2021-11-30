package lab4.macwozni.dmeshparallel.parallelism;

import lab4.macwozni.dmeshparallel.production.IProduction;

public class ConcurentBlockRunner extends AbstractBlockRunner {

    private final MyLock lock = new MyLock();

    @Override
    void runOne(IProduction _pOne) {
        _pOne.injectRefs(lock);
        _pOne.start();
    }

    @Override
    void wakeAll() {
        lock.unlock();
    }

}
