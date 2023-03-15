import math
from pprint import pprint

inf = math.inf
matrix = [[0.0, 1.0, inf, inf, 6.0, 3.0],
          [1.0, 0.0, 6.0, inf, inf, 5.0],
          [inf, 6.0, 0.0, 1.0, 3.0, 3.0],
          [inf, inf, 1.0, 0.0, 2.0, inf],
          [6.0, inf, 3.0, 2.0, 0.0, 4.0],
          [3.0, 5.0, 3.0, inf, 4.0, 0.0]]

result = [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

for i in range(6):
    for j in range(6):
        for k in range(6):
            result[j][k] = min(float(matrix[j][i])+float(matrix[i][k]), float(matrix[j][k]))
    matrix = result[:]

for l in range(6):
    result[l] = list(map(int, result[l]))

pprint(result)