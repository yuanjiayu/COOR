# coding=utf-8

'''
This module is the main algorithm, which can realize LSV experiment.
'''


# Author: Yuan Jiayu
# Date: 2021.10.23


import math
import copy # deep copy
import logging # printing logs
import numpy as np

from .getparams import get_params

def LSV(Con):
    '''
    Inputs:
        Con:
    Outputs:
        C,Theta_OH,Theta_V,Gamma_CO,Cjtot,Cjox,CjN,CjOH,CRna,CRan,CrN,CkN,Croxan,Croxaa,Ckox,Crb,Ckb,Crf,Ckf,Crdesn,Cradsn,Crdesa,Cradsa
    '''
    
    
    #diffusion layer
    D_CO=Con[25]
    tmax = Con[27]  # 0<t<T
    dt=Con[28]
    L=math.sqrt(2*D_CO*tmax)  # 0<x<L
    dx=math.sqrt(D_CO*dt/0.5)
    Y=D_CO*dt/(dx*dx)
    if Y<=0.6:
        print("The stability condition has been met:Y=",Y)
    else:
        print("Stability condition not met: Y=",Y)
    #Create an empty array
    #number of steps
    t_num = int(tmax/dt) 
    x_num = int(L/dx)
    C = np.zeros((x_num+1,t_num+1),dtype=float)#Generate an array, x rows, t columns, data type float
    Theta_OH=np.zeros(t_num+1,dtype=float)
    Theta_V=np.zeros(t_num+1,dtype=float)
    Gamma_CO=np.zeros(t_num+1,dtype=float)

    # Boundary conditions and initial values
    Cb =Con[26]
    C_x_0 = Cb
    C_L_t = Cb
    for i in range(0,x_num+1): #range(x_num) means range(0,x_num), that is, an array from 0 to x_num-1
        C[i,0] = C_x_0  #

    for j in range(0,t_num+1):
        C[x_num,j] = C_L_t #
    print("The initial distribution of concentration in the diffusion layer:",C)
    #
    Gamma_CO[0] = Con[0]
    Theta_OH[0] = Con[1]
    Theta_V[0] = Con[2]
    Zaa = Con[3]
    Zan = Con[4]
    kads_a = Con[5]
    kdes_a = Con[6]
    kads_n = Con[7]
    kdes_n = Con[8]
    kf0 = Con[9]
    kb0 = Con[10]
    kox0 = Con[11]
    kN0 = Con[12]
    kdan = Con[13]
    kdna = Con[14]
    v = Con[15]
    xi = Con[16]
    alpha_f = Con[17]
    alpha_b = Con[18]
    alpha_ox = Con[19]
    alpha_N = Con[20]
    Eeq_f = Con[21]
    Eeq_b = Con[22]
    Eeq_ox = Con[23]
    Eeq_N = Con[24]

    T = Con[30]
    F = Con[31]
    R = Con[32]
    ps = Con[33]
    e0 = Con[34]
    s = Con[35]
    # Create an empty list for storing data
    Cradsa,Crdesa,Cradsn,Crdesn=[],[],[],[]
    Ckf,Crf,Ckb,Crb=[],[],[],[]
    Ckox,Croxaa,Croxan=[],[],[]
    CkN,CrN=[],[]
    CRan,CRna=[],[]
    Cjtot,CjOH,CjN,Cjox=[],[],[],[]
    for j in range(0,t_num,1):
        for i in range(1,x_num,1):
            #CO adsoprtion and desorption
            radsa_log = np.log(kads_a)+np.log(C[0,j])+np.log(Theta_V[j])+np.log(xi)
            rdesa_log = np.log(kdes_a)+np.log((1-Theta_V[j]-Theta_OH[j]))+np.log(xi)
            radsn_log = np.log(kads_n)+np.log(C[0,j])+np.log((1-Gamma_CO[j]))+np.log((1-xi))
            rdesn_log = np.log(kdes_n)+np.log(Gamma_CO[j])+np.log((1-xi))
            radsa = math.exp(radsa_log)
            rdesa = math.exp(rdesa_log)
            radsn = math.exp(radsn_log)
            rdesn = math.exp(rdesn_log)
            #OH formation and H2O formation
            kf_log = np.log(kf0)+alpha_f*F*(v*j*dt-Eeq_f)/(R*T)
            rf_log = kf_log+np.log(xi)+np.log(Theta_V[j])
            kb_log = np.log(kb0)-(1-alpha_b)*F*(v*j*dt-Eeq_b)/(R*T)
            rb_log = kb_log+np.log(xi)+np.log(Theta_OH[j])
            kf = math.exp(kf_log)
            rf = math.exp(rf_log)
            kb = math.exp(kb_log)
            rb = math.exp(rb_log)
            #CO electrooxidation(L-H)
            kox_log = np.log(kox0)+alpha_ox*F*(v*j*dt-Eeq_ox)/(R*T)
            roxaa_log = np.log(Zaa)+kox_log+np.log(Theta_OH[j])+np.log((1-Theta_V[j]-Theta_OH[j]))+2*np.log(xi)
            roxan_log = np.log(Zan)+kox_log+np.log(Theta_OH[j])+np.log(Gamma_CO[j])+np.log(xi)+np.log((1-xi))
            kox = math.exp(kox_log)
            roxaa = math.exp(roxaa_log)
            roxan = math.exp(roxan_log)
            #CO nucleation (E-R)
            kN_log = np.log(kN0)+alpha_N*F*(v*j*dt-Eeq_N)/(R*T)
            rN_log = kN_log+np.log((1-Theta_V[j]-Theta_OH[j]))+np.log(xi)
            kN = math.exp(kN_log)
            rN = math.exp(rN_log)
            #CO surface diffusion
            Ran_log = np.log(Zan)+np.log(kdan)+np.log((1-Theta_V[j]-Theta_OH[j]))+np.log((1-Gamma_CO[j]))+np.log(xi)+np.log(1-xi)
            Rna_log = np.log(Zan)+np.log(kdna)+np.log(Gamma_CO[j])+np.log(Theta_V[j])+np.log(xi)+np.log((1-xi))
            Ran = math.exp(Ran_log)
            Rna = math.exp(Rna_log)
            #current density(unit:μA/cm2)
            jOH=e0*s*(rf-rb)*1000000
            jN=e0*s*2*rN*1000000
            jox=e0*s*(roxaa + roxan)*1000000
            jtot=e0*s*(roxaa + roxan + 2 * rN + rf - rb)*1000000
            #Boundary point and coverage difference form
            C[0,j+1]=2*Y*C[1,j]-(2*Y-1)*C[0,j]-ps*2*dt/dx*(radsa+radsn-rdesa-rdesn)
            Theta_OH[j+1]=Theta_OH[j]+dt/xi*(rf-rb-roxan-roxaa)
            Theta_V[j+1]=Theta_V[j]+dt/xi*(-(rf-rb-roxan-roxaa)-(radsa-rdesa-roxaa-Ran+Rna-rN))
            Gamma_CO[j+1]=Gamma_CO[j]+dt/(1-xi)*(radsn-rdesn-roxan+Ran-Rna)
            #Interior point difference form
            C[i,j+1] = Y*(C[i+1,j]+C[i-1,j])-(2*Y-1)*C[i,j]
        Cradsa.append(radsa)
        Crdesa.append(rdesa)
        Cradsn.append(radsn)
        Crdesn.append(rdesn)
        Ckf.append(kf)
        Crf.append(rf)
        Ckb.append(kb)
        Crb.append(rb)
        Ckox.append(kox)
        Croxaa.append(roxaa)
        Croxan.append(roxan)
        CkN.append(kN)
        CrN.append(rN)
        CRan.append(Ran)
        CRna.append(Rna)
        CjOH.append(jOH)
        CjN.append(jN)
        Cjox.append(jox)
        Cjtot.append(jtot)

        Outputs={"Cradsa":Cradsa,
                 "Crdesa":Crdesa,
                 "Cradsn":Cradsn,
                 "Crdesn":Crdesn,
                 "Ckf":Ckf,
                 "Crf":Crf,
                 "Ckb":Ckb,
                 "Crb":Crb,
                 "Ckox":Ckox,
                 "Croxaa":Croxaa,
                 "Croxan":Croxan,
                 "CkN":CkN,
                 "CrN":CrN,
                 "CRan":CRan,
                 "CRna":CRna,
                 "CjOH":CjOH,
                 "CjN":CjN,
                 "Cjox":Cjox,
                 "Cjtot":Cjtot,
                 "C":C,
                 "Theta_OH":Theta_OH,
                 "Theta_V":Theta_V,
                 "Gamma_CO":Gamma_CO,}
    return Outputs
