import numpy as np

def binary_choice(probability_true):
    return np.random.choice([True, False], 1, p=[probability_true, 1 - probability_true])