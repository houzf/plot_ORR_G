#!/usr/bin/env  python
# written by HOU Zhufeng, email: hou.zhufeng@gmail.com

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import sys

def  cal_Gibbs_free_energy_change(G, pH, volt, fout, format_fout='Origin', is_start_zero=True):
    dG_pH = 0.0591 * pH
    dG_volt = volt

    if format_fout.lower()=='origin':
        sep_str='-'
    else:
        sep_str=' '


    G_new = np.empty(shape=(len(G)), dtype=np.float64)
    y = np.zeros(shape=(len(G)+1), dtype=np.float64)
    for i in range(len(G)):
        G_new[i] =G[i] + dG_volt + dG_pH

    """
    y[4] = 0.0
    y[3] = -G_new[3]
    y[2] = -G_new[3] - G_new[2]
    y[1] = -G_new[3] - G_new[2] - G_new[1]
    y[0] = -G_new[3] - G_new[2] - G_new[1] - G_new[0]
    """

    for i in range(len(G)+1):
        for j in range(i):
            y[i] += G_new[j]

    if is_start_zero:
        pass
    else:
        for i in range(len(G)+1):
            y[i] -= y[-1]

    x_start =[]
    x_end =[]

    horizontal_lines = []
    with open(fout+'_horizontal_line.dat', 'w') as fx:
        for i in range(y.shape[0]):
            for j in range(3):
                x = 2.0*i+(j+1)*0.5
                fx.write('{:5.1f} {:10.3f}\n'.format(x, y[i]))
                horizontal_lines.append([x, y[i]])
                if j == 0:
                    x_start.append(x)
                if j == 2:
                    x_end.append(x)

            if i != y.shape[0]-1:
                fx.write('{:5s} {:5s}\n'.format(sep_str, sep_str))


    inclined_lines = []
    with open(fout+'_inclined_line.dat', 'w') as fz:
        for i in range(G_new.shape[0]):
            x_dash=np.linspace(x_end[i],x_start[i+1],5)
            slope = (y[i+1]-y[i])/(x_start[i+1]-x_end[i])
            for j in range(x_dash.shape[0]):
                fz.write('{:6.2f} {:10.3f}\n'.format(x_dash[j], (x_dash[j]-x_end[i])*slope + y[i]))
                inclined_lines.append([x_dash[j], (x_dash[j]-x_end[i])*slope + y[i]])
            if i != G_new.shape[0]-1:
                fz.write('{:6s} {:6s}\n'.format(sep_str, sep_str))
                
    ah = np.array(horizontal_lines)
    ai = np.array(inclined_lines)
    array_horizontal_lines = np.array(np.split(ah, len(G)+1))
    array_inclined_lines = np.array(np.split(ai, len(G)))
    return array_horizontal_lines, array_inclined_lines

if __name__ == "__main__":
    ### Please adjust the values of the following variables
    volt = 0
    pH= 0
    format_fout='Origin'
    is_start_zero = True

    all_G={'A': [1.00533960000007, -0.156876649999958, -2.04267289999996,-2.04192315 , -1.6056124 ],
           'B': [1.0053396, -0.15687665, -2.0426729,  -1.99666515, -1.5728894 ],
           'C': [1.0053396, -0.08259665, -1.9960409, -1.97553215, -1.5937874]
          }
    substrates_list=[r'A$_2$C', r'B', r'C']
    colors_list=['black','red', 'blue', 'green', 'purple', 'cyan', 'magenta', 'brown', 'tomato', 'orange']
    reaction_species_list =[r'CO$_{2}$', r'COOH', r'CO', r'COH', r'C', r'CH$_{4}$', r'test']
    ### END ####
    
    all_hlines =[]
    all_ilines = []
    
    for key, G in all_G.items():
        print(key, G)
        fout=key+'_pH'+str(0)+'_'+str(volt)+'V'
        hori_lines, incl_lines=cal_Gibbs_free_energy_change(G, pH, volt,
                                       fout, format_fout, is_start_zero)
        if len(G)+1 > len(reaction_species_list):
            sys.exit("The number of reaction species in list is too fewer than that of reaction steps.")
        n_rs = len(G)+1
        
        all_hlines.append(hori_lines)
        all_ilines.append(incl_lines)
    
    with plt.style.context(['science', 'notebook', 'high-vis']):
        fig, ax = plt.subplots()
        ax.xaxis.set_minor_locator(AutoMinorLocator(1))
        ax.yaxis.set_minor_locator(AutoMinorLocator(4))
        ax.set_xlabel((r"Reaction pathway"))
        ax.set_ylabel((r"Gibbs free energy change (eV)"))
        ax.xaxis.set_ticks(all_hlines[0][:,1,0])
        ax.set_xticklabels(reaction_species_list[:n_rs])
        
        
        for i in range(len(all_hlines)):
            for j in range(all_hlines[i].shape[0]):
                if j == 0:
                    ax.plot(all_hlines[i][j,:,0], all_hlines[i][j,:,1], linestyle='-', 
                            color= colors_list[i], linewidth=1.2, label=substrates_list[i])
                else:
                    ax.plot(all_hlines[i][j,:,0], all_hlines[i][j,:,1], linestyle='-',  
                            color= colors_list[i], linewidth=1.2)

            for k in range(all_ilines[i].shape[0]):
                ax.plot(all_ilines[i][k,:,0], all_ilines[i][k,:,1], linestyle='--',  
                       color= colors_list[i], linewidth=1.2)
            
    

    plt.legend(loc='upper right', shadow=False, ncol=1)
    plt.savefig("Figure_deltaG_change1.png", dpi=300)
    plt.show()