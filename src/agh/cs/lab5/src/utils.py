from matplotlib import pyplot as plt

from src.trace_theory import *
from src.transaction import Transaction


def draw_graph(G: nx.DiGraph):
    """
    Plot graph, each color represents one layer
    :param G: Diekert's graph
    """
    color_map = [G.nodes[node]["layer"] for node in G]
    plt.title("Diekert's Graph")
    pos = nx.multipartite_layout(G, subset_key="layer")
    nx.draw(G, pos, node_color=color_map, with_labels=True, font_weight='bold')
    # plt.savefig('graph.png')
    plt.show()


def from_file(filename: str) -> [set, list]:
    """
    Read and parse file contents.
    First line must be alphabet
    Second line is empty
    Next lines are transactions definitions
    :param filename: file location
    :return: alphabet, transactions
    """
    with open(filename) as file:
        lines = file.readlines()

    alphabet = {*lines[0][:-1].split(" ")}
    transactions = []
    for line in lines[2:]:
        if len(line) > 3:
            transactions.append(Transaction(line[:1], line[2:], alphabet))

    return alphabet, transactions


def calc_and_save(transactions: list, word: str, D_I_FNF_filename: str, graph_filename: str):
    """
    Calculate Dependency, Independence relations, FNF, Diekert's Graph and save to files
    :param transactions: list of transactions
    :param word: word from alphabet
    :param D_I_FNF_filename: filename for calculated relations and FNF
    :param graph_filename: filename to save graph in .dot format
    """
    D, I = D_I_relations(transactions)
    G = diekertGraph(word, D)
    FNF = FNF_graph(G)

    with open(D_I_FNF_filename, 'w+') as file:
        file.write("D = " + str(D) + "\n")
        file.write("I = " + str(I) + "\n")
        file.write("FNF = " + str(FNF) + "\n")

    nx.nx_agraph.write_dot(G, graph_filename)

