package agh.cs.lab2.zad3;


class CountSemaphore {
    // source: http://www.cs.umd.edu/~shankar/412-Notes/10x-countingSemUsingBinarySem.pdf
    // Tak, semafor binarny to szczególny przypadek semafora ogólnego, wtedy count = 1.
    private int count;
    private final BinSemaphore countLock = new BinSemaphore();
    private final BinSemaphore sectionLock = new BinSemaphore();

    public CountSemaphore(int max_count){
        count = max_count;
    }

    public void P(){
        sectionLock.P();
        countLock.P();
        count--;
        if (count > 0){
            sectionLock.V();
        }
        countLock.V();
    }

    public void V(){
        countLock.P();
        count++;
        if (count == 1){
            sectionLock.V();
        }
        countLock.V();
    }

    public int availablePermits() {
        countLock.P();
        int c = count;
        countLock.V();
        return c;
    }
}
