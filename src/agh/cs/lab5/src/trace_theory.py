import networkx as nx


def D_I_relations(transactions: list) -> (set, set):
    """
    Determines Dependency and Independence relations from list of transactions
    :param transactions: list of transaction objects
    :return: dependency set and independence set of transaction
    """
    D_set = set()

    for i in range(len(transactions)):
        for j in range(i, len(transactions)):  # for each transaction
            a = transactions[i]
            b = transactions[j]
            if a.left in b.right or b.left in a.right:  # if one's right side updates other's left side
                D_set.add((a, b))
                D_set.add((b, a))

    Ia_set = {(t, t) for t in transactions}  # self dependency
    D_set = D_set.union(Ia_set)
    I_set = {(t1, t2) for t1 in transactions for t2 in transactions}.difference(D_set)

    D = {(t[0].name, t[1].name) for t in D_set}
    I = {(t[0].name, t[1].name) for t in I_set}
    # D = sorted([(t[0].name, t[1].name) for t in D_set])
    # I = sorted([(t[0].name, t[1].name) for t in I_set])

    return D, I


def diekertGraph(original_word: str, D: set) -> nx.DiGraph:
    """
    Diekert graph based on word and dependency relation
    :param original_word: word from alphabet
    :param D: Dependency relations dict
    :return: Diekert's graph (directed acyclic)
    """
    G = nx.DiGraph()

    word = []
    #  Same name transactions must have different ids for as graph nodes: a, a -> a0, a1
    for i, v in enumerate(original_word):
        id = original_word[:i].count(v)
        word.append(v + str(id))
    # Add nodes
    for v in word:
        G.add_node(v, name=v, layer=-1)

    lowest_vertex = dict()  # mapping node type -> node with lowest layer (lowest in diekert's graph)
    # Add edges
    for i, v in enumerate(word):
        parents = {parent[:1] for parent in word[:i] if (v[:1], parent[:1]) in D}  # set of dependent vertex types
        if not parents:
            G.nodes[v]['layer'] = 0
        else:
            parents = [lowest_vertex[p] for p in parents]  # get lowest dependent vertices
            parents.sort(key=lambda x: G.nodes[x]["layer"], reverse=True)  # to add edges from lowest layer to highest
            G.nodes[v]['layer'] = max(G.nodes[parent]["layer"] + 1 for parent in parents)  # -1 to parent's layer + 1

            for parent in parents:
                if not nx.has_path(G, parent, v):  # if there is no transitive dependency already
                    G.add_edge(parent, v)

        lowest_vertex[v[:1]] = v  # this vertex is now the lowest in graph for it's type

    return G


def FNF_graph(G: nx.DiGraph) -> dict:
    """
    Foat Normal Form based on Diekert's graph
    :param G: Diekert's graph
    :return: FNF as mapping: layer -> transactions
    """
    FNF = dict()
    for v in G.nodes:  # split nodes based on graph's layers
        layer = G.nodes[v]["layer"]
        if layer not in FNF:
            FNF[layer] = [v[:1]]
        else:
            FNF[layer].append(v[:1])

    return FNF


def FNF_word(word: str, D: set) -> dict:
    """
    Foat Normal Form based on word from alphabet
    :param word: word from alphabet
    :param D: Dependency relation
    :return: FNF as mapping: layer -> transactions
    """
    FNF = dict()
    for char in word:
        layer = 0
        for key, values in FNF.items():  # check dependency with all previous transactions and get FNF-layer
            for value in values:
                if (char, value) in D:
                    layer = max(layer, key + 1)
        if layer not in FNF:
            FNF[layer] = [char]
        else:
            FNF[layer].append(char)

    return FNF


