import numpy as np

class Perceptron(object):
    def __init__(self, no_of_inputs, threshold = 100, learning_rate = 0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        # + 1 is the bias
        self.weights = np.zeros(no_of_inputs + 1)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            return 1
        else:
            return 0

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            
