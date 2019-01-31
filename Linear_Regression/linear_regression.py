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
    
    b, m = gradient_descent(x, y, learning_rate, initial_b, initial_m, number_of_itr)


if __name__ == "__main__":
    main()
