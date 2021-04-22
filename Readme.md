From the Gibb free energy change (G<sub>i</sub>) for each elementary ORR step (standard 4e reaction steps) at 0 V and pH=0, one can obtain the Gi at a given voltage and pH.

Input: 
     volt, pH, Gi
 
 For example
 
    volt = 0.0
    pH= 13

    all_G={'FePc': [-1.406, -1.961, -0.985, -0.568]}

- G<sub>1</sub>: O<sub>2</sub>(g) + H<sup>+</sup> + e<sup>-</sup> ---> <sup>&#42;</sup>OOH

- G<sub>2</sub>: <sup>&#42;</sup>OOH + H<sup>+</sup> + e<sup>-</sup> ---> <sup>&#42;</sup>O +H<sub>2</sub>O

- G<sub>3</sub>: <sup>&#42;</sup>O + H<sup>+</sup> + e<sup>-</sup> ---> <sup>&#42;</sup>OH

- G<sub>4</sub>: <sup>&#42;</sup>OH + H<sup>+</sup> + e<sup>-</sup> ---> H<sub>2</sub>O

FePc_pH0_0V_hl.dat:  for the horizontal line

FePc_pH0_0V_dl.dat: for the oblique line between two neighboring horizontal lines. 
