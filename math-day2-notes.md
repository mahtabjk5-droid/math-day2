# Day 2 - Math: Matrix + Tensor Operations

**Date:** 8 October 2026

## 1. Matrix Kya Hai?
- 2D grid (rows x columns)
- Example: [[1,2], [3,4]] - 2x2

## 2. Tensor Kya Hai?
- N-dimensional array
- 0D=Scalar, 1D=Vector, 2D=Matrix, 3D+=Tensor

## 3. Matrix Operations
- Element-wise: A+B, A*B (element by element)
- Matrix mult: A @ B (row x column sum)
- Transpose: A.T (rows <-> columns)
- Reshape: change dimensions

## 4. Rules
- Matrix mult: (m,n) @ (n,p) = (m,p)
- Element-wise: same shape required

## 5. AI Applications
- Image = matrix (H x W)
- Dataset = matrix (samples x features)
- NN layer = matrix mult (x @ W + b)
- Transformer = tensor (batch, seq, embed)

## 6. Code Output (Aaj)
- A @ B: [[19, 22], [43, 50]]
- Tensor shape: (2, 2, 2)
- NN forward: [2.3, 3.0]

## Status
? Day 2 Math Complete
