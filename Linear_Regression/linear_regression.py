import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def compute_error_for_given_points(b, m, x, y):
    totalError = 0
    for i in range(len(x)):
        totalError += (y[i] - (m*x[i] + b)) ** 2
    return (totalError/float(len(x)))


def gradient_descent(x, y, learning_rate, intial_b, intial_m, number_of_itr):
    b = intial_b
    m = intial_m
    for _ in range(number_of_itr):
        b, m = step_gradient_descent(x, y, b, m, learning_rate)
    return (b, m)


def step_gradient_descent(x, y, b_current, m_current, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(x))
    for i in range(len(x)):
        b_gradient += -(2/N) * (y[i] - ((m_current * x[i]) + b_current))
        m_gradient += -(2/N) * x[i] * (y[i] - ((m_current * x[i]) + b_current))
    b_new = b_current - (learning_rate * b_gradient)
    m_new = m_current - (learning_rate * m_gradient)
    return (b_new, m_new)

def main():
    # Step 1 : Get data
    data = pd.read_csv("data_back_pain.csv")
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]

    # Step 2 : Define hyperparameters
    learning_rate = 0.0001
    initial_m = 0
    initial_b = 0
    number_of_itr = 1000

    # Step 3 : Train the model
    print('Starting gradient descent at b={0}, m={1} with initial error={2}'.format(
        initial_b, initial_m, compute_error_for_given_points(initial_b, initial_m, x, y)))

    b, m = gradient_descent(x, y, learning_rate,
                            initial_b, initial_m, number_of_itr)

    print('Ending gradient descent at b = {1}, m = {2}, error = {3} with {0} iterations'.format(
        number_of_itr, b, m, compute_error_for_given_points(b, m, x, y)))

    plt.scatter(x, y)
    plt.plot(x, x*m + b, 'r')
    plt.show()

if __name__ == "__main__":
    main()
