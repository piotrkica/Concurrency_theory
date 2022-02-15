import numpy as np
from matplotlib import pyplot as plt
import networkx as nx


def load_matrix(filename: str, eps: int = 14) -> np.ndarray:
    """
    Load and parse input file
    :param filename: path to input file
    :param eps: precision matrix is rounded to
    :return: matrix of (n, n+1) size
    """
    with open(filename) as file:
        lines = file.readlines()

    n = int(lines[0])
    RHS = np.genfromtxt([lines[-1]]).reshape((n, 1))
    matrix = np.genfromtxt(lines[1:-1])
    matrix = np.append(matrix, RHS, axis=1)
    matrix = np.round(matrix, eps)

    return matrix


def save_matrix(matrix: np.ndarray, filename: str):
    """
    Save matrix-result to specified file
    :param matrix: output matrix
    :param filename: output file
    """
    n = len(matrix)
    np.savetxt(filename, (matrix[:n, :n]), fmt="%g", delimiter=" ", header=str(n), comments='')
    with open(filename, "a+") as file:
        last_col = ' '.join([str(num) for num in matrix[:, -1]])
        file.write(last_col)


def draw_graph(G: nx.DiGraph):
    """
    Plot graph, each color represents one layer
    :param G: Diekert's graph
    """
    color_map = [G.nodes[node]["layer"] for node in G]
    plt.title("Diekert's Graph")
    pos = nx.multipartite_layout(G, subset_key="layer")
    nx.draw(G, pos, node_color=color_map, with_labels=True, font_size=6, arrowsize=3, width=0.3, node_size=75,
            font_color="red")
    plt.savefig('graph.pdf')  # pdf pozwala nieskończenie przybliżać
    # plt.show()


def make_graph(n: int) -> nx.DiGraph:
    """
    Generate Diekert Graph for Gaussian Elimination.
    Simpler version - lacks edges from nodes C to B and C in the next layer
    :param n: size of input matrix
    :return: DiGraph
    """
    def make_subgraph(depth, layer):
        if depth == n:
            return
        for i in range(depth + 1, n + 1):
            G.add_node(f"A{depth, i}", layer=layer)
            if depth != 1:
                G.add_edge(f"C{depth - 1, depth, depth}", f"A{depth, i}")
                G.add_edge(f"C{depth - 1, depth, i}", f"A{depth, i}")

            for j in range(depth, n + 2):
                G.add_node(f"B{depth, i, j}", layer=layer + 1)
                G.add_edge(f"A{depth, i}", f"B{depth, i, j}")
                G.add_node(f"C{depth, i, j}", layer=layer + 2)
                G.add_edge(f"B{depth, i, j}", f"C{depth, i, j}")

        make_subgraph(depth + 1, layer + 3)

    G = nx.DiGraph()
    make_subgraph(1, layer=0)

    return G


def make_graph4x5() -> nx.DiGraph:
    """
    Hardcoded full Diekert's Graph for matrix size=4x5.
    :return: DiGraph
    """
    G = nx.DiGraph()
    for i in range(2, 5):
        A_id = f"A{1},{i}"
        G.add_node(A_id, layer=0)
        for j in range(1, 6):
            B_id = f"B{1},{j},{i}"
            C_id = f"C{1},{j},{i}"
            G.add_node(B_id, layer=1)
            G.add_edge(A_id, B_id)
            G.add_node(C_id, layer=2)
            G.add_edge(B_id, C_id)

    for i in range(3, 5):
        A_id = f"A{2},{i}"
        G.add_node(A_id, layer=3)
        for j in range(2, 6):
            B_id = f"B{2},{j},{i}"
            C_id = f"C{2},{j},{i}"
            G.add_node(B_id, layer=4)
            G.add_edge(A_id, B_id)
            G.add_node(C_id, layer=5)
            G.add_edge(B_id, C_id)

    G.add_edge(f"C{1},{2},{2}", f"A{2},{3}")
    G.add_edge(f"C{1},{2},{3}", f"A{2},{3}")
    G.add_edge(f"C{1},{2},{2}", f"A{2},{4}")
    G.add_edge(f"C{1},{2},{4}", f"A{2},{4}")

    G.add_edge(f"C{1},{3},{2}", f"B{2},{3},{3}")
    G.add_edge(f"C{1},{3},{2}", f"B{2},{3},{4}")
    G.add_edge(f"C{1},{4},{2}", f"B{2},{4},{3}")
    G.add_edge(f"C{1},{4},{2}", f"B{2},{4},{4}")
    G.add_edge(f"C{1},{5},{2}", f"B{2},{5},{3}")
    G.add_edge(f"C{1},{5},{2}", f"B{2},{5},{4}")

    G.add_edge(f"C{1},{3},{3}", f"C{2},{3},{3}")
    G.add_edge(f"C{1},{4},{3}", f"C{2},{4},{3}")
    G.add_edge(f"C{1},{5},{3}", f"C{2},{5},{3}")
    G.add_edge(f"C{1},{3},{4}", f"C{2},{3},{4}")
    G.add_edge(f"C{1},{4},{4}", f"C{2},{4},{4}")
    G.add_edge(f"C{1},{5},{4}", f"C{2},{5},{4}")

    for i in range(4, 5):
        A_id = f"A{3},{i}"
        G.add_node(A_id, layer=6)
        for j in range(3, 6):
            B_id = f"B{3},{j},{i}"
            C_id = f"C{3},{j},{i}"
            G.add_node(B_id, layer=7)
            G.add_edge(A_id, B_id)
            G.add_node(C_id, layer=8)
            G.add_edge(B_id, C_id)

    G.add_edge(f"C{2},{3},{3}", f"A{3},{4}")
    G.add_edge(f"C{2},{3},{4}", f"A{3},{4}")

    G.add_edge(f"C{2},{4},{3}", f"B{3},{4},{4}")
    G.add_edge(f"C{2},{5},{3}", f"B{3},{5},{4}")

    G.add_edge(f"C{2},{4},{4}", f"C{3},{4},{4}")
    G.add_edge(f"C{2},{5},{4}", f"C{3},{5},{4}")

    return G

