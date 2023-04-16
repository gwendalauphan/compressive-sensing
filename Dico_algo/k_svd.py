import numpy as np 
from math import *
from scipy.linalg import svd, norm
from scipy.sparse.linalg import svds
from tqdm import tqdm
from time import sleep
import pandas as pd

from .utils import *

def affichage_infos(U,s,V,alpha):
    print("U",U)
    print("U[:,0].shape",U[:,0].shape)
    print("U.shape",U.shape)
    print("s",s)
    print("s",s.shape)
    print("V",V)
    print("V",V.shape)

    print("V.T[:,0]",(V.T)[:,0])
    print("s[0]*((V[:,0]).T)",s[0]*((V.T)[:,0]))
    print("alpha[:,i] avant update",alpha[i,:])

def init_values(X,num_atoms,method_dico,verbose = False, initial_D=None):  
    try: N,P = X.shape
    except: N,P = 1,X.shape[0]
    idx_set = range(P)

    if initial_D is not None: 
        Dico = initial_D / np.linalg.norm(initial_D, axis=0)
    else:# randomly select initial dictionary from X
        if method_dico.startswith("alea"):

            if method_dico == "alea-1":
                idxs = np.random.choice(idx_set, num_atoms, replace=True)

            elif method_dico == "alea-2":
                idxs_1 = np.random.choice(idx_set, int(num_atoms/2), replace=False) #Ligne a reflechir sur le fait du replace = True ? Car si L>K => Pas besoin de mettre true
                idxs_2 = np.random.choice(idx_set, int(num_atoms/2), replace=False)
                idxs = np.concatenate((idxs_1,idxs_2))

            elif method_dico == "alea-3":
                idxs_1 = np.random.choice(idx_set, int(num_atoms/3), replace=False) #Ligne a reflechir sur le fait du replace = True ? Car si L>K => Pas besoin de mettre true
                idxs_2 = np.random.choice(idx_set, int(P/3), replace=False)
                idxs_3 = np.random.choice(idx_set, int(P/3), replace=False) #Ligne a reflechir sur le fait du replace = True ? Car si L>K => Pas besoin de mettre true
                idxs = np.concatenate((idxs_1,idxs_2,idxs_3))

            else:
                idxs = np.random.choice(idx_set, num_atoms, replace=False)
        else:
            idxs = range(num_atoms)
    
        if N == 1:
            Dico = np.matrix(list(map(lambda x: X[x], idxs)))
        
        else: #Partie à generaliser pour des dimensions superieures
            if verbose == True:
                print("idx_set:",idx_set," idxs",idxs)
                print("X[:,idxs]",X[:,idxs])
                print("np.linalg.norm(X[:,idxs])",np.linalg.norm(X[:,idxs]))
            Dico = X[:,idxs] #/ np.linalg.norm(X[:,idxs])

        alpha = np.zeros([num_atoms, P])
        
    return (Dico,X,alpha)

def generate_D(Data,
                num_atoms,
                maxiter,
                func,
                iteration_algo,
                max_alpha,
                arret_stop_algo,
                t_st_omp,
                epsilon_irls,
                p_irls,
                approx,
                verbose,
                method_dico,
                initial_D):

    dico_init,Y,alpha = init_values(Data,num_atoms,method_dico,verbose)
    
    liste_dico = []

    try: N,P = Y.shape
    except: N,P = 1,Y.shape[0]
    N,K = dico_init.shape
    #K,P = alpha.shape

    if max_alpha == None:
        max_alpha = num_atoms

    #iterator = tqdm(range(1,maxiter+1)) #if debug else range(1,maxiter+1)
    for iteration in range(maxiter):
        for zz in range(num_atoms):
            dico_init[:,zz] = dico_init[:,zz] / np.linalg.norm(dico_init[:,zz])

        dico = dico_init
        liste_alpha = []

        for index_vect in range(P): #On calcule les alphas pour chaque vecteur du dataset d'entrainement
            params = (Y[:,index_vect],dico,iteration_algo,arret_stop_algo,max_alpha,t_st_omp,epsilon_irls,p_irls,verbose)

            alpha_vect = choix_algo(func,params)
            liste_alpha.append(alpha_vect)

        alpha = np.matrix(liste_alpha).T
   
        for i in range(num_atoms):

            #Commentaires a faire
            Ti =[] #Les indices d'alpha_i different de zero
            wi =[] 

            for ii,jj in enumerate(alpha[:,i]):
                if np.linalg.norm(jj) != 0:
                    Ti.append(ii)
                    wi.append(jj)
                        

            N1 = len(alpha[:,i]) #Nombre d'atomes. K1 = num_atoms
            K2 = len(Ti)    #Nombre d'atomes pris en compte, K2 = max_alpha

            if K2 == 0:
                if not approx:
                    dico_init[:,i] = np.random.randn(*dico[:,i].shape)
                    dico_init[:,i] = dico[:,i] / np.linalg.norm(dico[:,i])
                continue

            else:
                omega = np.zeros((P, len(Ti)))
                for inz in range(len(Ti)):
                    omega[Ti[inz], inz] = 1

                tmp = dico[:,i]
                dico[:,i] = 0

                ###----1 ere methode de calcul de Eir-----######
                Ei = Y - dico.dot(alpha) 
                Eir2 = (Ei).dot(omega)

                ###----2 eme methode de calcul de Eir-----###### 
                Eir = Y[:, Ti] - dico.dot(alpha[:, Ti])

                #print("Difference entre les 2 methodes",np.linalg.norm(Eir -Eir2))

                U, s, V = svd(Eir)

                if verbose == True:
                    affichage_infos(U,s,V,alpha)
                    
                dico_init[:,i] = U[:,0] / np.linalg.norm(U[:,0] )
                alpha[i,Ti] = s[0]*((V.T)[:,0])

                if verbose == True:
                    print("alpha[:,i] apres update",alpha[:,i])

                dico[:,i] = tmp


        new_x = dico_init.dot(alpha)
        print("erreur update", np.linalg.norm(Y-new_x))
        
    df_alpha = pd.DataFrame(alpha)
    filepath = 'alpha.xlsx'
    df_alpha.to_excel(filepath, index=False)

    return dico

        



