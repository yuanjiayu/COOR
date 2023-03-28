# [COOR](https://github.com/yuanjiayu/COOR)

<p align="center">
    <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache%202-red.svg"></a>
    <a href="support os"><img src="https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg"></a>
    <a href=""><img src="https://img.shields.io/badge/python-3.7+-aff.svg"></a>
    <a href="https://github.com/yuanjiayu/COOR/graphs/contributors"><img src="https://img.shields.io/github/contributors/yuanjiayu/COOR?color=9ea"></a>
    <a href="https://github.com/yuanjiayu/COOR/commits"><img src="https://img.shields.io/github/commit-activity/m/yuanjiayu/COOR?color=3af"></a>
    <a href="https://github.com/yuanjiayu/COOR/issues"><img src="https://img.shields.io/github/issues/yuanjiayu/COOR?color=9cc"></a>
    <a href="https://github.com/yuanjiayu/COOR/stargazers"><img src="https://img.shields.io/github/stars/yuanjiayu/COOR?color=ccf"></a>
</p>





* Author: [Yuan Jiayu](https://github.com/yuanjiayu)    
* Date: 2023.3.28


COOR is an abbreviation for CO electro-oxidation reaction.
This module can realize the kinetic simulation of CO electrooxidation process.

## Overview
The distribution and type of exposed surface sites are essential aspects of kinetics which should be considered together with mass transport in an electrochemical process, since multiple types of functional sites may coexist on electrocatalyst surfaces. In this study, we categorized the surface sites into active sites where the dissociation of water molecule and CO oxidation took place and nonactive sites where CO was adsorbed. By solving the bulk diffusion, adsorption, surface diffusion and reaction using the Fick’s diffusion law, reaction rate law, and Butler-Volmer equation, it was shown that the catalysts surface with a certain ratio of nonactive sites possessed high current rather than only with a type of active sites. More importantly, the high steady-state current can be obtained by balancing the micro-kinetics and mass transport. The findings provide a new strategy of catalyst design and electrochemical operation.

The [lsv](./lsv) package includes [modeling_lsv](./lsv/modeling_lsv.py), [getparams](./lsv/getparams.py), and [save_results](./lsv/getparams.py), which can realize linear scan experiments.
params_dict.json is the default parameter setting for this model.

## Usage

* Clone Our Project:
```bash
cd ~
git clone https://github.com/yuanjiayu/COOR.git
```
* Enter the project directory:
```bash
cd COOR
```
* Run the [run_model.py](./run_model.py) to perform simulation calculations:
```bash
python run_model.py --exp_name=lsv --save_path=./runs --log_file=./logs
```  
Note: The resulting experimental data are saved in .runs, and experiment logs are saved in .logs.    

* Data graphing. Edit the [plot_lsv.py](./plot_lsv.py) and then change the ```exp_name="lsv_data_Mar27_22-45-01"``` by using your experience folder name.
```python
if __name__ == "__main__":
    plot_lsv(exp_name="lsv_data_Mar27_22-45-01", 
             exp_dir="./runs",
             regen_figure=True)
```
* Run the updated [plot_lsv.py](./plot_lsv.py):
```bash
python plot_lsv.py
```
Note: Graphics files are saved in the **plot_lsv_results** folder.    

## References

```
@article{COOR2023,
title = {Modeling the electrooxidation of CO on the catalyst with heterogeneous sites},
year = {2023},
url = {https://github.com/yuanjiayu/COOR},
author = {Jiayu Yuan and Guangxing Yang and Haofan Wang and Yonghai Cao and Hongjuan Wang and Feng Peng and Hao Yu}
}
```

## License
The project is provided under the [Apache-2.0 License](https://github.com/scutcyr/dstc11-simmc2.1-scut-bds-lab/blob/main/LICENSE).

