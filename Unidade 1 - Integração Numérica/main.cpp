#include <iostream>
#include "Function.hpp"
#include "NewtonCotes.hpp"

int main(int argc, char const *argv[])
{
  Function function;
  NewtonCotes newtonCotes;
  
  std::cout << newtonCotes.openedToleranceNewtonCotesDegree1(function, 0, 0.8, 0.00001) << std::endl;
  std::cout << newtonCotes.openedToleranceNewtonCotesDegree2(function, 0, 0.8, 0.00001) << std::endl;
  std::cout << newtonCotes.openedToleranceNewtonCotesDegree3(function, 0, 0.8, 0.00001) << std::endl;
  std::cout << newtonCotes.openedToleranceNewtonCotesDegree4(function, 0, 0.8, 0.00001) << std::endl;
  
  return 0;
}
