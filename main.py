import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

####################################################
#                                                  #
#------Import des fichiers python necessaires------#

####---Affiche les plots
####---Enregistre les valeurs dans le dataframe
from Analyse.register_results import *
from Analyse.print_results import *

####---Algorithme creation du dictionnaire
####---Switch case des fonctions de matching pursuit
from Dico_algo.k_svd import *
from Dico_algo.utils import *

####---Chargement du dataset sous format xlxs
####---Configuration des parametres
from Init_config.load_data import *
from Init_config.set_parameters import *

####---Comparaison coherence mutuelle
####---Initialisation des matrices de mesures
from Mesure.functions import *
from Mesure.sensing_matrix import *

####---Algorithmes de Matching Pursuit
####---MP-OMP-STOMP-COSAMP-IRLS
####---Reconstruction alpha
from Pursuit_algo.mp import *
from Pursuit_algo.omp import *
from Pursuit_algo.st_omp import *
from Pursuit_algo.coSaMP import *
from Pursuit_algo.irls import *
from Pursuit_algo.sparse_alpha import *

####---Fonctions de reconstruction du signal
####---Fonctions de calcul d'erreurs
from Reconstruct.functions import *

df2 = pd.DataFrame(index=liste_func, columns=liste_P)

###----------------------------------------------------###

config_params_dico = config_dico()
config_params_dico = list(map(lambda arg: arg[0] if isinstance(arg, tuple) and len(arg) > 0 else arg, config_params_dico))

def create_dico(x_train,              #  Dataset d'entrainement 
            num_atoms,                #  Nombre d'atomes du dictionnaire
            func,                     #  Fonction utilisée pour calculer alpha          
            maxiter=10,               #  Nombre d'itération de l'algo K-svd
            iteration_algo=30,        #  Nombre d'itération de l'algo utilisé
            max_alpha = None,         #  Nombre maximum d'alpha = None (par défaut)
            arret_stop_algo=0.000001, #  Critère d'arrêt de l'algo (Convergence)
            t_st_omp=2.5,             #  Paramètre "t" utilisé pour St_omp
            epsilon_irls = 0.1,       #  Paramètre "epsilon" pour IRLS
            p_irls = 0.5,             #  Paramètre "p" pour IRLS
            approx=False,             #  Approximation du K-svd (Si Alpha_nonzero = 0)
            verbose = False,          #  Mode Verbose (Affiche d)
            method_dico = "alea",     #  Méthode d'initialisation du dictionnaire
            initial_D=None):          #  Check d'un dictionnaire déjà existant

    try:
        try: df_dico = pd.read_excel(r'dico.xlsx',sheet_name="dico",engine='openpyxl', header=None)
        except: pass
        
        print(df_dico)
        dico = df_dico.to_numpy()
    except:
        dico = generate_D(x_train,num_atoms,maxiter,func,iteration_algo,max_alpha,arret_stop_algo,t_st_omp,epsilon_irls,p_irls,approx,verbose,method_dico,initial_D) #K-svd
        dico_file = dico.tolist()

        workbook = Workbook()
        worksheet = workbook.create_sheet(title="dico")

        for row in dico_file:
            worksheet.append(row)

        try: workbook.save('dico.xlsx')
        except: pass

    return dico

dico = create_dico(*config_params_dico)

###----------------------------------------------------###

config_params_phi = config_phi(dico,liste_P)
config_params_phi = list(map(lambda arg: arg[0] if isinstance(arg, tuple) and len(arg) > 0 else arg, config_params_phi))

def set_config(dico,low,high,p,threshold,liste_P):
    df = pd.DataFrame(index=['phi1', 'phi2', 'phi3', 'phi4', 'phi5'], columns=liste_P)

    liste_phi_P = []
    for P in liste_P:
        liste_phi = generate_liste_phi(P,X_train.shape[0],low,high,p,threshold)
    
        df_mesures = update_compare_mesures(dico,liste_phi,df,P)
        df_mesures = df_mesures.astype(np.float64)

        index_nom_min = df_mesures[P].idxmin()
        index_min = df_mesures.index.get_loc(index_nom_min)
        print("index_nom_min",index_nom_min)

        phi = liste_phi[index_min]
        liste_phi_P.append(phi)

    print(df) #Tableau 1

    return liste_phi_P

liste_phi = set_config(*config_params_phi)

###----------------------------------------------------###

config_params_run = config_run(dico,liste_phi,liste_P)
config_params_run = list(map(lambda arg: arg[0] if isinstance(arg, tuple) and len(arg) > 0 else arg, config_params_run))

def run(X_origin,
    dico,
    liste_phi_P,
    num_atoms,
    liste_P,
    func,
    affichage = True,
    nb_graphs=4,
    iteration_algo=25,
    max_alpha = None,
    arret_stop_algo=0.0000001,
    t_st_omp=2.5,
    epsilon_irls = 0.1,
    p_irls = 0.3,
    verbose = False):
    
    idxs = np.random.choice(range(X_origin.shape[1]), nb_graphs, replace=False)
    #idxs = [1]
    X_reconstruct = []
    liste_alpha =[]
    for index_P,phi_P in enumerate(liste_phi_P):
        erreur = 0
        X_reconstruct_tmp = []
        for col_index in idxs:

            x_test_col = X_origin[:,col_index]

            # Y: M,P
            Y = dot(phi_P,x_test_col)
            #A: M,K
            A = dot(phi_P,dico)
            
            params = (Y,A,iteration_algo,arret_stop_algo,max_alpha,t_st_omp,epsilon_irls,p_irls,verbose)
            alpha = choix_algo(func,params)
            liste_alpha.append(alpha)
            x_return = dot(dico,alpha)
            X_reconstruct_tmp.append(x_return)

            norm_erreur = np.linalg.norm(x_test_col-x_return)
            erreur += norm_erreur
        """
        df = pd.DataFrame(liste_alpha)
        filepath = 'liste_alpha.xlsx'
        df.to_excel(filepath, index=False)
        """
        erreur = erreur/len(idxs)

        P = liste_P[index_P]
        df2.loc[func, P] = erreur
        print(df2)

        X_reconstruct_tmp = np.matrix(X_reconstruct_tmp).T
        X_reconstruct.append(X_reconstruct_tmp)

    X_origin = X_origin[:,idxs]
    if affichage == True:
        print_graphs_depends_P(X_origin,X_reconstruct,liste_P,nb_graphs)

run(*config_params_run)

###----------------------------------------------------###
"""
X_origin,dico_run,liste_phi_P,num_atoms_run,liste_P_run,func_run,affichage,nb_graphs,iteration_algo_run,max_alpha_run,arret_stop_algo_run,t_st_omp_run,epsilon_irls_run,p_irls_run,verbose_run = config_params_run
for func_pursuit in liste_func:
    run(X_origin,dico,liste_phi_P,num_atoms_run,liste_P_run,func=func_pursuit)

print(df2)
"""