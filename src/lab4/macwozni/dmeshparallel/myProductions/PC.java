package lab4.macwozni.dmeshparallel.myProductions;

import lab4.macwozni.dmeshparallel.mesh.Vertex;
import lab4.macwozni.dmeshparallel.production.AbstractProduction;

public class PC extends AbstractProduction<Vertex> {

    public PC(Vertex _obj) {
        super(_obj, null);
    }

    @Override
    public Vertex apply(Vertex t1) {
        System.out.println("pc");
        Vertex t2 = t1.getUp().getRight().getDown();
        t1.setRight(t2);
        t2.setLeft(t1);
        return t1;
    }
}
