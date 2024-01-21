# TOPSIS-JAISIKA-102103378

## Project Description

The topsis package is a Python library for dealing with Multiple Criteria Decision Making (MCDM) problems by using the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS). This package provides a simple and efficient way to perform TOPSIS calculations for decision-making purposes.

## Installation

To install the topsis package, you can use pip:


'''pip install topsis'''

## Usage

To use the topsis package, you can call the topsis() function with the following arguments:

matrix: A numpy array containing the decision matrix.
weights: A 1D numpy array containing the weights of each criterion.
impacts: A 1D numpy array containing the impacts (+ or -) of each criterion.

Here's an example:


'''import numpy as np
from topsis import topsis'''

Let's say we have the following decision matrix:

Fund Name	P1    P2	P3	  P4	P5
M1	        0.7	0.49    3.1	42.2	11.62
M2	        0.71 0.5	5.2	53.7	15.03
M3	        0.9	0.81    4.6	55.8	15.53
M4	        0.63 0.4	6.5	53.8	15.33
M5      	0.86 0.74	5.8	30.5	9.48
M6	        0.83 0.69	6.2	49.8	14.38
M7	        0.63 0.4	4.2	64.3	17.38
M8	        0.78 0.61	5	40.9	11.82



### Define the decision matrix
matrix = np.array([[0.84, 0.71, 6.7, 42.1, 12.59],
    [0.91, 0.83, 7.0, 31.7, 10.11],
    [0.79, 0.62, 4.8, 46.7, 13.23],
    [0.78, 0.61, 6.4, 42.4, 12.55],
    [0.94, 0.88, 3.6, 62.2, 16.91],
    [0.88, 0.77, 6.5, 51.5, 14.91],
    [0.66, 0.44, 5.3, 48.9, 13.83],
    [0.93, 0.86, 3.4, 37.0, 10.55]])

### Define the weights
weights = np.array([1, 1, 1, 1, 1])

### Define the impacts
impacts = np.array([1, -1, 1, -1, 1])

### Calculate the TOPSIS results
p_score, rank = topsis(matrix, weights, impacts)

### Print the results
print("P-Score\tRank")
for i in range(len(p_score)):
    print("{:.4f}\t{:d}".format(p_score[i], rank[i]))



## Example

Fund Name	P1	  P2	P3	  P4	P5	  Topsis Score	Rank
M1	        0.7	  0.49	3.1	42.2	11.62	0.576991867	4
M2	        0.71  0.5	5.2	53.7	15.03	0.587964639	2
M3	        0.9	  0.81	4.6	55.8	15.53	0.577557644	6
M4	        0.63  0.4	6.5	53.8	15.33	0.594517337	8
M5	        0.86  0.74	5.8	30.5	9.48	0.583075847	5
M6	        0.83  0.69	6.2	49.8	14.38	0.587103664	7
M7	        0.63  0.4	4.2	64.3	17.38	0.582051301	3
M8	        0.78  0.61	5	40.9	11.82	0.585241478	1





## Other Notes

The first column and first row of the CSV file will be removed by the library before processing, so make sure the CSV follows the format as shown in the example.
Make sure the CSV does not contain categorical values.

## License

© 2024 Jaisika Bhatia

This repository is licensed under the MIT license. See LICENSE for details.