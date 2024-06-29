import numpy as np
import pandas as pd
import os
from PIL import Image
from openpyxl import Workbook
import sys

# getting the name of the directory where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
root_project = os.path.dirname(parent)

sys.path.append(root_project)

data_directory = os.path.join(root_project,"data")
sys.path.append(data_directory)

data_file_name = "data.xlsx"
data_file = os.path.join(data_directory,data_file_name)

def init_signaux(verbose=False):
    try:
        print("Jeu de données utilisé:",data_file)
        df_signaux_dico = pd.read_excel(data_file, sheet_name="data ell=150 et N=98", engine='openpyxl')
        df_signaux_test = pd.read_excel(data_file, sheet_name="pour test -- 13 signaux à N=98", engine='openpyxl')
        print("--------Lecture des données réussie--------")
    except:
        print("Erreur lors de la lecture du fichier de données")
        exit(1)
    matrice_signaux_train = df_signaux_dico.to_numpy()
    matrice_test_test = df_signaux_test.to_numpy()

    N1,K1 = 98,150
    if verbose:
        print("matrice_signaux_train.shape avant découpage",matrice_signaux_train.shape)
    matrice_signaux_train = matrice_signaux_train[:N1,:K1]
    if verbose:
        print("matrice_signaux_train.shape après découpage",matrice_signaux_train.shape)

    N2,P2 = 98,13
    if verbose:
        print("matrice_test_test.shape avant découpage",matrice_test_test.shape)
    matrice_test_test = matrice_test_test[:N2,:P2]
    if verbose:
        print("matrice_test_test.shape après découpage",matrice_test_test.shape)

    x_train,x_test = matrice_signaux_train,matrice_test_test
    return x_train,x_test
