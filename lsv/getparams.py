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
This file is used to pass parameters. Here, an array is created to store each parameter variable. 
The value of the variable is the value in the dictionary. 
Here, a function (get_params(C_dict)) is created to realize parameter passing.
'''


# Author: Yuan Jiayu
# Date: 2021.10.23
import json

def get_params(C_dict):
    print("The current parameters are:")
    print(C_dict)
    Con = [None]*36
    Con[0]=C_dict["GammaCO"]
    Con[1]=C_dict["ThetaOH"]
    Con[2]=C_dict["ThetaV"]
    Con[3]=C_dict["Zaa"]
    Con[4]=C_dict["Zan"]
    Con[5]=C_dict["kads_a"]
    Con[6]=C_dict["kdes_a"] 
    Con[7]=C_dict["kads_n"] 
    Con[8]=C_dict["kdes_n"] 
    Con[9]=C_dict["kf0"]
    Con[10]=C_dict["kb0"] 
    Con[11]=C_dict["kox0"]
    Con[12]=C_dict["kN0"]
    Con[13]=C_dict["kdan"]
    Con[14]=C_dict["kdna"]
    Con[15]=C_dict["v"]
    Con[16]=C_dict["xi"]
    Con[17]=C_dict["alpha_f"] 
    Con[18]=C_dict["alpha_b"]
    Con[19]=C_dict["alpha_ox"]
    Con[20]=C_dict["alpha_N"]
    Con[21]=C_dict["Eeq_f"]
    Con[22]=C_dict["Eeq_b"]
    Con[23]=C_dict["Eeq_ox"]
    Con[24]=C_dict["Eeq_N"]
    Con[25]=C_dict["D_CO"]
    Con[26]=C_dict["Cb"]
    Con[27]=C_dict["tmax"]
    Con[28]=C_dict["dt"]
    Con[29]=C_dict["dx"]
    Con[30]=C_dict["T"]
    Con[31]=C_dict["F"]
    Con[32]=C_dict["R"]
    Con[33]=C_dict["ps"]
    Con[34]=C_dict["e0"]
    Con[35]=C_dict["s"]
    return Con

if __name__ == "__main__":
    params_dict=json.load(open("params_dict.json", "r")) #"r" means read
    Con = get_params(C_dict=params_dict)
