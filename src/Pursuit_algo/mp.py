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

def Matching_Pursuit(x, iteration_mp, D, e,max_alpha=None):
    #Initialisation
    Index = []
    R = x
    k = 0
    n_sample, n_feature = D.shape

    N2, K1 = np.matrix(D).shape
    alpha = {}
    
    while (np.linalg.norm(R) > e and k < iteration_mp):
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
        #print(liste_candidats)
        #print(k)
        m = np.argmax(liste_candidats)

        if m not in Index:
            Index.append(m)


        z = (D[:,m].dot(R))/(np.linalg.norm(D[:,m])**2)

        try: alpha[str(m)] = alpha[str(m)] + z 
        except: alpha[str(m)] = z 

        #print(alpha)
        R = R - z*D[:,m] #(D[:,m][:,None]*(z))
        new_x = (D[:,m]).dot(alpha[str(m)])

        k=k+1
    
    #affichage_resultats(new_x,k,R,str(m),alpha,Index)

    return_mp = {"liste_alpha":alpha, "liste_index":Index, "last_index":str(m), "erreur": np.linalg.norm(R)}

    return return_mp
