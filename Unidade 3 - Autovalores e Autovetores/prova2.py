from __future__ import print_function
from matrix import Matrix
from methods import Methods

methods = Methods()

matricula_franklyn = '397847'
matricula_daniel = '374169'

A, B, C, D, E, F = map(int, list(matricula_daniel))

M = [[30+A+F, A, B, C, D],
     [A, 10+B+E, E, F, A+B],
     [B, E, 50+C+D, B+C, C+D],
     [C, F, B+C, 40-A, D+E],
     [D, A+B, C+D, D+E, 60-B]]

V = [[1], [1], [1], [1], [1]]

N = [[1, 3, -1], [3, 2, 4], [-1, 4, 10]]
e = 0.000001

# methods.power_method(M, V, e)

print(M)
