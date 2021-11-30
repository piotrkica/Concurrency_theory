package lab4.macwozni.dmeshparallel.myProductions;

import lab4.macwozni.dmeshparallel.mesh.Vertex;
import lab4.macwozni.dmeshparallel.production.AbstractProduction;

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
