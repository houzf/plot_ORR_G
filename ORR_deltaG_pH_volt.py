#!/bin/python
import numpy as np

def  cal_Gibbs_free_energy_change(G, pH, volt, fout):
    dG_pH = 0.0591 * pH
    dG_volt = volt

    G_new = np.empty(shape=(4), dtype=np.float64)
    y = np.empty(shape=(5), dtype=np.float64)
    G_new[0] =G[0] + dG_volt + dG_pH
    G_new[1] =G[1] + dG_volt + dG_pH
    G_new[2] =G[2] + dG_volt + dG_pH
    G_new[3] =G[3] + dG_volt + dG_pH

    y[4] = 0.0
    y[3] = -G_new[3]
    y[2] = -G_new[3] - G_new[2]
    y[1] = -G_new[3] - G_new[2] - G_new[1]
    y[0] = -G_new[3] - G_new[2] - G_new[1] - G_new[0]
    x_start =[]
    x_end =[]
    with open(fout+'_hl.dat', 'w') as fx:
        for i in range(y.shape[0]):
            for j in range(3):
                x = 2.0*i+(j+1)*0.5
                fx.write('{:5.1f} {:10.3f}\n'.format(x, y[i]))
                if j == 0:
                    x_start.append(x)
                if j == 2:
                    x_end.append(x)

            if i != y.shape[0]-1:
                fx.write('{:5s} {:5s}\n'.format('-', '-'))


    with open(fout+'_dl.dat', 'w') as fz:
        for i in range(4):
            x_dash=np.linspace(x_end[i],x_start[i+1],5)
            slope = (y[i+1]-y[i])/(x_start[i+1]-x_end[i])
            for j in range(x_dash.shape[0]):
                fz.write('{:6.2f} {:10.3f}\n'.format(x_dash[j], (x_dash[j]-x_end[i])*slope + y[i]))
            if i != 3:
                fz.write('{:6s} {:6s}\n'.format('-', '-'))
    return y

if __name__ == "__main__":
    volt = 0.0
    pH= 13

    all_G={'FePc': [-1.406, -1.961, -0.985, -0.568]}

    for k,G in all_G.items():
        print(k, G)
        fout=k+'_pH13_0V'
        y_orr=cal_Gibbs_free_energy_change(G, pH, volt,fout)
