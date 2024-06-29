from .load_data import*

verbose_init_signaux = False
X_train,X_test = init_signaux(verbose=verbose_init_signaux)

liste_P = [15,25,50,75]
liste_func = ["MP","OMP","STOMP","COSAMP","IRLS"]

def config_dico():
    x_train= X_train,              #  Dataset d'entrainement 
    num_atoms_dico=100,            #  Nombre d'atomes du dictionnaire
    func_dico="IRLS",               #  Fonction utilisée pour calculer alpha          
    maxiter_dico=10,               #  Nombre d'itération de l'algo K-svd
    iteration_algo_dico=20,        #  Nombre d'itération de l'algo utilisé
    max_alpha_dico = None,         #  Nombre maximum d'alpha = None (par défaut)
    arret_stop_algo_dico=0.000001, #  Critère d'arrêt de l'algo (Convergence)
    t_st_omp_dico=2.4,             #  Paramètre "t" utilisé pour St_omp
    epsilon_irls_dico = 0.1,       #  Paramètre "epsilon" pour IRLS
    p_irls_dico = 0.5,             #  Paramètre "p" pour IRLS
    approx=False,                  #  Approximation du K-svd (Si Alpha_nonzero = 0)
    verbose_dico = False,          #  Mode Verbose (Affiche d)
    method_dico = "alea",          #  Méthode d'initialisation du dictionnaire
    initial_D=None                 #  Check d'un dictionnaire déjà existant

    params_dico = [x_train,num_atoms_dico,func_dico,maxiter_dico,iteration_algo_dico,max_alpha_dico,arret_stop_algo_dico,t_st_omp_dico,epsilon_irls_dico,p_irls_dico,approx,verbose_dico,method_dico,initial_D]
    return params_dico

def config_phi(dico,liste_P):
    dico_phi = dico,               #  Dictionnaire
    low_phi = 0                    #  Borne inférieure
    high_phi = 1                   #  Borne supérieure
    p_phi=0.5                      #  Paramètre p
    threshold_phi = 0.75           #  Seuil de sparsité
    liste_P_phi = liste_P          #  Liste des valeurs de P

    params_phi = [dico_phi,low_phi,high_phi,p_phi,threshold_phi,liste_P_phi]
    return params_phi


def config_run(dico,liste_phi,liste_P):
    X_origin = X_test,             #  Dataset de test
    dico_run = dico,               #  Dictionnaire
    liste_phi_P = liste_phi,       #  Liste des matrices de mesure
    num_atoms_run = 100,           #  Nombre d'atomes du dictionnaire
    liste_P_run = liste_P,         #  Liste des valeurs de P
    func_run="IRLS",                #  Fonction utilisée pour calculer alpha
    affichage = True,             #  Affichage graphes
    nb_graphs=3,                  #  Nombre de signaux à reconstruire
    iteration_algo_run=30,         #  Nombre d'itération de l'algo utilisé
    max_alpha_run = None,          #  Nombre maximum d'alpha = None (par défaut)
    arret_stop_algo_run=0.0000001, #  Critère d'arrêt de l'algo (Convergence)
    t_st_omp_run=2.5,              #  Paramètre "t" utilisé pour St_omp
    epsilon_irls_run = 0.1,        #  Paramètre "epsilon" pour IRLS
    p_irls_run = 0.5,              #  Paramètre "p" pour IRLS
    verbose_run = False            #  Mode Verbose

    params_run = [X_origin,dico_run,liste_phi_P,num_atoms_run,liste_P_run,func_run,affichage,nb_graphs,iteration_algo_run,max_alpha_run,arret_stop_algo_run,t_st_omp_run,epsilon_irls_run,p_irls_run,verbose_run]
    return params_run