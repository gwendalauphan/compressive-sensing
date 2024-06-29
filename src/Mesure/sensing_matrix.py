import numpy as np
from math import *
from scipy.sparse import csr_matrix

from .functions import *

def phi1(size,low = 0,high = 1):
    matrice_uniform = np.random.uniform(low = low, high = high, size = size)
    #print(matrice_uniform)
    return matrice_uniform

def phi2(size,p=0.5) :
    matrice_bernoulli_1 = np.random.choice([-1, 1], size=size, p=[1-p, p])
    #print(matrice_bernoulli_1)
    return matrice_bernoulli_1

def phi3(size,p=0.5) :
    matrice_bernoulli_0 = np.random.choice([0, 1], size=size, p=[1-p, p])
    #print(matrice_bernoulli_0)
    return matrice_bernoulli_0

def phi4(size,M) :
    matrice_normale_M = np.random.normal(0, 1/M, size=size)
    #print(matrice_normale_M)
    return matrice_normale_M

def phi5(size,threshold):
    dense_matrix = np.random.rand(*size)
    mask = np.random.rand(*size) < threshold
    sparse_matrix = csr_matrix(dense_matrix * mask)
    matrice_creuse = np.array(sparse_matrix.todense())
    #print(matrice_creuse)
    return matrice_creuse
