# coding=utf-8
'''
This module draws basic graphs based on experimental data.
'''
# Author: Yuan Jiayu
# Date: 2021.10.23
import os
import json
import math
import shutil
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from matplotlib import ticker, cm
from load_data_from_dir import load_data_with_exp_name 

def plot_lsv(exp_name="lsv_data_Mar27_22-45-01", 
             exp_dir="./runs",
             regen_figure=True):

    data_dir = os.path.join(exp_dir, exp_name)
    figure_save_path = os.path.join("./plot_lsv_results",exp_name) # 给保存实验图片的文件夹赋予名字

    if os.path.exists(figure_save_path):
        if regen_figure == False:
            return None
        elif regen_figure == True:
            shutil.rmtree(figure_save_path)  # Remove the figure_save_path
    #
    if not os.path.exists(figure_save_path):
        os.makedirs(figure_save_path) # If the directory figure_save_path does not exist, it is created
    # load data
    L_C, L_Theta_OH, L_Theta_V, L_Gamma_CO, L_Cjtot, L_Cjox, L_CjN, L_CjOH = load_data_with_exp_name(exp_name, exp_dir)
    PARAMS_DICT = json.load(open(os.path.join(data_dir, "params_dict.json"), "r"))
    params_dict=PARAMS_DICT
    # plot
    plt.rcParams['figure.figsize']=(6.0,4.5)
    plt.rcParams['savefig.dpi'] = 600 
    plt.rcParams['figure.dpi'] = 600 
    plt.rcParams['font.sans-serif']=['Arial']
    font1 = {'family' : 'Arial',
             'weight' : 'normal',
             'size'   : 18,}
    #
    v = params_dict["v"]
    dt = params_dict["dt"]#
    D_CO=params_dict["D_CO"]
    dx = params_dict["dx"]
    tmax = params_dict["tmax"]  # 0<t<T
    L=math.sqrt(2*D_CO*tmax)  # 0<x<L
    t_num = int(tmax/dt) 
    x_num = int(L/dx)
    #print("t_num=",t_num,"x_num=",x_num)
    Space_t_1 = np.arange(0,(t_num)*dt*v,dt*v)
    Space_t = np.arange(0,(t_num+0.5)*dt*v,dt*v)
    Space_x=np.arange(0,(x_num+0.5)*dx/L,dx/L)
    #plot current density
    plt.plot(Space_t_1,L_Cjtot,linewidth =1)
    plt.legend(frameon=False,fontsize='xx-large',loc='upper left')
    plt.xlabel('$\t{E}$ (V)',font1)
    plt.ylabel('$\t{j}$ ($\mu$A cm$^{-2}$)',font1)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tick_params(axis='both',width=1,length=5)
    plt.savefig(os.path.join(figure_save_path,"jtot"+'.png'),bbox_inches = 'tight')
    plt.clf()
    # plot coverage 
    plt.plot(Space_t,L_Theta_OH,linewidth =1.2,label = r"$\theta$$\rm{_{OH}}$",color='tab:red')
    plt.plot(Space_t,L_Theta_V,linewidth =1.2,label = r"$\theta$$\rm{_{V}}$",color='tab:blue')
    plt.plot(Space_t,L_Gamma_CO,linewidth =1.2,label = r"$\Gamma$$\rm{_{CO}}$",color='tab:green')
    plt.legend(frameon=False,fontsize='xx-large')
    plt.ylim(-0.05,1.05)
    plt.xlim(-0.05,1.2)
    x_major_locator=MultipleLocator(0.24)
    y_major_locator=MultipleLocator(0.20)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    plt.xlabel('$\t{E}$ (V)',font1)
    plt.ylabel('$\t{coverage}$',font1)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.savefig(os.path.join(figure_save_path,"coverage"+'.png'),bbox_inches = 'tight')
    plt.clf()
    # plot Concentration changes of reactants in the diffusion layer
    fig, ax = plt.subplots(figsize=(6,4.5))
    C_L_one=np.array(L_C)
    Space_t_3d, Space_x_3d = np.meshgrid(Space_t, Space_x)
    levels = np.arange(0,1.0001,0.005)
    surf = ax.contourf(Space_t_3d, Space_x_3d,C_L_one,levels,cmap =plt.get_cmap('Spectral'))
    clb=fig.colorbar(surf, fraction=0.1, pad=0.15, shrink=0.9, anchor=(0.0, 0.3))
    tick_locator = ticker.MaxNLocator(nbins=6)  # The number of scale values ​​on the colorbar
    clb.locator = tick_locator
    clb.ax.tick_params(labelsize=13)
    clb.ax.set_title(r"$C$($\rm{mol}$$\cdot$$\rm{m^{-3}}$)",fontsize=10.8)
    clb.update_ticks()#Display the scale value of the colorbar
    Emax=tmax*v
    ax.set_xlim(0,Emax)
    ax.set_ylim(0,1)
    x_step=Emax/5
    x_major_locator=MultipleLocator(x_step)
    y_major_locator=MultipleLocator(0.2)
    ax=plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)
    ax.set_xlabel('$\t{E}$(V)',font1)
    ax.set_ylabel('$\t{x/L}$',font1)
    ax.tick_params(labelsize=16)
    labels = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontname('Arial') for label in labels]
    plt.savefig(os.path.join(figure_save_path,"CO_2D"+'.png'),bbox_inches = 'tight')
    plt.clf()
    
if __name__ == "__main__":
    plot_lsv(exp_name="lsv_data_Mar27_22-45-01", 
             exp_dir="./runs",
             regen_figure=True)