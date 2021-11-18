#%%
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

X = csr_matrix([[0, 8, 0, 3],
                [0, 0, 2, 5],
                [0, 0, 0, 6],
                [0, 0, 0, 0]])

Tcsr = minimum_spanning_tree(X)
array = Tcsr.toarray().astype(int)

