from gauss import *
from utils import *

matrix = load_matrix("test_matrices/input20.txt")
matrix = parallel_gauss(matrix)
matrix = backwards_solving(matrix)
save_matrix(matrix, "pg_output20.txt")

# G = make_graph(5)
# draw_graph(G)

