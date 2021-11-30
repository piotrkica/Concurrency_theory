import unittest
from src.trace_theory import *
from src.transaction import Transaction


class MyTestCase(unittest.TestCase):
    def setUp_1(self):  # case from classes
        alphabet = {"x", "y", "z", "v"}
        a = Transaction("a", "x = 0", alphabet)
        b = Transaction("b", "x = x * y", alphabet)
        c = Transaction("c", "x = x + 2", alphabet)
        d = Transaction("d", "y = 1", alphabet)
        e = Transaction("e", "y = y - z", alphabet)
        f = Transaction("f", "z = z * v", alphabet)
        g = Transaction("g", "z = v + y", alphabet)
        h = Transaction("h", "v = z - v", alphabet)

        return [a, b, c, d, e, f, g, h]

    def setUp_2(self):  # case 1 from .pdf
        alphabet = {"x", "y", "z", "v"}
        a = Transaction("a", "x = x + y", alphabet)
        b = Transaction("b", "y = y + 2z", alphabet)
        c = Transaction("c", "x = 3x + z", alphabet)
        d = Transaction("d", "z = y - z", alphabet)

        return [a, b, c, d]

    def test_D_I_relations_1(self):
        transactions = self.setUp_1()

        D, I = D_I_relations(transactions)
        self.assertSetEqual(D, {
            ('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'a'),
            ('c', 'b'), ('c', 'c'), ('d', 'b'), ('d', 'd'), ('d', 'e'), ('d', 'g'), ('e', 'b'), ('e', 'd'), ('e', 'e'),
            ('e', 'f'), ('e', 'g'), ('f', 'e'), ('f', 'f'), ('f', 'g'), ('f', 'h'), ('g', 'd'), ('g', 'e'), ('g', 'f'),
            ('g', 'g'), ('g', 'h'), ('h', 'f'), ('h', 'g'), ('h', 'h')
        })
        self.assertSetEqual(I, {
            ('a', 'd'), ('a', 'e'), ('a', 'f'), ('a', 'g'), ('a', 'h'), ('b', 'f'), ('b', 'g'), ('b', 'h'), ('c', 'd'),
            ('c', 'e'), ('c', 'f'), ('c', 'g'), ('c', 'h'), ('d', 'a'), ('d', 'c'), ('d', 'f'), ('d', 'h'), ('e', 'a'),
            ('e', 'c'), ('e', 'h'), ('f', 'a'), ('f', 'b'), ('f', 'c'), ('f', 'd'), ('g', 'a'), ('g', 'b'), ('g', 'c'),
            ('h', 'a'), ('h', 'b'), ('h', 'c'), ('h', 'd'), ('h', 'e')
        })

    def test_D_I_relations_2(self):
        transactions = self.setUp_2()

        D, I = D_I_relations(transactions)

        self.assertSetEqual(D, {('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'd'), ('c', 'a'),
                                ('c', 'c'), ('c', 'd'), ('d', 'b'), ('d', 'c'), ('d', 'd')})
        self.assertSetEqual(I, {('a', 'd'), ('b', 'c'), ('c', 'b'), ('d', 'a')})

    def test_FNF_graph_1(self):
        transactions = self.setUp_1()

        D, I = D_I_relations(transactions)
        G = diekertGraph("adhcbgfae", D)
        FNF = FNF_graph(G)

        self.assertEqual(FNF, {0: ["a", "d", "h"], 1: ["c", "g"], 2: ["b", "f"], 3: ["a", "e"]})

    def test_FNF_graph_2(self):
        transactions = self.setUp_2()

        D, I = D_I_relations(transactions)
        G = diekertGraph("baadcb", D)
        FNF = FNF_graph(G)

        self.assertEqual(FNF, {0: ["b"], 1: ["a", "d"], 2: ["a"], 3: ["c", "b"]})

    def test_FNF_word_1(self):
        transactions = self.setUp_1()

        D, I = D_I_relations(transactions)
        FNF = FNF_word("adhcbgfae", D)

        self.assertEqual(FNF, {0: ["a", "d", "h"], 1: ["c", "g"], 2: ["b", "f"], 3: ["a", "e"]})

    def test_FNF_word_2(self):
        transactions = self.setUp_2()

        D, I = D_I_relations(transactions)
        FNF = FNF_word("baadcb", D)

        self.assertEqual(FNF, {0: ["b"], 1: ["a", "d"], 2: ["a"], 3: ["c", "b"]})


if __name__ == '__main__':
    unittest.main()
