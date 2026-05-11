import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input and output for XOR problem
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Initialize weights
w1 = np.random.rand(2, 2)
w2 = np.random.rand(2, 1)

# Training
for _ in range(10000):
    # Forward propagation
    h = sigmoid(np.dot(X, w1))
    o = sigmoid(np.dot(h, w2))

    # Backpropagation
    d2 = (y - o) * o * (1 - o)
    d1 = d2.dot(w2.T) * h * (1 - h)

    # Update weights
    w2 += h.T.dot(d2) * 0.1
    w1 += X.T.dot(d1) * 0.1

# Testing
for i in X:
    h = sigmoid(np.dot(i, w1))
    o = sigmoid(np.dot(h, w2))

    print(f"Input: {i} Predicted Output: {o[0]}")
