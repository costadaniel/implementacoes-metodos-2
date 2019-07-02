from __future__ import print_function
from matrix import Matrix


class Methods:
    def __init__(self):
        pass

    def power_method(self, given_matrix, given_vector, given_error):
        matrix = Matrix()
        xnew = [given_vector[i] for i in range(len(given_vector))]
        xold = [[given_vector[i][0]*100] for i in range(len(given_vector))]

        while(max([abs(xnew[i][0]-xold[i][0]) for i in range(len(xnew))]) > given_error):
            xold = [xnew[i] for i in range(len(xnew))]
            a_xnew = matrix.multiply_matrices(given_matrix, xnew)
            xnew = [[a_xnew[i][0]/max(a_xnew)[0]] for i in range(len(a_xnew))]
            print(a_xnew)
            print(max(a_xnew)[0])
            print(xnew)
            print("--------------------------------------------------")

        print("Maior autovalor: ", max(a_xnew)[0])
        return max(a_xnew)[0]

    def inverse_power_method(self, given_matrix, given_vector, given_error):
        pass
