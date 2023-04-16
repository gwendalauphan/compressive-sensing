import numpy as np
import pandas as pd
from math import *

from Mesure.functions import *
from Mesure.sensing_matrix import *

from Reconstruct.functions import *

def update_compare_mesures(D,liste_matrice_mesure,df,P):
    
    df.loc['phi1', P] = coherence_mutuelle(D, liste_matrice_mesure[0])
    df.loc['phi2', P] = coherence_mutuelle(D, liste_matrice_mesure[1])
    df.loc['phi3', P] = coherence_mutuelle(D, liste_matrice_mesure[2])
    df.loc['phi4', P] = coherence_mutuelle(D, liste_matrice_mesure[3])
    df.loc['phi5', P] = coherence_mutuelle(D, liste_matrice_mesure[4])

    print(df)
    return df

def run_compare_algos(D,phi,alpha):
    print("phi4.shape",phi.shape)
    print("D.shape",D.shape)
    print("new_D.shape",new_D.shape)
    print("alpha.shape",np.matrix(alpha).shape)
    print("x",x)
    print("y",y)
    psnr = PSNR(x,y)
    print("psnr",psnr)

    return y