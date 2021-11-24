#%%
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

X = csr_matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #0
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #1
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #2  
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #3
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #4
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #5
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #6
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #7
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  #8
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) #10

Tcsr = minimum_spanning_tree(X)
array = Tcsr.toarray().astype(int)

Y = csr_matrix([[0, 13, 0, 19],  #0
                [0, 0, 0, 9],  #1
                [16, 9, 0, 0],  #2
                [0, 0, 4, 0]])  #3

TcsrT = minimum_spanning_tree(Y)
arrayT = TcsrT.toarray().astype(int)

print(arrayT)