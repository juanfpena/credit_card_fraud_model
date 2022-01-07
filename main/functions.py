import numpy as np


def cross_entropy(predictions, targets, epsilon=1e-12):
    """
    Computes cross entropy between targets (encoded as one-hot vectors)
    and predictions. 
    Input: predictions (N, k) ndarray
           targets (N, k) ndarray        
    Returns: scalar
    """
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce = -np.sum(targets*np.log(predictions+1e-9))/N
    return ce


def age_discretizer(age):
    if age < 25:
        return 0
    if age < 35:
        return 1
    if age < 45:
        return 2
    else:
        return 3


def pay_to_bill_discretizer(x):
    if x < 0.25:
        return 0
    elif x < 0.5:
        return 1
    elif x < 1:
        return 2
    else:
        return 3
