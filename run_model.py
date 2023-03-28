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
This module is used to call functions and implement LSV experiments.
'''

# Author: Yuan Jiayu
# Date: 2021.10.23
import os
import json
import math
import time
import socket
import logging
import numpy as np
from pprint import pformat
from argparse import ArgumentParser
import lsv
from lsv import get_params,LSV,save_data
logger = logging.getLogger(__file__)

def run_model():
    parser = ArgumentParser()
    # model type and path
    parser.add_argument("--exp_name", type=str, default="lsv", help="Type of Model")
    parser.add_argument("--params_dict", type=str, default="./lsv", help="Path of the .json params_dict file")
    parser.add_argument("--save_path", type=str, default="./runs", help="Path of the saved data")
    parser.add_argument('--log_file', type=str, default="./logs", help="Output logs to a file under this path")
    args = parser.parse_args()
    # Create a runs folder to save the experiment folder
    if not os.path.exists(args.save_path):
        # If there is no directory to save data, create it
        os.makedirs(args.save_path)

    # Read parameter configuration from params_dict path
    PARAMS_DICT = json.load(open(os.path.join(args.params_dict, "params_dict.json"), "r")) 

    # storage data file name
    EXP_NAME = args.exp_name
    START_TIME = str(time.strftime('%b%d_%H-%M-%S',time.localtime(time.time()))) #Read the current time and convert it to a string, e.g. Oct30_17-15-40
    # Create a folder to save the experimental data under args.save_path
    data_path = os.path.join(args.save_path, EXP_NAME+'_data'+'_'+START_TIME)

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    if not os.path.exists(args.log_file):
        os.makedirs(args.log_file)
    # log file name
    logging_file_name = os.path.join(args.log_file,EXP_NAME+'_data'+'_'+START_TIME+'.log')
    logging.basicConfig(level=logging.INFO,
                        filename=logging_file_name) # output the log information to the log file 
    logger.info("Arguments: %s", pformat(args)) 

    # Save the parameter configuration for running the experiment at the beginning, and save it in the data folder
    with open(os.path.join(data_path, "params_dict.json"), 'w') as f:
        json.dump(PARAMS_DICT, f)
    
    #View step size
    
    dt = PARAMS_DICT["dt"]#time step
    D_CO=PARAMS_DICT["D_CO"]
    dx=PARAMS_DICT["dx"]
    #Stability requirements for differential format requirements
    Y=D_CO*dt/(dx*dx)
    logger.info("Stability Conditions for Classical Display Formats: Y="+str(Y))
    
    logger.info("start running experiment...")
    Con = get_params(C_dict=PARAMS_DICT)
    outputs=LSV(Con)
    logger.info("End running experiment...")
    logger.info("Save experiment results...")

    # Save experiment results
    for key in outputs:
        save_data(data=outputs[key], 
                  data_name=key+".npz", 
                  sava_path=data_path)

    logger.info("Save the experiment results!")

if __name__ == "__main__":
    run_model()
