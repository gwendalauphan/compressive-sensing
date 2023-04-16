import numpy as np
from math import *
from time import sleep

def affichage_resultats(new_x,k,R,last_index,alpha,Index):
    print("\n \n")
    print("new_x:", new_x)
    print("iteration de fin: ", k)
    print("erreur de fin:", np.linalg.norm(R))
    print("last_index:",last_index)
    print("alpha final:",alpha)
    print("Index:",Index)



def Co_Sa_Matching_Pursuit(x, iteration_omp, D, e, max_alpha=None):
    #Initialisation
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

    while (np.linalg.norm(R) > e and k < iteration_omp):
        liste_candidats = []
        #print("iteration: ", k+1)

        for i in range(K1):
 
            try: value = abs((D[:,i].dot(R)))/np.linalg.norm(D[:,i])
            except: value = abs((D[:,i].dot(np.matrix(R))))/np.linalg.norm(D[:,i])

            try:
                if isnan(value):
                    value = 0
            except: pass
            
            liste_candidats.append(value)

        m1 = np.argmax(liste_candidats)
        liste_candidats[m1] = -1
        m2 = np.argmax(liste_candidats)

        Delta_k = [m1,m2]

        for element in Delta_k:     #Mise a jour
            if element not in Index:
                Index.append(element)

        A = D[:,Index]

        pinv = np.linalg.pinv(A)

        try: alpha[str(k)]= pinv.dot(x)

        except: 
            N_tmp = x.shape[0]
            x = x.reshape(1,N_tmp)
            alpha[str(k)]= pinv.dot(x)

        new_x = (A).dot(alpha[str(k)])
        R = x - new_x
        k=k+1

    #affichage_resultats(new_x,k,R,str(m),alpha,Index)

    return_omp = {"liste_alpha":alpha, "liste_index":Index, "last_index":str(k-1), "erreur": np.linalg.norm(R)}

    return return_omp


