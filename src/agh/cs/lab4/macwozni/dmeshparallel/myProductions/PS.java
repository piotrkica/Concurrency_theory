package agh.cs.lab4.macwozni.dmeshparallel.myProductions;

import agh.cs.lab4.macwozni.dmeshparallel.mesh.Vertex;
import agh.cs.lab4.macwozni.dmeshparallel.production.AbstractProduction;
import agh.cs.lab4.macwozni.dmeshparallel.production.PDrawer;

public class PS extends AbstractProduction<Vertex> {

    public PS(Vertex _obj) {
        super(_obj, null);
    }

    @Override
    public Vertex apply(Vertex s) {
        System.out.println("ps");
        Vertex t1 = new Vertex(null, null,s, null, "M");
        s.setDown(t1);
        return t1;
    }

}
