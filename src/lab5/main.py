from src.utils import *

if __name__ == "__main__":
    alphabet = {"x", "y", "z", "v"}
    a = Transaction("a", "x = 0", alphabet)
    b = Transaction("b", "x = x * y", alphabet)
    c = Transaction("c", "x = x + 2", alphabet)
    d = Transaction("d", "y = 1", alphabet)
    e = Transaction("e", "y = y - z", alphabet)
    f = Transaction("f", "z = z * v", alphabet)
    g = Transaction("g", "z = v + y", alphabet)
    h = Transaction("h", "v = z - v", alphabet)
    transactions = [a, b, c, d, e, f, g, h]

    # alphabet, transactions = from_file("input.txt")  # alternative
    D, I = D_I_relations(transactions)
    print("D =", D)
    print("I =", I)
    G = diekertGraph("adhcbgfae", D)
    draw_graph(G)
    print("FNF_graph =", FNF_graph(G))
    print("FNF_word =", FNF_word("adhcbgfae", D))

    # calc_and_save(transactions, "adhcbgfae", "output.txt", "graph.dot")
