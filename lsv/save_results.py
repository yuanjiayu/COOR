# coding=utf-8

'''
This module is used to save data as a binary file, and specifies the storage location
'''


# Author: Yuan Jiayu
# Date: 2021.10.23


import os
import numpy as np


def save_data(data, data_name, sava_path):
    '''
    Save the data data to the sava_path directory and name it data_name
    '''
    data_path = os.path.join(sava_path,data_name)
    np.savez(data_path,data)