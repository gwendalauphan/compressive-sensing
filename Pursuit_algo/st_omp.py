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


def st_Optimal_Matching_Pursuit(x, iteration_omp, D, e,t,max_alpha=None):
    #Initialisation
    Index = []
    R = x
    k = 0

    N, K = D.shape
    #print(" D.shape:", "N",N, " K",K)

    alpha ={}

    while (np.linalg.norm(R) > e and k < iteration_omp):
        
        liste_candidats = []

        for i in range(K): #Selection

            try:
                C_j = abs(np.dot(D[:,i],R))/np.linalg.norm(D[:,i])
            except:
                C_j = abs(np.dot(D[:,i],np.matrix(R)))/np.linalg.norm(D[:,i])
            #norm = max(norm,np.linalg.norm(np.dot(C_j,D[:,i]),2))

            try:
                if isnan(C_j):
                    C_j = 0
            except: pass

            liste_candidats.append(C_j)

        Seuil_k = t*(np.linalg.norm(R,2)/(sqrt(K)))
        Delta_k = [ z for z,w in enumerate(liste_candidats) if w> Seuil_k]

        for element in Delta_k:     #Mise a jour
            if element not in Index:
                Index.append(element)
                
        if len(Index) != 0:

            A = D[:,Index]
            pinv = np.linalg.pinv(A)

            alpha[str(k)]= pinv.dot(x)

            new_x = (A).dot(alpha[str(k)])
            R = x - new_x
        
        k=k+1

    return_omp = {"liste_alpha":alpha, "liste_index":Index, "last_index":str(k-1), "erreur": np.linalg.norm(R)}

    return return_omp

