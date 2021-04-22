From the Gibb free energy change (G<sub>i</sub>) for each elementary ORR step (standard 4e reaction steps) at 0 V and pH=0, one can obtain the Gi at a given voltage and pH.

Input: 
     volt, pH, Gi
 
 For example
 
    volt = 0.0
    pH= 13

    all_G={'FePc': [-1.406, -1.961, -0.985, -0.568]}

- G<sub>1</sub> = &#916;G<sub>&#42;OOH</sub> + 2&#916;G<sub>water</sub>

  O<sub>2</sub>(g) + H<sup>+</sup> + e<sup>-</sup> ---> &#42;OOH

- G<sub>2</sub>: &#42;OOH + H<sup>+</sup> + e<sup>-</sup> ---> &#42;O +H<sub>2</sub>O

- G<sub>3</sub>: &#42;O + H<sup>+</sup> + e<sup>-</sup> ---> &#42;OH

- G<sub>4</sub>: &#42;OH + H<sup>+</sup> + e<sup>-</sup> ---> H<sub>2</sub>O

FePc_pH0_0V_hl.dat:  for the horizontal line

FePc_pH0_0V_dl.dat: for the oblique line between two neighboring horizontal lines. 
