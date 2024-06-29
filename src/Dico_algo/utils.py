import numpy as np 
from math import *
from Pursuit_algo.mp import *
from Pursuit_algo.omp import *
from Pursuit_algo.st_omp import *
from Pursuit_algo.coSaMP import *
from Pursuit_algo.irls import *
from Pursuit_algo.sparse_alpha import *

def choix_algo(func,params):
    Y,dico,iteration_algo,arret_stop_algo,max_alpha,t_st_omp,epsilon_irls,p_irls,verbose = params
    
    if func == "MP":
        mp_vect = Matching_Pursuit(Y,iteration_algo,dico, arret_stop_algo,max_alpha)
        alpha_vect = return_alpha_mp(mp_vect["liste_alpha"],mp_vect["last_index"],mp_vect["liste_index"],1,np.matrix(dico).shape[1])

    elif func == "OMP":
        omp_vect = Optimal_Matching_Pursuit(Y,iteration_algo,dico, arret_stop_algo,max_alpha)
        alpha_vect = return_alpha(omp_vect["liste_alpha"],omp_vect["last_index"],omp_vect["liste_index"],1,np.matrix(dico).shape[1])
        
    elif func == "STOMP":
        st_omp_vect = st_Optimal_Matching_Pursuit(Y,iteration_algo,dico,arret_stop_algo,t_st_omp)
        alpha_vect = return_alpha(st_omp_vect["liste_alpha"],st_omp_vect["last_index"],st_omp_vect["liste_index"],1,np.matrix(dico).shape[1])
    
    elif func == "COSAMP":
        Co_sa_omp_vect = Co_Sa_Matching_Pursuit(Y,iteration_algo,dico,arret_stop_algo)
        alpha_vect = return_alpha(Co_sa_omp_vect["liste_alpha"],Co_sa_omp_vect["last_index"],Co_sa_omp_vect["liste_index"],1,np.matrix(dico).shape[1])
    
    elif func == "IRLS":
        alpha_list = irls_algo(Y, iteration_algo, dico, epsilon_irls, p_irls, max_alpha)
        alpha_vect = alpha_list["liste_alpha"][alpha_list["last_index"]]

    return alpha_vect

    
