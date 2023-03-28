# coding=utf-8
# Copyright 2023 South China University of Technology
# 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
# http://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License.


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
