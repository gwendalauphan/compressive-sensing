import numpy as np
import pandas as pd

from PIL import Image
from openpyxl import Workbook

def init_signaux():
    try:
        df_signaux_dico = pd.read_excel(r'data.xlsx',sheet_name="data ell=150 et N=98",engine='openpyxl')
        df_signaux_test = pd.read_excel(r'data.xlsx',sheet_name="pour test -- 13 signaux à N=98",engine='openpyxl')
    except:
        pass
    matrice_signaux_train = df_signaux_dico.to_numpy()
    matrice_test_test = df_signaux_test.to_numpy()

    N1,K1 = 98,150
    print("matrice_signaux_train.shape",matrice_signaux_train.shape)
    matrice_signaux_train = matrice_signaux_train[:N1,:K1]
    print("matrice_signaux_train.shape",matrice_signaux_train.shape)

    N2,P2 = 98,13
    print("matrice_test_test.shape",matrice_test_test.shape)
    matrice_test_test = matrice_test_test[:N2,:P2]
    print("matrice_test_test.shape",matrice_test_test.shape)

    x_train,x_test = matrice_signaux_train,matrice_test_test
    return x_train,x_test
