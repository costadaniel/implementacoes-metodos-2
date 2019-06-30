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
