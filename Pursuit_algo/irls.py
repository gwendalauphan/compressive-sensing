import numpy as np
from math import *
import time

def affichage_resultats(new_x,k,R,last_index,alpha,Index):
    print("\n \n")
    print("new_x:", new_x)
    print("iteration de fin: ", k)
    print("erreur de fin:", np.linalg.norm(R))
    print("last_index:",last_index)
    print("alpha final:",alpha)
    print("Index:",Index)



def irls_algo(x, iteration_irls, D, e, p, max_alpha=None):
    #Initialisation
    # 0<p<1
    Index = []
    R = x
    k = 0

    N1, L1 = np.matrix(x).shape
    #print("x.shape:","N",N1," L",L1)

    N2, K1 = D.shape
    #print(" D.shape:", "N",N2, " K",K1)

    if max_alpha==None:
        max_alpha = K1
    #print("alpha.shape"," K",max_alpha," L",L1)

    alpha ={}

    W = np.ones(K1)
    G = np.dot(D,D.T)
    inv_G = np.linalg.inv(G)

    transform_alpha = np.dot(D.T, inv_G)
    alpha_0 = np.dot(transform_alpha,x)
    
    abs_alpha_diff = 10000
    alpha[str(0)] = alpha_0

    while (abs_alpha_diff > sqrt(e)/100 and k < iteration_irls):
        #print("iteration: ", k+1)

        for kk in range(K1): #update W
            
            W[kk] = ((abs(alpha[str(k)][kk])**2 + e))**((p/2) -1)

        Q = np.diag(W)

        QDT = np.dot(Q,D.T)
        DQDT_1 = np.linalg.inv(np.dot(D,QDT))
        
        transform_alpha = np.dot(QDT, DQDT_1)
        alpha[str(k+1)] = np.dot(transform_alpha,x)
        
        new_x = (D).dot(alpha[str(k)])

        abs_alpha_diff = abs(np.linalg.norm(alpha[str(k+1)]) - np.linalg.norm(alpha[str(k)]))
        R = x - new_x

        if e > 0.00000001:
            e = e/10

        k=k+1
        if np.linalg.norm(R)<0.0000001:
            break

    #affichage_resultats(new_x,k,R,str(m),alpha,Index)

    return_omp = {"liste_alpha":alpha, "liste_index":Index, "last_index":str(k), "erreur": np.linalg.norm(R)}

    return return_omp