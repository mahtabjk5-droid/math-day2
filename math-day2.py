import numpy as np

# 1. MATRIX BASICS
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A:", A)
print("Shape of A:", A.shape)       # (2, 2)

# 2. ELEMENT-WISE
print("\nA + B:", A + B)
print("A * B (element-wise):", A * B)

# 3. MATRIX MULTIPLICATION
print("\nA @ B:", A @ B)
print("np.matmul(A, B):", np.matmul(A, B))

# 4. TRANSPOSE
print("\nA.T:", A.T)
print("Shape of A.T:", A.T.shape)

# 5. IDENTITY MATRIX
I = np.eye(2)
print("\nIdentity:", I)
print("A @ I:", A @ I)

# 6. TENSOR (3D)
T = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nTensor T shape:", T.shape)  # (2, 2, 2)
print("T[0]:", T[0])
print("T[1]:", T[1])

# 7. RESHAPE
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print("\nReshaped (2,3):")
print(reshaped)

# 8. NEURAL NETWORK FORWARD PASS (Preview)
# Input: 3 features, Weights: 3x2, Bias: 2
x = np.array([1, 2, 3])              # Input (3,)
W = np.array([[0.1, 0.2],
              [0.3, 0.4],
              [0.5, 0.6]])           # Weights (3, 2)
b = np.array([0.1, 0.2])             # Bias (2,)

output = x @ W + b
print("\nNN Forward Pass:")
print("Input:", x)
print("Output:", output)
