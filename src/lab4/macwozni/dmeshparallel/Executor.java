package lab4.macwozni.dmeshparallel;

import lab4.macwozni.dmeshparallel.myProductions.PC;
import lab4.macwozni.dmeshparallel.myProductions.PS;
import lab4.macwozni.dmeshparallel.myProductions.PW;
import lab4.macwozni.dmeshparallel.mesh.Vertex;
import lab4.macwozni.dmeshparallel.mesh.GraphDrawer;
import lab4.macwozni.dmeshparallel.parallelism.BlockRunner;
import lab4.macwozni.dmeshparallel.production.PDrawer;

import java.util.ArrayList;
import java.util.Iterator;

public class Executor extends Thread {

    private final BlockRunner runner;
    private final int n;

    public Executor(BlockRunner _runner, int _n) {
        this.runner = _runner;
        this.n = _n;
    }

    @Override
    public void run() {

        PDrawer drawer = new GraphDrawer();
        //axiom
        Vertex s = new Vertex(null, null, null, null, "M");  // initial production

        ArrayList<Vertex> southVertices = new ArrayList<Vertex>();  // array to store lowest vertices in column (for next PS productions)
        ArrayList<Vertex> southVerticesCopy = new ArrayList<Vertex>();  // array to handle concurrent modification
        ArrayList<Vertex> pcProductionVertices = new ArrayList<Vertex>();  // vertices to run PC productions on
        southVertices.add(s);

        Vertex leftmost = s;
        int run_no = 1;

        for (int i = 1; i < n; i++) {
            // PW PRODUCTION
            PW pw = new PW(leftmost);
            this.runner.addThread(pw);

            // PS PRODUCTIONS
            for (Vertex southVertex : southVertices) {
                PS ps = new PS(southVertex);
                this.runner.addThread(ps);
            }

            // PC PRODUCTIONS
            for (Vertex pcProductionVertex : pcProductionVertices) {
                PC pc = new PC(pcProductionVertex);
                this.runner.addThread(pc);
            }
            // START THREADS
            System.out.println("Run " + run_no++);
            this.runner.startAll();

            // UPDATE ARRAYS AND LEFTMOST VERTEX
            leftmost = leftmost.getLeft();
            for (Vertex southVertex : southVertices) {
                southVerticesCopy.add(southVertex.getDown());
            }
            southVerticesCopy.add(leftmost);
            southVertices = southVerticesCopy;
            southVerticesCopy = new ArrayList<Vertex>();

            // UPDATE PC PRODUCTION ARRAY BY DROPPING FIRST AND LAST SOUTH VERTEX
            if (southVertices.size() >= 3) {
                pcProductionVertices = (ArrayList<Vertex>) southVertices.clone();
                pcProductionVertices.remove(0);
                pcProductionVertices.remove(pcProductionVertices.size() - 1);
            }
        }

        southVertices.remove(0);

        for (int i = n - 1; i > 0; i--) {
            // PC PRODUCTIONS
            for (Vertex pcProductionVertex : pcProductionVertices) {
                PC pc = new PC(pcProductionVertex);
                this.runner.addThread(pc);
            }
            // PS PRODUCTIONS
            Iterator<Vertex> foreach = southVertices.iterator();
            while (foreach.hasNext()) {
                PS ps = new PS(foreach.next());
                this.runner.addThread(ps);
            }
            // START THREADS
            System.out.println("Run " + run_no++);
            this.runner.startAll();

            // UPDATE ARRAYS
            Vertex tmpForPCList = southVertices.get(0);  // lowest vertex in array should get a PC production next run
            southVertices.remove(0);  // skip the lowest vertex each iteration because it would go over n-elements down

            foreach = southVertices.iterator();
            while (foreach.hasNext()) {
                southVerticesCopy.add(foreach.next().getDown());
            }

            southVertices = southVerticesCopy;
            southVerticesCopy = new ArrayList<Vertex>();

            pcProductionVertices = (ArrayList<Vertex>) southVertices.clone();
            pcProductionVertices.add(tmpForPCList.getDown());

            // last iteration -> run only one PC production
            if (i == 1) {
                PC pc = new PC(tmpForPCList.getDown());
                this.runner.addThread(pc);
                System.out.println("Run " + run_no++);
                this.runner.startAll();
            }

        }

        drawer.draw(s);

    }
}
