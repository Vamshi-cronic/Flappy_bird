import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.weights = []
        self.biases = []

        for i in range(len(layers) - 1):
            self.weights.append(
                np.random.randn(layers[i], layers[i + 1]) * 0.1
            )
            self.biases.append(
                np.zeros((1, layers[i + 1]))
            )

    def forward_prop(self, x):
        current = np.array(x).reshape(1, -1)

        for i in range(len(self.weights)):
            current = sigmoid(
                (current @ self.weights[i]) + self.biases[i]
            )

        return current

    def predict(self, x):
        return self.forward_prop(x)[0][0]

    def copy(self):
        clone = NeuralNetwork(self.layers)
        clone.weights = [w.copy() for w in self.weights]
        clone.biases = [b.copy() for b in self.biases]
        return clone

    def mutate(self, rate=0.1, scale=0.1):
        for i in range(len(self.weights)):
            mask = np.random.rand(*self.weights[i].shape) < rate
            noise = np.random.normal(
                0,
                scale,
                self.weights[i].shape
            )
            self.weights[i] += mask * noise
        
        for i in range(len(self.biases)):
            mask = np.random.rand(*self.biases[i].shape) < rate
            noise = np.random.normal(
                0,
                scale,
                self.biases[i].shape
            )
            self.biases[i] += mask * noise