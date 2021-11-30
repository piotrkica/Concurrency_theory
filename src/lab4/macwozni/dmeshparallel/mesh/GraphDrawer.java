package lab4.macwozni.dmeshparallel.mesh;

import lab4.macwozni.dmeshparallel.production.PDrawer;

public class GraphDrawer implements PDrawer<Vertex> {

    @Override
    public void draw(Vertex start) {
        System.out.print("\n");
        Vertex v = start;
        while (v.mUp != null) {  // find top left corner
            v = v.mUp;
        }
        while (v.mLeft != null) {  // find top left corner
            v = v.mLeft;
        }
        start = v;
        while (v != null) {
            while (v != null) {  // draw M-row
                Vertex mRight = v.mRight;
                if (v.mRight != null) {
                    System.out.print(v.mLabel + "--");
                } else {  // last vertex in row
                    System.out.print(v.mLabel);
                }
                v = mRight;
            }
            if (start.mDown != null) {  // draw row with |
                System.out.print("\n");
                v = start;
                while (v != null) {
                    System.out.print("|  ");
                    v = v.mRight;
                }
                System.out.print("\n");
            }
            start = start.mDown; // go one M-row down
            v = start;
        }
        System.out.print("\n");
    }
}