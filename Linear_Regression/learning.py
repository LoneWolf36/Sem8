import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def compute_error_for_given_points(b, m, x, y):
    totalError = 0
    for i in range(0, len(x)):
        totalError += (y[i] - (m * x[i] + b)) ** 2
    return (totalError / float(len(x)))

def gradient_descent(x, y, learning_rate, initial_b, initial_m, num_iterations):
    b = initial_b
    m = initial_m
    for _ in range(num_iterations):
        b, m = step_gradient_descent(x, y, b, m, learning_rate)
    return (b, m)

def step_gradient_descent(x, y, b_current, m_current, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(x))
    for i in range(0, len(x)):
        b_gradient += -(2/N) * (y[i] - ((m_current * x[i]) + b_current))
        m_gradient += -(2/N) * x[i] * (y[i] - ((m_current * x[i]) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return (new_b, new_m)

def main():
    # Step 1 : Get data
    points = pd.read_csv('data.csv')
    x = points.iloc[:, 0]
    y = points.iloc[:, 1]

    # Step 2 : Define hyperparameters
    learning_rate = 0.0001
    initial_m = 0
    initial_b = 0
    num_iterations = 1000

    # Step 3 : Train our model
    print('Starting gradient descent at b = {0}, m = {1}, error = {2}'.format(
        initial_b, initial_m, compute_error_for_given_points(initial_b, initial_m, x, y)))

    b, m = gradient_descent(x, y, learning_rate,
                            initial_b, initial_m, num_iterations)

    print('Ending gradient descent at b = {1}, m = {2}, error = {3} with {0} iterations'.format(
        num_iterations, b, m, compute_error_for_given_points(b, m, x, y)))

    plt.scatter(x, y)
    plt.plot(x, x*m + b, 'r')
    plt.show()

if __name__ == '__main__':
    main()
