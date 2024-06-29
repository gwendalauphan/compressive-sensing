import numpy as np
from math import *
from scipy.linalg import svd,norm
from Mesure.sensing_matrix import *

def dot(phi,x):
    return (np.dot(phi,x))

def reconstruct_D(phi, dico):
    return np.dot(phi,dico)

def compress_(new_D,alpha):
    return np.dot(new_D,np.matrix(alpha))

def decoding_bis(new_D,new_Dt,Y):
    G = np.dot(new_D,new_Dt)
    G_inv = np.linalg.inv(G)
    return np.dot(np.dot(new_Dt,G_inv),Y)

def PSNR(x,y,r=4):
    return 10*(np.log10(((2**3)-1)**2)/MSE(x,y))

def MSE(x,y):
    try: mse = norm(x-y, 'fro')/(x.shape[0]*x.shape[1])
    except: mse = norm(x-y)/(x.shape[0])
    return mse





