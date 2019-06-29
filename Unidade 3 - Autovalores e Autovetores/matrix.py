from __future__ import print_function


class Matrix:
    def __init__(self):
        pass

    def create_matrix(self, i, j):
        return [[0 for x in range(j)] for y in range(i)]

    def generate_identity_matrix(self, n):
        matrix = self.create_matrix(n, n)
        for i in range(n):
            matrix[i][i] = 1
        return matrix

    def multiply_matrices(self, A, B):
        C = self.create_matrix(len(A), len(B[0]))

        for m in range(len(C)):
            for n in range(len(C[0])):
                for x in range(len(A[0])):
                    C[m][n] += A[m][x]*B[x][n]

        return C

    def print_matrix(self, matrix):
        for line in matrix:
            print(line)

    def print_wolfram_input(self, matrix):
        print(str(matrix).replace('[', '{').replace(']', '}'))


matrix = Matrix()

matricula_franklyn = '397847'
matricula_daniel = '374169'

A, B, C, D, E, F = map(int, list(matricula_franklyn))

M = [[30+A+F, A, B, C, D],
     [A, 10+B+E, E, F, A+B],
     [B, E, 50+C+D, B+C, C+D],
     [C, F, B+C, 40-A, D+E],
     [D, A+B, C+D, D+E, 60-B]]

N = [[1, 3, -1], [3, 2, 4], [-1, 4, 10]]
xnew = [[1], [1], [1], [1], [1]]
xold = [[100], [100], [100], [100], [100]]
e = 0.000001

while(max([abs(xnew[i][0]-xold[i][0]) for i in range(len(xnew))]) > e):
    xold = [xnew[i] for i in range(len(xnew))]
    a_xnew = matrix.multiply_matrices(M, xnew)
    xnew = [[a_xnew[i][0]/max(a_xnew)[0]] for i in range(len(a_xnew))]
    print(a_xnew)
    print(max(a_xnew)[0])
    print(xnew)
    print("-----------------------------------------------------------------------")
