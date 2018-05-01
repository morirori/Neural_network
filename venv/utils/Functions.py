import numpy as np
from math import exp
from enum import Enum


class ActivationFunctionDoesntExist(Exception):
    def __init__(self):
        message="Provieded activation function doesnt exist"


class ActivaionFunction(Enum):
    HYPERBOLIC_TANGENT="hyperbolic tangent"
    SIGMOID="sigmoid"


def sigmoid(beta,value):
    result = 1 / (1 + exp(-1 * beta * value))
    return result

def sigmoid_derivative(value):
    result=value*(1-value)
    return result

def hiberbolic(beta,value):
    return  np.tanh(beta*value)

def hiperbolic_derivative(value):
    return 1-value*value