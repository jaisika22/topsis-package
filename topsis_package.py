#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


def topsis(matrix, weights, impacts):
    if matrix.shape[1] == len(weights) and matrix.shape[1] == len(impacts):
        
        matrix = matrix / np.linalg.norm(matrix, axis=0)
        
        matrix_w = matrix * weights
        
        ideal_best = np.max(matrix_w * impacts, axis=0)
        ideal_worst = np.min(matrix_w * impacts, axis=0)
        
        s1 = np.linalg.norm(matrix_w - ideal_best, axis=1)
        s2 = np.linalg.norm(matrix_w - ideal_worst, axis=1)
        
        p = s2 / (s2 + s1)
        
        rank = np.argsort(p)[::-1] + 1
        return p, rank
    
    else:
        print("wrong inputs")
        return None, None 


# In[ ]:


import sys
from mypackage import topsis

if __name__ == "__main__":
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    
    weights = np.array([float(x) for x in args.Weights.split(',')])
    impacts = np.array([1 if i == '+' else -1 for i in args.Impacts.split(',')])

    df = pd.read_csv(args.InputDataFile)
    data = df.iloc[:, 1:].values

    topsis = topsis(data, weights, impacts)
    results = topsis.calculate()

    
    with open(output_file, 'w') as f:
        for row in results:
            f.write(','.join(str(x) for x in row) + '\n')

