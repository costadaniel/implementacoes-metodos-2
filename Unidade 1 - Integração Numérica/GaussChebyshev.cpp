#include "GaussChebyshev.hpp"
#include "Function.hpp"
#include <iostream>
#include <cstdlib>
#include <cmath>

// #define _USE_MATH_DEFINES

using namespace std;

// N points
double GaussChebyshev::gaussChebyshevNPoints(Function function, int N){
  double result = 0;
  double x;
  double weight = M_PI / N;
  double aux;

  // Sum Loop
  for (int i = 1; i <= N; i++) {
    aux = (2*i - 1)/(2*N);
    x = cos((aux)*M_PI);
    cout << aux << endl;

    result += function.chebyshevType(x)*weight;

  }

  return result;
}
