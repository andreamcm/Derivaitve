import numpy as np
import sympy as sym

def derivative_cost(theta, X, y):
    m = X.shape
    m = m[0]
    i = 1
    for (i in range(1, m)):
        res = (1/m)*((theta*i(X**i)) - y**i) X[i]
        
    return res
        
    
    