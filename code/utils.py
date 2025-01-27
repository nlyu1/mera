import numpy as np 

def cosine_similarity(A, B):
    """Compute cosine similarity between flattened matrices"""
    A_flat = A.flatten()
    B_flat = B.flatten()
    return np.dot(A_flat, B_flat) / (np.linalg.norm(A_flat) * np.linalg.norm(B_flat))

# Convert numpy arrays to tuples of tuples to make them hashable
def matrix_to_tuple(matrix):
    return tuple(tuple(row) for row in matrix)

