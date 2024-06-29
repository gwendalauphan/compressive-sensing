import numpy as np

def return_alpha(alpha,last_index,Liste_Index,L1,K1):
    alpha_optimal = alpha[last_index]

    K2, L2 = np.matrix(alpha_optimal).shape
    #print("\n------alpha brut------\n", np.matrix(alpha_optimal))

    flatten_list = []
    if K2 == 1:
        flatten_list = alpha_optimal
        alpha_index_tmp = [0]*K1
    else:
        for i in range(K2):
            flatten_list.append(alpha_optimal[i])
        alpha_index_tmp = [[0]*L1]*K1

    if K2 ==1:
        for i, valeur in zip(Liste_Index, alpha_optimal):
            alpha_index_tmp[i] = valeur  # on place la valeur à l'indice i de la liste_init
    
    else:
        for index,alpha_index in enumerate(Liste_Index):
            alpha_index_tmp[alpha_index] = flatten_list[index].tolist()

    #print("\n------Alpha transfome--------\n", np.matrix(alpha_index_tmp))

    return alpha_index_tmp


def return_alpha_mp(alpha,last_index,Liste_Index,L1,K1):
    flatten_list = []
    alpha_optimal,Liste_Index_safe = list(alpha.values()),list(alpha.keys())
    K2, L2 = 1,len(Liste_Index)
    #print(Liste_Index_safe)
    #print("\n------alpha brut------\n", np.matrix(alpha_optimal))

    flatten_list = []
    if K2 == 1:
        flatten_list = alpha_optimal
        alpha_index_tmp = [0]*K1
    else:
        for i in range(K2):
            flatten_list.append(alpha_optimal[i])
        alpha_index_tmp = [[0]*L1]*K1

    if K2 ==1:
        for i, valeur in zip(Liste_Index, alpha_optimal):
            alpha_index_tmp[i] = valeur  # on place la valeur à l'indice i de la liste_init
    
    else:
        for index,alpha_index in enumerate(Liste_Index):
            alpha_index_tmp[alpha_index] = flatten_list[index].tolist()

    #print("\n------Alpha transfome--------\n", np.matrix(alpha_index_tmp))

    return alpha_index_tmp
