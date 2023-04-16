import numpy as np
from math import *
from .sensing_matrix import *

def coherence_mutuelle(D, phi):
    M,N = phi.shape
    N,K = D.shape
    coherence = 0.0
    liste_coherence = []
    for j in range(K):
        dj = D[:,j]
        for i in range(M):
            phi_i = phi[i,:]
            if i !=j:
                liste_coherence.append((np.abs(np.dot(phi_i, dj)))/(np.linalg.norm(dj)* np.linalg.norm(phi_i)))

    coherence = sqrt(N)*(np.max(liste_coherence))
    return coherence


def generate_liste_phi(P,N,low,high,p,threshold):
    M = ceil((P*N)/100)
    size = (M,N)
    print("size of sensing matrix",size)
    liste_matrice_mesure = [phi1(size,low,high),phi2(size,p),phi3(size,p),phi4(size,M),phi5(size,threshold)]

    return liste_matrice_mesure




