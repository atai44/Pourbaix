#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:35:21 2020

@author: alex
"""
import numpy
import math
import matplotlib.pyplot as plt

R=.008314 #kJ/mol-K
T=298.15 #K
F=96.485 #kJ/V-g

#Standard formation energies in kJ/mol from PBESol no spin
GPb = 0
GPbO = 96*-2.5961558581258
GPb3O4 = 96*-8.97161696378122
GPb2O3 = 96*-6.24363209948911
GPbO2 = 96*-3.594140407095
title_ = 'PBESol no spin'

##PBESol spin
GPb = 0
GPbO = -182.179911180077
GPbO2 = -225.05892068112
GPb2O3 = -409.660823950954
GPb3O4 = -606.321927722997
PbCO3 = -636.8927823795264
hc = -1990.5166151753715
pbphos = -2265.1179660491134
P = -553.825665

title_ = 'PBESol spin (low lead conc)'

# # ##LDA
# GPb = 0
# GPbO=96*-2.2967371581258
# GPbO2=96*-3.177723757095
# GPb2O3=96*-5.4897082494891
# GPb3O4=96*-7.85681991378122
# title_= 'LDA with log C = 0'

#PBE
# GPb = 0
# GPbO = -176.883931980077
# GPbO2 = -198.46141028112
# GPb2O3 = -377.086166350954
# GPb3O4 = -579.147706922997
# title_ = 'PBE with log C = 0'

#Experimental (no Pb2O3 data)
# GPb = 0
# GPbO = -187.9
# GPb2O3 = 10000
# GPb3O4 = -601.2
# GPbO2 = -217.4
# PbCO3 = -626.3
# hc = -1709.582 #REMEMBER THIS HAS 3 LEAD ATOMS
# title_ = 'Experimental (low lead conc)'

GPb4 = 302.50074
GPb2 = -23.9743
GHPbO2 = -338.904
GPbO3 = -277.56656
GPbO4 = -282.08946
GPbH2 = 290.788
OH = -157.33514

conc = 1.5*10**(-8)
conc = 1
Cconc = 10**(-5)

pHstart = -2
pHend = 16
dpH = 0.045
pHvec = numpy.arange(pHstart, pHend, dpH)

#pb2plus = [None]*pHvec.size

#pHvec = [10]

Vstart = -2
Vend = 4
dV = 0.01
Vvec = numpy.arange(Vstart, Vend, dV)
#Vvec = [1]

pH_, V_ = numpy.meshgrid(pHvec, Vvec)
Z = pH_ + V_

i=0
j=0
for pH in pHvec:
    i = 0
    for V in Vvec:
        lowpot = 10000000
        stable = ""
        ue = -F * V
        uH = -R*T*math.log(10)*pH
        uPb = GPb
        uH2O = -237.18
        
        #Pb
        lowpot = uPb
        stable = 0
        
        
        
        #Pb2+
        pot = GPb2 + R*T*math.log(conc)
        urxn = pot + 2*ue - uPb
        #print("Pb2+: ", urxn)
        #pb2plus[j] == urxn
        if (urxn <= lowpot) :
            lowpot = urxn
            stable = 1
            
        #PbO
        urxn = GPbO + 2*ue + 2*uH - uPb - uH2O
        #print("PbO: ", urxn)
        if (urxn <= lowpot) :
            lowpot = urxn
            stable = 2
            
            
        #PbO2
        urxn = GPbO2 + 4*ue + 4*uH - uPb - 2*uH2O
        if (urxn <= lowpot) :
            lowpot = urxn
            stable = 3
        
        # #Pb2O3
        # urxn = (GPb2O3 + 6*ue + 6*uH - 2*uPb - 3*uH2O)/2;
        # if (urxn < lowpot) :
        #     lowpot = urxn
        #     stable = 4
            
        #Pb3O4
        urxn = (GPb3O4 + 8*ue + 8*uH - 3*uPb -4*uH2O)/3
        if (urxn <= lowpot) :
            lowpot = urxn
            stable = 5
            
        #Pb4+
        pot = GPb4 + R*T*math.log(conc)
        urxn = pot + 4*ue - uPb
        if (urxn <= lowpot) :
            lowpot = urxn
            stable = 6
            
        #HPbO2
        pot = GHPbO2 + R*T*math.log(conc)
        #print("HPbO2: ", urxn)
        if (urxn <= lowpot) : 
            lowpot = urxn
            stable = 7
            
        #PbO3--
        pot = GPbO3 + R*T*math.log(conc)
        urxn = pot + 6*uH + 4*ue - 3*uH2O - uPb
        #print("PbO3: ", urxn)
        if (urxn <= lowpot) :
            lowpot = urxn
            stable = 8
            
        #PbCO3
        
        
        
        # H2CO3 = -623.2068
        # HCO3 = -586.93152
        # # H2CO3 = -600
        # # HCO3 = -550
        # CO3 = -527.97896
        # border1 = 5.5
        # border2 = 11
        # if pH < border1:
        #     urxn = PbCO3 + 2*ue + 2*uH - (H2CO3 + R*T*math.log(Cconc))
        # elif pH < border2:
        #     urxn = PbCO3 + 2*ue + uH - (HCO3 + R*T*math.log(Cconc))
        # else:
        #     urxn = PbCO3 + 2*ue - (CO3 + R*T*math.log(Cconc))
        # #print("PbCO3: ",urxn )
        # if (urxn <= lowpot) :
        #     lowpot = urxn
        #     stable = 9
            
        # #Hc   
        # #PbOH3 = -575.3
        # #urxn = (hc + 7*OH - 2*(CO3 + R*T*math.log(Cconc)) - 3 * (PbOH3 + R*T*math.log(conc)))/3
        # #urxn = (hc + 6*ue - 2*(CO3 + R*T*math.log(Cconc)) -(2*OH+R*T*(pH-14)))/3
        # urxn = (hc + 2*uH + 4*ue - 2*uH2O - 2*(CO3 + R*T*math.log(Cconc)))/3 
        # #print(urxn)
        # if (urxn <= lowpot):
        #     lowpot = urxn
        #     stable = 10
            
        #ortho
        pconc = 0.0000001
        urxn = (pbphos + 16*uH + 16*ue - 8*uH2O - 2*(P+R*T*math.log(pconc)))/3
        if (urxn <= lowpot): 
            lowpot = urxn
            stable = 11
            
        # #PbO4----
        # pot = GPbO4 + R*T*math.log(conc)
        # urxn = pot + 8*uH + 4*ue - 4*uH2O - uPb
        # if (urxn < lowpot) :
        #     lowpot = urxn
        #     stable = 9
            
        #PbH2S
        # pot = GPbH2 + R*T*math.log(conc)
        # urxn = pot - 2*uH - 2*ue - uPb
        # if (urxn < lowpot) :
        #     lowpot = urxn
        #     stable = 10
    
        #print(lowpot)
        #print(pH , "," , V,":",stable)
        #print(stable)
        Z[i,j] = stable
        i+=1
    j+=1
    
    
fig, ax = plt.subplots()
levels = [-1, 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
colors_ = ['#85807b', '#db653d', '#e04a16', '#3ec760', '#2a8744', '#c92840', '#db7d42', '#bf3939', '#191cf7', '#d142f5', '#007BA7']
CS = ax.contourf(pH_,V_,Z, levels, colors=colors_)
# CS = ax.pcolormesh(pH_, V_, Z)
ax.contour(pH_, V_, Z, colors= 'k', linewidths=0.25, antialiased=True)

plt.text(6,-1.25,'$\mathrm{Pb}$')
plt.text(8, 2.5, '$\mathrm{PbO_{2}}$')
plt.text(1, 0.3, '$\mathrm{Pb^{2+}}$')
plt.text(8, 0, '$\mathrm{PbO}$')
plt.text(11, 0.25, '$\mathrm{Pb_{3}O_{4}}$')
# plt.text(-2, 2.5, '$\mathrm{Pb^{4+}}$')
plt.text(14, -0.25, '$\mathrm{HPbO_{2}^{-}}$')
# plt.text(0, -1.75, '$PbH_{2}$')
# plt.text(14.2, 2, '$\mathrm{PbO_{3}^{2-}}$')

a = 1.299-0.0592*pHvec
b = -0.059*pHvec
plt.plot(pHvec, a, '--', color='b')
plt.plot(pHvec, b, '--', color='b')
plt.text(0,1.1,'Water Oxidation', fontsize=11, rotation=-7, color='b')
plt.text(0,-0.2,'Water Reduction', fontsize=11, rotation=-7, color='b')


pHexp = [7,	7,	7,	7,	7,	7,	7,	7,	7,	7,	7,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10,	10]
Vexp = [-0.62,	-0.62,	-0.16,	-0.12,	0.06,	0.48,	0.58,	0.67,	0.74,	1.08,	1.08,	-0.8,	-0.42,	-0.28,	-0.26,	-0.03,	0.02,	0.24,	0.34,	0.46,	0.75,	0.75,	0.84,	0.94,	0.94,	1.24]
for i in list(range(3)) + list(range(11,12)):
    plt.plot(pHexp[i], Vexp[i], 'o', color = 'k')
for i in list(range(3,11))+list(range(13,26)):
    plt.plot(pHexp[i], Vexp[i], '^', color = 'red', markeredgewidth=0.5, markeredgecolor='k')


plt.xlabel('pH')
plt.ylabel('$\mathrm{V_{SHE}}$')
#plt.title(title_)
plt.savefig(title_, dpi=300)
print(title_)
print("Pb: ", conc)
print("C: ", Cconc)

        
