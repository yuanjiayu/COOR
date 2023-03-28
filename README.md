# [COOR](https://github.com/yuanjiayu/COOR)

* Author: [Yuan Jiayu](https://github.com/yuanjiayu)    
* Date: 2023.3.28

COOR is an abbreviation for CO electro-oxidation reaction.
This module can realize the kinetic simulation of CO electrooxidation process.

The lsv package includes modeling_lsv, getparams, and save_results, which can realize linear scan experiments.
params_dict.json is the default parameter setting for this model.

## Usage
1.enter the current directory    
2.Run the run_model.py file in the terminal, e.g. python run_model.py    
3.The resulting experimental data are saved in .runs, and experiment logs are saved in .logs.    
4.Data graphing. Pass the data folder name(e.g. lsv_data_Mar27_22-45-01) to the file(plot_lsv.py), and run.     
5.Graphics files are saved in the plot_lsv_results folder.    
