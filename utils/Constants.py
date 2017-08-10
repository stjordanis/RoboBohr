# Author: Burak Himmetoglu
# Date  : 08-18-2016
# -- Project RoboBohr -- # 

import numpy as np

## Example sdf 
#ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound_3D/01_conf_per_cmpd/SDF/00050001_00075000.sdf.gz

## Some constants
auToA = 0.529 # au is 0.529 A

# The periodic table: {element: [Z, m]}, no La-Lu and Ac-Lr series
periodic_table = {'H' : [1, 1.0079],
                  'He': [2, 4.0026],
                  'Li': [3, 6.941],
                  'Be': [4, 9.01218],
                  'B' : [5, 10.811],
                  'C' : [6, 12.0107],
                  'N' : [7, 14.0067],
                  'O' : [8, 15.9994],
                  'F' : [9, 18.9984],
                  'Ne': [10, 20.1797],
                  'Na': [11, 22.9898],
                  'Mg': [12, 24.3050],
                  'Al': [13, 29.9815],
                  'Si': [14, 28.0855],
                  'P' : [15, 30.9738],
                  'S' : [16, 32.065],
                  'Cl': [17, 35.453],
                  'Ar': [18, 39.948],
                  'K' : [19, 39.0983],
                  'Ca': [20, 40.078],
                  'Sc': [21, 44.9559],
                  'Ti': [22, 47.867],
                  'V' : [23, 50.9415],
                  'Cr': [24, 51.9961],
                  'Mn': [25, 54.9381],
                  'Fe': [26, 55.845],
                  'Co': [27, 58.933195],
                  'Ni': [28, 58.6934],
                  'Cu': [29, 63.546],
                  'Zn': [30, 65.38],
                  'Ga': [31, 69.723],
                  'Ge': [32, 72.64],
                  'As': [33, 74.9216],
                  'Se': [34, 78.96],
                  'Br': [35, 79.904],
                  'Kr': [36, 82.798],
                  'Rb': [37, 85.4678],
                  'Sr': [38, 87.62],
                  'Y' : [39, 88.9059],
                  'Zr': [40, 91.224],
                  'Nb': [41, 92.9064],
                  'Mo': [42, 95.96],
                  'Tc': [43, 97.9072],
                  'Ru': [44, 101.07],
                  'Rh': [45, 102.9055],
                  'Pd': [46, 106.42],
                  'Ag': [47, 107.8682],
                  'Cd': [48, 112.411],
                  'In': [49, 114.818],
                  'Sn': [50, 118.710],
                  'Sb': [51, 121.760],
                  'Te': [52, 127.60],
                  'I' : [53, 126.9045],
                  'Xe': [54, 131.293],  
                  'Cs': [55, 132.9055],
                  'Ba': [56, 137.327],
                  'Hf': [72, 178.49],
                  'Ta': [73, 180.9479],
                  'W' : [74, 183.84],
                  'Re': [75, 186.207],
                  'Os': [76, 190.23],
                  'Ir': [77, 192.217],
                  'Pt': [78, 195.084],
                  'Au': [79, 196.9666],
                  'Hg': [80, 200.59],
                  'Tl': [81, 204.3833],
                  'Pb': [82, 207.2],
                  'Bi': [83, 208.9804],
                  'Po': [84, 208.9824],
                  'At': [85, 209.9871],
                  'Rn': [86, 222.0176], 
                  'Fr': [87, 223],
                  'Ra': [88, 226],
                  'Rf': [104, 261],
                  'Db': [105, 262],
                  'Sg': [106, 266],
                  'Bh': [107, 264],
                  'Hs': [108, 277],
                  'Mt': [109, 268],
                  'Ds': [110, 271],
                  'Rg': [111, 272],
                  'Cn': [112, 285]}
                  


# Here is an example for studying CHNOPS
#dict_valences = {'H': 1, 'C': 4, 'N': 5, 'O': 6, 'P': 5, 'S': 6}
#dict_masses = {'H': 1.0, 'C': 12.0, 'N': 14.0, 'O': 15.999, 'P': 30.97, 'S': 32.06}
#dict_Z = {'H': 1, 'C': 6, 'N': 7, 'O': 8, 'P': 15, 'S': 16}
#dict_singleAtomEnergies = {'H': -0.917798, 'C': -11.275352, 'N': -19.577858, 'O': -33.171237, 'P': -15.12336, 'S': -22.522057}

## Some parameters for generating data matrices
#natMax = 50; box = 30; 

