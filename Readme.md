### ORR_deltaG_pH_volt.py
From the Gibb free energy change (&#916;G<sub>i</sub>) for each elementary ORR step (standard 4e reaction steps) at 0 V and pH=0, one can obtain the &#916;G<sub>i</sub> at a given voltage and pH.

Input: 
     volt, pH, &#916;G<sub>i</sub>
 
 For example
 
    volt = 0.0
    pH= 13

    all_G={'FePc': [-1.406, -1.961, -0.985, -0.568]}

- &#916;G<sub>1</sub> = &#916;G<sub>&#42;OOH</sub> + 2&#916;G<sub>water</sub>

  O<sub>2</sub>(g) + H<sup>+</sup> + e<sup>-</sup> ---> &#42;OOH

- &#916;G<sub>2</sub> = &#916;G<sub>&#42;O</sub> - &#916;G<sub>&#42;OOH</sub>
   
   &#42;OOH + H<sup>+</sup> + e<sup>-</sup> ---> &#42;O +H<sub>2</sub>O

- &#916;G<sub>3</sub> = &#916;G<sub>&#42;OH</sub> - &#916;G<sub>&#42;O</sub>
   
   &#42;O + H<sup>+</sup> + e<sup>-</sup> ---> &#42;OH

- &#916;G<sub>4</sub> = -&#916;G<sub>&#42;OH</sub>
  
  &#42;OH + H<sup>+</sup> + e<sup>-</sup> ---> H<sub>2</sub>O

&#916;G<sub>water</sub> = -2.46 eV is the experimental formation energy of water molecule. &#916;G<sub>&#42;O</sub>, &#916;G<sub>&#42;OH</sub>, and &#916;G<sub>&#42;OOH</sub> are the adsorption Gibbs free energies of ORR intermediate species (&#42;O, &#42;OH, and &#42;OOH) at the room temperature and standard pressure.


- FePc_pH13_0V_hl.dat:  for the horizontal line

- FePc_pH13_0V_dl.dat: for the oblique line between two neighboring horizontal lines. 

Based on the above output files of this python script file, one can use the gnuplot or Origin software to draw the diagram of free energy changes in the ORR.

### free_energy_change_plot.py
For more types of chemical reactions.
```
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
```
