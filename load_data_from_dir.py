# coding=utf-8

'''
This file is used to: Batch read .npz files from a folder
'''
# Author: Yuan Jiayu
# Date: 2021.10.23
import os
import numpy as np


def loaddata(data_dir="./runs/lsv_data_Mar27_22-21-21", file_name="L_Cradsa.npz"):
    data_path = os.path.join(data_dir, file_name)
    data = np.load(data_path)
    data = data['arr_0']#The default index is used
    return data

def load_data_with_exp_name(exp_name="lsv_data_Mar27_22-21-21", exp_dir="./runs"):
    exp_path = os.path.join(exp_dir, exp_name)

    L_C = loaddata(data_dir=exp_path, file_name="C.npz")
    L_Theta_OH = loaddata(data_dir=exp_path, file_name="Theta_OH.npz")
    L_Theta_V = loaddata(data_dir=exp_path, file_name="Theta_V.npz")
    L_Gamma_CO = loaddata(data_dir=exp_path, file_name="Gamma_CO.npz")
    L_Cjtot = loaddata(data_dir=exp_path, file_name="Cjtot.npz")
    L_Cjox = loaddata(data_dir=exp_path, file_name="Cjox.npz")
    L_CjN = loaddata(data_dir=exp_path, file_name="CjN.npz")
    L_CjOH = loaddata(data_dir=exp_path, file_name="CjOH.npz")

    return L_C, L_Theta_OH, L_Theta_V, L_Gamma_CO, L_Cjtot, L_Cjox, L_CjN, L_CjOH
