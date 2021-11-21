package agh.cs.lab4.macwozni.dmeshparallel.myProductions;

import agh.cs.lab4.macwozni.dmeshparallel.mesh.Vertex;
import agh.cs.lab4.macwozni.dmeshparallel.production.AbstractProduction;
import agh.cs.lab4.macwozni.dmeshparallel.production.PDrawer;

public class PW extends AbstractProduction<Vertex> {

    public PW(Vertex _obj) {
        super(_obj, null);
    }

    @Override
    public Vertex apply(Vertex s) {
        System.out.println("pw");
        Vertex t1 = new Vertex(null, s,null, null, "M");
        s.setLeft(t1);
        return t1;
    }

}
